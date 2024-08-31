import pymysql
from PIL import Image
import base64
from io import BytesIO
import matplotlib.pyplot as plt

conn = pymysql.connect(host='183.99.87.90',
        user='root',
        password='swhacademy!',
        db='hangcheol',
        charset='utf8')
try:
    with conn.cursor() as cursor:
        sql = 'SELECT 이미지 FROM img'
        cursor.execute(sql)
        results = cursor.fetchall()
        #print(type(results[0][0]))
        #print(type(results))
        img = Image.open(BytesIO(base64.b64decode(results[0][0])))
        print(img)
        plt.imshow(img)
        plt.show()

finally:
    conn.close()
