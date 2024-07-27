# flask_backend/app.py
from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

def query_db(query, args=(), one=False):
    con = sqlite3.connect('data.db')
    cur = con.cursor()
    cur.execute(query, args)
    rv = cur.fetchall()
    con.close()
    return (rv[0] if rv else None) if one else rv

@app.route('/api/data', methods=['GET'])
def get_data():
    query = "SELECT * FROM data WHERE 1=1"
    args = []

    filters = {
        'year': 'year=?',
        'topics': 'topics=?',
        'sector': 'sector=?',
        'region': 'region=?',
        'pest': 'pest=?',
        'source': 'source=?',
        'swot': 'swot=?',
        'country': 'country=?',
        'city': 'city=?'
    }

    for key, sql_filter in filters.items():
        value = request.args.get(key)
        if value:
            query += f" AND {sql_filter}"
            args.append(value)

    data = query_db(query, args)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
