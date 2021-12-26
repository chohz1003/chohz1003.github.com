import pymysql.cursors
from PIL import Image
import base64
from io import BytesIO


buffer = BytesIO()
im = Image.open('C:\\Users\\swh\\Desktop\\img\\ㅠ.jpg')
# im.show()
im.save(buffer, format='jpeg')
img_str = base64.b64encode(buffer.getvalue())
print(img_str)  # 변환된 데이터 확인 가능

conn = pymysql.connect(host='183.99.87.90',
        user='root',
        password='swhacademy!',#ㄱㄴㅁㅂㅅㅇㅊㅋㅌㅣ png
        db='hangcheol',
        charset='utf8')
try:
    with conn.cursor() as cursor:
        sql = 'INSERT INTO img (문자, 이미지) VALUES (%s, %s)'
        cursor.execute(sql, ('ㅠ', img_str))
    conn.commit()
    print(cursor.lastrowid)
finally:
    conn.close()
