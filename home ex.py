import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('hkboxoffice_FDF_projects.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Create a table with the specified columns
cursor.execute('''
CREATE TABLE IF NOT EXISTS films (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    film_title_en TEXT NOT NULL,
    film_title_sc TEXT,
    funding_scheme TEXT,
    hong_kong_box_office REAL,
    last_update TEXT
)
''')

# Commit the changes and close the connection
conn.commit()
conn.close()

print("SQLite database and table created successfully.")