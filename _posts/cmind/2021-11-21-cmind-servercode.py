import threading, socket

class Room: #채팅방
    def __init__(self):
        self.clients = []#접속한 클라이언트를 담당하는 ChatClient 객체 저장

    def addClient(self, c):#클라이언트 하나를 채팅방에 추가
        self.clients.append(c)

    def sendAllClients(self, msg):
        for c in self.clients:
            c.sendMsg(msg)

class ChatClient:#텔레 마케터: 클라이언트 1명이 전송한 메시지를 받고, 받은 메시지를 다시 되돌려줌
    def __init__(self, id, soc, r):
        self.id = id    #클라이언트 id
        self.soc = soc  #담당 클라이언트와 1:1 통신할 소켓
        self.room = r   #채팅방 객체

    def recvMsg(self):
        while True:
            data = self.soc.recv(15)
            msg = data.decode()
            self.room.sendAllClients(msg)

    def sendMsg(self, msg): #담당한 클라이언트 1명에게만 메시지 전송
        self.soc.sendall(msg.encode(encoding='utf-8'))

    def run(self):
        t = threading.Thread(target=self.recvMsg, args=())
        t.start()

class ServerMain:
    ip = 'localhost'
    port = 4444

    def __init__(self):
        self.room = Room()
        self.server_soc = None

    def open(self):
        self.server_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_soc.bind((ServerMain.ip, ServerMain.port))
        self.server_soc.listen()

    def run(self):
        self.open()
        print('start')
        while True:
            c_soc, addr = self.server_soc.accept()
            cc = ChatClient(id, c_soc, self.room)
            self.room.addClient(cc)
            cc.run()

def main():
    server = ServerMain()
    server.run()

main()
