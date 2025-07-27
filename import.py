import csv
import sqlite3

def insert_data_from_csv(db_name='hkboxoffice_FDF_projects.db', csv_file='hkboxoffice_FDF_projects.csv'):
    # 連接資料庫
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # 開啟big5編碼的CSV檔案，遇到無法解碼的字元忽略，防止錯誤
    with open(csv_file, newline='', encoding='big5', errors='ignore') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            # 取得並清理每個欄位資料
            Reference = row['Reference'].strip()
            Film_Title_EN = row['Film Title_EN'].strip()
            Film_Title_TC = row['Film Title_TC'].strip()
            Film_Title_SC = row['Film Title_SC'].strip()
            Funding_Scheme = row['Funding Scheme'].strip()
            Hong_Kong_Box_Office = row['Hong Kong Box Office (HK$)'].strip()
            Last_Update = row['Last Update'].strip()

            # 將Empty字串或非數字轉換成 None
            Funding_Scheme = int(Funding_Scheme) if Funding_Scheme.isdigit() else None
            Hong_Kong_Box_Office = int(Hong_Kong_Box_Office) if Hong_Kong_Box_Office.isdigit() else None

            # 插入資料庫
            cursor.execute('''
                INSERT INTO FilmFunding 
                (Reference, Film_Title_EN, Film_Title_TC, Film_Title_SC, Funding_Scheme, Hong_Kong_Box_Office, Last_Update)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (Reference, Film_Title_EN, Film_Title_TC, Film_Title_SC, Funding_Scheme, Hong_Kong_Box_Office, Last_Update))

    # 提交變更並關閉連線
    conn.commit()
    conn.close()
    print(f'已成功插入CSV資料到 {db_name}。')

if __name__ == '__main__':
    insert_data_from_csv()
