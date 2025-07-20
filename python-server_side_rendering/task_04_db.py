import json
import csv
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

def read_json_file():
    try:
        with open('products.json') as f:
            data = json.load(f)
        return data
    except Exception:
        return []

def read_csv_file():
    products = []
    try:
        with open('products.csv', newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                products.append({
                    'id': int(row['id']),
                    'name': row['name'],
                    'category': row['category'],
                    'price': float(row['price'])
                })
        return products
    except Exception:
        return []

def read_sqlite_db():
    try:
        conn = sqlite3.connect('products.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, category, price FROM Products')
        rows = cursor.fetchall()
        products = []
        for row in rows:
            products.append({
                'id': row['id'],
                'name': row['name'],
                'category': row['category'],
                'price': row['price']
            })
        conn.close()
        return products
    except Exception:
        return []

@app.route('/products')
def products():
    source = request.args.get('source', '').lower()
    product_id = request.args.get('id')

    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', error="Wrong source", products=None)

    # Leer datos según source
    if source == 'json':
        products_data = read_json_file()
    elif source == 'csv':
        products_data = read_csv_file()
    else:
        products_data = read_sqlite_db()

    # Filtrar por id si existe
    if product_id:
        try:
            pid = int(product_id)
            filtered = [p for p in products_data if p['id'] == pid]
            if not filtered:
                return render_template('product_display.html', error="Product not found", products=None)
            products_data = filtered
        except ValueError:
            return render_template('product_display.html', error="Invalid id parameter", products=None)

    return render_template('product_display.html', products=products_data, error=None)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
