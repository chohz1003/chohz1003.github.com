import pymysql.cursors
import base64
#이미지 -> sql

conn = pymysql.connect(host='183.99.87.90',
        user='root',
        password='swhacademy!',#ㄱㄴㅁㅂㅅㅇㅊㅋㅌㅣ png
        db='hangcheol',
        charset='utf8')
try:
    a = ['ㄱ','ㄲ','ㄴ','ㄷ','ㄸ','ㄹ','ㅁ','ㅂ','ㅃ','ㅅ','ㅆ','ㅇ','ㅈ','ㅉ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ','ㅏ','ㅐ','ㅑ','ㅒ','ㅓ','ㅔ','ㅕ','ㅖ','ㅗ','ㅚ','ㅛ','ㅜ','ㅟ','ㅠ','ㅡ','ㅢ','ㅣ']
    for b in a:
        with open(f'C:\\Users\\user\\Downloads\\img\\{b}.png', 'rb') as img:
            base64_string = base64.b64encode(img.read())
            binary_image = base64_string.decode('UTF-8')
        with conn.cursor() as cursor:
            sql = 'INSERT INTO img (문자, 이미지) VALUES (%s, %s)'
            cursor.execute(sql, (b, binary_image))
        conn.commit()
finally:
    conn.close()
