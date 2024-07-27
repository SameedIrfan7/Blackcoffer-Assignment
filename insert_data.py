import sqlite3
import json

# Correct path to the JSON file
with open('jsondata.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Connect to SQLite database
conn = sqlite3.connect('data.db')
c = conn.cursor()

# Create table
c.execute('''
    CREATE TABLE IF NOT EXISTS data (
        id INTEGER PRIMARY KEY,
        intensity INTEGER,
        likelihood INTEGER,
        relevance INTEGER,
        year INTEGER,
        country TEXT,
        topics TEXT,
        region TEXT,
        city TEXT,
        pest TEXT,
        source TEXT,
        swot TEXT
    )
''')

# Insert data
for entry in data:
    c.execute('''
        INSERT INTO data (intensity, likelihood, relevance, year, country, topics, region, city, pest, source, swot)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        entry.get('intensity'),
        entry.get('likelihood'),
        entry.get('relevance'),
        entry.get('year'),
        entry.get('country'),
        entry.get('topics'),
        entry.get('region'),
        entry.get('city'),
        entry.get('pest'),
        entry.get('source'),
        entry.get('swot')
    ))

# Commit and close
conn.commit()
conn.close()