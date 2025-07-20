import json
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/items')
def items():
    try:
        with open('items.json') as f:
            data = json.load(f)
            items_list = data.get('items', [])
    except Exception as e:
        print(f"Error leyendo items.json: {e}")
        items_list = []

    return render_template('items.html', items=items_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
