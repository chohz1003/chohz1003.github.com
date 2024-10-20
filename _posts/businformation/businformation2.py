import requests
from bs4 import BeautifulSoup

def buss(num):
    response = requests.get(f'https://api.gbis.go.kr/ws/rest/busrouteservice/station?serviceKey=1234567890&routeId={num}')#165000012
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    bus=list()
    all = soup.select('busRouteStationList')
    for one in all:
        onebus = dict()
        onebus['이름'] = one.select('stationName')[0].get_text()
        onebus['지역'] = one.select('regionName')[0].get_text()
        onebus['id'] = one.select('stationId')[0].get_text()
        bus.append(onebus)
    return bus
