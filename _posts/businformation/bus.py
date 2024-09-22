import requests
from bs4 import BeautifulSoup
response = requests.get('https://api.gbis.go.kr/ws/rest/busrouteservice/page?serviceKey=1234567890&pageSize=20&pageNo=1&keyword=8')
html = response.text
soup = BeautifulSoup(html, 'html.parser')

a = soup.select('routeList > busRouteList')
print(a[0].select('adminname'))

#print(soup.prettify())
