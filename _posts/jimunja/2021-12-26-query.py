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
#########################################################################
import pymysql.cursors
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
        for result in results:
            print(result)
finally:
    conn.close()
#####################################################
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import hgtk

class MyApp(QMainWindow): #창
    def __init__(self):
        super().__init__()
        #self.image = QImage(QSize(400, 400), QImage.Format_RGB32)
        #self.image.fill(Qt.white)
        self.initUI()
        self.show()

    def initUI(self): #창 설정
        self.setWindowTitle('Simple Painter')
        self.setGeometry(450, 100, 600, 600)

        self.line_edit = QLineEdit(self)
        self.line_edit.move(25, 550)

        self.button = QPushButton(self)
        self.button.move(500, 550)
        self.button.setText('입력')
        self.button.clicked.connect(self.button_event)

        self.label = QLabel("", self)
        self.label.move(5, -70)  # 문자열 포맷팅
        self.label.resize(500, 200)


    def button_event(self): #정답버튼 눌렀을때
        text = self.line_edit.text()
        #print(text)

        p = text
        c = []
        for b in range(len(p)):
            c.append(hgtk.letter.decompose(p[b]))
        print(c)
        o=['ㄱ','ㄴ']
        l=5
        ll=-70
        for v in o:
            print(v)
            self.label.move(l,ll)
            self.img = QPixmap("C:\\Users\\swh\\Desktop\\img\\"+str(v)+".png")
            self.img = self.img.scaledToWidth(50)
            self.button1Clicked()
            print(1)
            l=l+60
            #ll=ll+60

    def button1Clicked(self):
        self.label.setPixmap(self.img)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp() #창
    sys.exit(app.exec_())
    client_socket.close()
