from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS transaksi 
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, barang TEXT, harga INTEGER)''')
    conn.commit()
    conn.close()

@app.route('/')
def home():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM transaksi")
    data = c.fetchall()
    conn.close()
    return render_template('index.html', data=data)

@app.route('/add', methods=['POST'])
def add():
    barang = request.form['barang']
    harga = request.form['harga']
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("INSERT INTO transaksi (barang, harga) VALUES (?, ?)", (barang, harga))
    conn.commit()
    conn.close()
    return redirect('/')

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)
