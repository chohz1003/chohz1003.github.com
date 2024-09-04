import pymysql.cursors
import base64

conn = pymysql.connect(host='183.99.87.90',
        user='root',
        password='swhacademy!',
        db='hangcheol',
        charset='utf8')
try:
    message = ['ㄱ','ㄲ','ㄴ','ㄷ','ㄸ','ㄹ','ㅁ','ㅂ','ㅃ','ㅅ','ㅆ','ㅇ','ㅈ','ㅉ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ','ㅏ','ㅐ','ㅑ','ㅒ','ㅓ','ㅔ','ㅕ','ㅖ','ㅗ','ㅚ','ㅛ','ㅜ','ㅟ','ㅠ','ㅡ','ㅢ','ㅣ','입력','다시입력']
    for messages in message:
        with open(f'C:\\Users\\chohc\\Downloads\\img\\{messages}.png', 'rb') as img:
            base64_string = base64.b64encode(img.read())
            binary_image = base64_string.decode('UTF-8')
        with conn.cursor() as cursor:
            sql = 'INSERT INTO img (문자, 이미지) VALUES (%s, %s)'
            cursor.execute(sql, (messages, binary_image))
        conn.commit()
finally:
    conn.close()