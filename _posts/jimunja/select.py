import pymysql

def selectt(word):
    conn = pymysql.connect(host='183.99.87.90',
            user='root',
            password='swhacademy!',
            db='hangcheol',
            charset='utf8')
    try:
        with conn.cursor() as cursor:
            sql = f"SELECT * FROM img WHERE 문자 = '{word}'"
            cursor.execute(sql)
            results = cursor.fetchall()
            return results[0][1]
    finally:
        conn.close()
