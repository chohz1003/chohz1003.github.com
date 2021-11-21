import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import re
import socket,threading
import pyautogui
from worrd import gud

def recvMsg(soc): #좌표 받음
    while True:
        data = soc.recv(15) #길이를 
        msg = data.decode()
        a=msg.split(',')
        ex.sok(a[0],a[1],a[2],a[3])
    soc.close()

class Client:
    ip = 'localhost'
    port = 4444

    def __init__(self):
        self.client_soc = None

    def conn(self):
        self.client_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_soc.connect((Client.ip, Client.port))

    def run(self):
        self.conn()
        t2 = threading.Thread(target=recvMsg, args=(self.client_soc,))
        t2.start()

def main():
    c = Client()
    c.run()

client_socket  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket .connect(("localhost", 4444))

class MyApp(QMainWindow): #창 
    xy=[]

    def __init__(self):
        super().__init__()
        self.image = QImage(QSize(400, 400), QImage.Format_RGB32)
        self.image.fill(Qt.white)
        self.brush_size = 5
        self.brush_color = Qt.black
        self.initUI()
        self.show()

    def print_label(self, vbutton, vlabel):
        vlabel.setText(vbutton.text())

    def initUI(self): #창 설정
        self.setWindowTitle('Simple Painter')
        self.setGeometry(300, 200, 400, 400) 
        self.intialL1 = 'First Label' 
        a=gud()
        button = QPushButton(a[0], self)
        button.move(150, 0)

    def paintEvent(self, e):
        canvas = QPainter(self)
        canvas.drawImage(self.rect(), self.image, self.image.rect())
        qp = QPainter()
        qp.begin(self)
        self.draw_line(qp)
        qp.end()

    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton: #처음
            self.drawing = True
            self.last_point = e.pos() #마우스 좌표

    def mouseMoveEvent(self, e):
        if (e.buttons() & Qt.LeftButton) & self.drawing: #처음 빼고
            painter = QPainter(self.image)
            painter.setPen(QPen(self.brush_color, self.brush_size, Qt.SolidLine, Qt.RoundCap))
            a=str(self.last_point)+str(e.pos())
            painter.drawLine(self.last_point, e.pos()) #  (1칸전,현재)              drawline(x1, y1, x2, y2)
            self.last_point = e.pos() #마우스커서좌표
            b = re.findall("\d+", a)
            del b[0]
            del b[2]
            c = ''
            for a in b:
                a=str(a)
                k=a.zfill(3) #길이를 
                c = c + str(k) + ','
            c=c[:-1] #좌표
            b = []
            u=re.findall("\d+", str(self.geometry()))
            del u[0]
            self.xy=u
            i = re.findall("\d+", str(pyautogui.position()))
            if int(i[0]) >= int(u[0]) and int(i[0]) <= int(u[0])+int(u[2]) and int(i[1]) >= int(u[1])+30 and int(i[1]) <= int(u[1])+int(u[3])-40:#그려지는 좌표 제한
                client_socket.send(c.encode()) #좌표 전송

    def sok(self, q,w,e,r):
        painter = QPainter(self.image)
        painter.setPen(QPen(self.brush_color, self.brush_size, Qt.SolidLine, Qt.RoundCap))
        painter.drawLine(int(q), int(w),int(e),int(r)) #  (1칸전,현재)              drawline(x1, y1, x2, y2)
        self.update()

    def draw_line(self, qp): 
        qp.setPen(QPen(Qt.white, 40))
        qp.drawLine(0, 380, 400, 380)
        qp.setPen(QPen(Qt.white, 37))
        qp.drawLine(0, 10, 400, 10)

if __name__ == '__main__':
    main()
    app = QApplication(sys.argv)
    ex = MyApp() #창
    sys.exit(app.exec_())
    client_socket.close()
