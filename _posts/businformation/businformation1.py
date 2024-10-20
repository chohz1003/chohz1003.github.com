import requests
from bs4 import BeautifulSoup

def bus(num):
    response = requests.get(f'https://api.gbis.go.kr/ws/rest/busrouteservice/page?serviceKey=1234567890&pageSize=20&pageNo=1&keyword={num}')#8
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    bus=list()
    all = soup.select('routeList > busRouteList')
    for one in all:
        onebus = dict()
        onebus['지역']= one.select('regionName')[0].get_text()
        onebus['끝'] = one.select('edStaNm')[0].get_text()
        onebus['시작'] = one.select('stStaNm')[0].get_text()
        onebus['종류'] = one.select('routeTypeName')[0].get_text()
        onebus['id'] = one.select('routeId')[0].get_text()
        bus.append(onebus)
    return bus
