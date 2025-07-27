import sqlite3

def init_db(db_name='hkboxoffice_FDF_projects.db'):
    # 連接到SQLite資料庫（如果資料庫不存在會自動建立）
    conn = sqlite3.connect('hkboxoffice_FDF_projects.db')
    cursor = conn.cursor()

    # 建立FilmFunding表格的SQL語句
    create_table_sql = '''
    CREATE TABLE IF NOT EXISTS FilmFunding (
        Reference TEXT PRIMARY KEY,               -- 項目編號
        Film_Title_EN TEXT,                       -- 英文名稱
        Film_Title_TC TEXT,                       -- 繁體中文名稱
        Film_Title_SC TEXT,                       -- 簡體中文名稱
        Funding_Scheme INTEGER,                   -- 資助計劃編碼: 1,2,3
        Hong_Kong_Box_Office INTEGER,             -- 香港票房（港元）
        Last_Update TEXT                          -- 更新日期 dd/mm/yyyy
    );
    '''

    # 執行建立資料表的命令
    cursor.execute(create_table_sql)

    # 提交更改並關閉連接
    conn.commit()
    conn.close()
    print(f"資料庫 {'hkboxoffice_FDF_projects.db'} 初始化完成，已建立FilmFunding資料表。")

# 主程式區域執行初始化
if __name__ == '__main__':
    init_db()
