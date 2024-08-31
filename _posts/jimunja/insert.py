import pymysql.cursors
import base64
#이미지 -> sql

conn = pymysql.connect(host='183.99.87.90',
        user='root',
        password='swhacademy!',#ㄱㄴㅁㅂㅅㅇㅊㅋㅌㅣ png
        db='hangcheol',
        charset='utf8')
try:
    with open('C:\\Users\\chohc\\Downloads\\img\\ㅛ.png', 'rb') as img:
        base64_string = base64.b64encode(img.read())
        print(base64_string)
        binary_image = base64_string.decode('UTF-8')
        print(binary_image)
    with conn.cursor() as cursor:
        sql = 'INSERT INTO img (문자, 이미지) VALUES (%s, %s)'
        cursor.execute(sql, ('ㅛ', binary_image))
    conn.commit()
    print(cursor.lastrowid)
finally:
    conn.close()
