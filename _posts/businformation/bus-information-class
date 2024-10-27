import requests
from bs4 import BeautifulSoup

class busclass:
    information1 = [] #n번버스
    information2 = [] #n번버스  하나
    information3 = [] #n번버스  하나 실시간 버스위치
    information4 = dict()  # n번버스 하나 정류장 정보
    information5 = dict() #n번버스 하나 정류장 남은 시간 정류장
    information6 = [] #정류장 가는 버스

    def bus1(self,num): #n번버스
        self.information1 = []
        #https://api.gbis.go.kr/ws/rest/busrouteservice/page?serviceKey=1234567890&pageSize=20&pageNo=1&keyword=8
        response = requests.get(f'https://api.gbis.go.kr/ws/rest/busrouteservice/page?serviceKey=1234567890&pageSize=20&pageNo=1&keyword={num}')
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        all = soup.select('routeList > busRouteList')
        for one in all:
            bus = dict()
            bus['지역'] = one.select('regionName')[0].get_text()
            bus['끝'] = one.select('edStaNm')[0].get_text()
            bus['시작'] = one.select('stStaNm')[0].get_text()
            bus['종류'] = one.select('routeTypeName')[0].get_text()
            bus['루트id'] = one.select('routeId')[0].get_text()
            bus['스테이션id'] = one.select('stStaId')[0].get_text()
            self.information1.append(bus)
        return self.information1

    def bus2(self, num): #n번버스  하나
        self.information2 = []
        #https://api.gbis.go.kr/ws/rest/busrouteservice/station?serviceKey=1234567890&routeId=165000012
        response = requests.get(f'https://api.gbis.go.kr/ws/rest/busrouteservice/station?serviceKey=1234567890&routeId={num}')
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        all = soup.select('busRouteStationList')
        for one in all:
            bus = dict()
            bus['지역'] = one.select('regionName')[0].get_text()
            bus['이름'] = one.select('stationName')[0].get_text()
            bus['stationid'] = one.select('stationId')[0].get_text()
            self.information2.append(bus)
        return self.information2

    # def bus3(self, num): #n번버스  하나  실시간 버스위치
    #     self.information3 = []
    #     https://api.gbis.go.kr/ws/rest/buslocationservice?serviceKey=1234567890&routeId=165000012
    #     response = requests.get(f'https://api.gbis.go.kr/ws/rest/buslocationservice?serviceKey=1234567890&routeId={num}')
    #     html = response.text
    #     soup = BeautifulSoup(html, 'html.parser')
    #     all = soup.select('busRouteStationList')
    #     for one in all:
    #         bus = dict()
    #
    #         self.information3.append(bus)
    #     return self.information3

    def bus4(self, num): #n번버스 하나 정류장 정보
        self.information4 = dict()
        #https://api.gbis.go.kr/ws/rest/busstationservice/info?serviceKey=1234567890&stationId=164000377
        response = requests.get(f'https://api.gbis.go.kr/ws/rest/busstationservice/info?serviceKey=1234567890&stationId={num}')
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        self.information4['x좌표'] = soup.select('x')[0].get_text()
        self.information4['y좌표'] = soup.select('y')[0].get_text()
        self.information4['이름'] = soup.select('stationName')[0].get_text()
        self.information4['스테이션id'] = soup.select('stationId')[0].get_text()
        return self.information4

    def bus5(self, num1, num2, num3): #n번버스 하나 정류장 남은 시간 정류장
        self.information5 = dict()
        #https://api.gbis.go.kr/ws/rest/busarrivalservice/tv?serviceKey=1234567890&stationId=164000377&routeId=165000012&staOrder=1
        response = requests.get(f'https://api.gbis.go.kr/ws/rest/busarrivalservice/tv?serviceKey=1234567890&stationId={num1}&routeId={num2}&staOrder={num3}')
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        self.information5['남은 정류장1'] = soup.select('locationNo1')[0].get_text()
        self.information5['남은 정류장2'] = soup.select('locationNo2')[0].get_text()
        self.information5['남은 시간1'] = soup.select('predictTime1')[0].get_text()
        self.information5['남은 시간2'] = soup.select('predictTime2')[0].get_text()
        self.information5['루트id'] = soup.select('routeId')[0].get_text()
        self.information5['스테이션id'] = soup.select('stationId')[0].get_text()
        return self.information5

    def bus6(self,num): #정류장 가는 버스
        self.information6 = []
        #https://api.gbis.go.kr/ws/rest/busarrivalservice/tvstation?serviceKey=1234567890&stationId=164000377
        response = requests.get(f'https://api.gbis.go.kr/ws/rest/busarrivalservice/tvstation?serviceKey=1234567890&stationId={num}')
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        all = soup.select('busArrivalList')
        for one in all:
            bus = dict()
            bus['지역'] = one.select('routeDestName')[0].get_text()
            bus['버스번호'] = one.select('routeName')[0].get_text()
            bus['루트id'] = one.select('routeId')[0].get_text()
            bus['스테이션id'] = one.select('stationId')[0].get_text()
            self.information6.append(bus)
        return self.information6
