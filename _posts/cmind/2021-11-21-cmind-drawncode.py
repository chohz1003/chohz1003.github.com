import threading, socket
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
from worrd import gud

def recvMsg(soc): #좌표 받음
    while True:
        data = soc.recv(15)
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
    def __init__(self):
        super().__init__()
        self.image = QImage(QSize(400, 400), QImage.Format_RGB32)
        self.image.fill(Qt.white)
        self.brush_size = 5
        self.brush_color = Qt.black
        self.initUI()
        self.show()


    def initUI(self): #창 설정
        self.setWindowTitle('Simple Painter')
        self.setGeometry(700, 200, 400, 400)
        a = gud()
        button = QPushButton(a[1], self)
        button.move(150, 0)

        self.line_edit = QLineEdit(self)
        self.line_edit.move(25, 365)

        self.button = QPushButton(self)
        self.button.move(200, 365)
        self.button.setText('정답')
        self.button.clicked.connect(self.button_event)

    def button_event(self): #정답버튼 눌렀을때
        text = self.line_edit.text()
        ekq = gud()
        if text == ekq[0]:
            QMessageBox.about(self, "정답", "정답")
        else:
            QMessageBox.about(self, "오답", "오답")

    def paintEvent(self, e):
        canvas = QPainter(self)
        canvas.drawImage(self.rect(), self.image, self.image.rect())

    def sok(self, q,w,e,r):
        painter = QPainter(self.image)
        painter.setPen(QPen(self.brush_color, self.brush_size, Qt.SolidLine, Qt.RoundCap))
        painter.drawLine(int(q), int(w),int(e),int(r)) #  (1칸전,현재)              drawline(x1, y1, x2, y2)
        self.update()

if __name__ == '__main__':
    main()
    app = QApplication(sys.argv)
    ex = MyApp() #창
    sys.exit(app.exec_())
    client_socket.close()
