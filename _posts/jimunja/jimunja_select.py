import pymysql

def select(word):
    conn = pymysql.connect(host='183.99.87.90',
            user='root',
            password='swhacademy!',
            db='hangcheol',
            charset='utf8')
    try:
        with conn.cursor() as cursor:
            fake_sql = f"SELECT IFNULL(MAX('문자'), 0) '문자' FROM img WHERE 문자 = '{word}'"
            cursor.execute(fake_sql)
            results = cursor.fetchall()
            if results[0][0] == '0':
                sql = "SELECT * FROM img WHERE 문자 = '다시입력'"
            else:
                sql = f"SELECT * FROM img WHERE 문자 = '{word}'"
            cursor.execute(sql)
            results = cursor.fetchall()
            return results[0][1].decode('utf-8')
    finally:
        conn.close()
