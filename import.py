import sqlite3
import csv

# Connect to SQLite database
conn = sqlite3.connect('hkboxoffice_FDF_projects.db')
cursor = conn.cursor()

# Path to your CSV file
csv_file_path = 'hkboxoffice_FDF_projects.csv'

# Read the CSV file encoded in Big5
with open(csv_file_path, mode='r', encoding='big5', errors='replace') as file:
    reader = csv.DictReader(file)

    # Prepare insert statement
    insert_statement = '''
    INSERT INTO films (film_title_en, film_title_sc, funding_scheme, hong_kong_box_office, last_update)
    VALUES (?, ?, ?, ?, ?)
    '''

    # Iterate through each row in the CSV and execute the insert statement
    for row in reader:
        cursor.execute(insert_statement, (
            row['Film Title_TC'],
            row['Film Title_SC'],
            row['Funding Scheme'],
            row['Hong Kong Box Office (HK$)'] if row['Hong Kong Box Office (HK$)'] else None,
            row['Last Update']
        ))

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Data inserted into the database successfully.")