import json
import csv
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
                # Convert price to float and id to int for consistency
                products.append({
                    'id': int(row['id']),
                    'name': row['name'],
                    'category': row['category'],
                    'price': float(row['price'])
                })
        return products
    except Exception:
        return []

@app.route('/products')
def products():
    source = request.args.get('source', '').lower()
    product_id = request.args.get('id')

    if source not in ['json', 'csv']:
        return render_template('product_display.html', error="Wrong source", products=None)

    # Read data based on source
    if source == 'json':
        products_data = read_json_file()
    else:
        products_data = read_csv_file()

    # Filter by id if provided
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
