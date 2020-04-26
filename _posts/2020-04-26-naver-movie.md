---
layout: post
title:  "naver movie"
date:   2020-04-25 13:00:00
categories: jekyll update
permalink: /archivers/hello
---


### 네이버 영화 순위 및 댓글을 크롤링 하는 방법을 알아보고,  그전에 해야하는 일을 알아봅시다.

 

   1. 오픈소스 다운
	       - **request**
	       - **bs4(BeautifulSoup)**
  2. 파이썬 설치
	      - **파이참**

 

# 오픈소스

##  request
```python
import requests
from bs4 import BeautifulSoup
response = requests.get(url)
#url에 있는 정보 가져오기
html = response.text  
#가져온 정보를 text 형식으로 저장
soup = BeautifulSoup(html, 'html.parser')
#저장한 정보를 hrml 형식으로 변환
```
**request** 라는 오픈소스를  **import** 하면 **requests.get**을 사용하여 정보를 가져올수있습니다. 

## bs4(BeautifulSoup)

```python
import requests
from bs4 import BeautifulSoup
response = requests.get(url)
#url에 있는 정보 가져오기
html = response.text  
#text 형식으로 저장
soup = BeautifulSoup(html, 'html.parser')
#html 형식으로 변환
```
**BeautifulSoup** 는 **html** 코드를 Python 문법으로 변환시켜줍니다.

# 파이썬
버전에 맞는 **파이썬**,**파이참** 설치 


# 네이버 영화순위 및 댓글 크롤링
## 전체 코드
```python
import requests  
from bs4 import BeautifulSoup  
response = requests.get('[https://movie.naver.com/movie/sdb/rank/rmovie.nhn](https://movie.naver.com/movie/sdb/rank/rmovie.nhn)')  
#url에 있는 정보 가져오기
html = response.text  
#text 형식으로 저장
soup = BeautifulSoup(html, 'html.parser')  
#html 형식으로 변환
ranking = 1
#순위 1
for tag in soup.select('div[class=tit3] a' ):
	url = tag.get('href')  
	print("\n" + str(ranking) + '위 : ' + tag.text.strip())  
	ranking = ranking + 1  
	a= requests.get('[https://movie.naver.com](https://movie.naver.com/)'+url)  
	b = a.text  
	c=BeautifulSoup(b, 'html.parser')  
	for d in c.select('div[class=score_result] li'):
		v= d.select('div[class=score_reple] p')[0]  
		print(v.text.strip())  
		for b in d.select('div[class=btn_area] a'):
			print(b.text.strip())
```

## 네이버 영화 사이트 정보 가져오기

```python
import requests  
from bs4 import BeautifulSoup  
response = requests.get('[https://movie.naver.com/movie/sdb/rank/rmovie.nhn](https://movie.naver.com/movie/sdb/rank/rmovie.nhn)')  
#url에 있는 정보 가져오기
html = response.text  
#text 형식으로 저장
soup = BeautifulSoup(html, 'html.parser')  
#html 형식으로 변환
ranking = 1
#순위 1
```



## 영화 순위 
```python
for tag in soup.select('div[class=tit3] a' ):
	#<div class="tit3">태그로된 정보를 가져옴
	url = tag.get('href')  
	#href 로 시작하는 정보를 가져옴
	print("\n" + str(ranking) + '위 : ' + tag.text.strip())  
	#영화 제목,순위
	ranking = ranking + 1  
	#순위를 1씩 더함
	a= requests.get('[https://movie.naver.com](https://movie.naver.com/)'+url)  
	#다음 순위의 영화 사이트로 넘어감
	b = a.text  
	#
	c=BeautifulSoup(b, 'html.parser')  
```
네이버 영화 소스를 보면 영화제목은  **<**div class="tit3"**>** 태그가 감싸져 있습니다. 
