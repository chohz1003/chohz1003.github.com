import pymysql

def select(word_list):
    w_list = []
    conn = pymysql.connect(host='183.99.87.90',
            user='root',
            password='swhacademy!',
            db='hangcheol',
            charset='utf8')
    try:
        for words in word_list:
            for word in words:
                if word == ' ':
                    continue
                with conn.cursor() as cursor:
                    if word_list == '입력':
                        sql = "SELECT * FROM img WHERE 문자 = '입력'"
                    else:
                        fake_sql = f"SELECT IFNULL(MAX('문자'), 0) '문자' FROM img WHERE 문자 = '{word}'"
                        cursor.execute(fake_sql)
                        results = cursor.fetchall()
                        if results[0][0] == '0':
                            sql = "SELECT * FROM img WHERE 문자 = '다시입력'"
                        else:
                            sql = f"SELECT * FROM img WHERE 문자 = '{word}'"
                    cursor.execute(sql)
                    results = cursor.fetchall()
                    w_list.append(results[0][1].decode('utf-8'))
        return w_list
    finally:
        conn.close()
