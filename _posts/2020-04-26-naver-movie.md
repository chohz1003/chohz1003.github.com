---
layout: post
title:  "naver movie"
date:   2020-04-25 13:00:00
categories: jekyll update
permalink: /archivers/movie
---


# 오픈소스

```python
import requests
from bs4 import BeautifulSoup
```

**request**,**BeautifulSoup**를  ``import`` 합니다.
**BeautifulSoup**는 문서가  ``html``이라고  알려주고
**request**는 웹사이트의 정보를 가져옵니다.
# 네이버 영화 크롤링
```python
response = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn')
```
**response**는 네이버  영화 랭킹 페이지의 정보입니다.
```python
html = response.text  
soup = BeautifulSoup(html, 'html.parser') 
```
**html**은 가져온 정보중 ``text``정보를 저장한것이고
**soup**는 **html**이 ``html``코드라고 알주는것입니다.

```python
for tag in soup.select('div[class=tit3] a' ):  
	url = tag.get('href')
```
**tag**는 ``soup`` 안에있는 정보중에서 ``div``태그의 ``class="tit3"`` 속성으로된 값중 ``a``로시작하는 속성의 값이고
**url**은 **tag**에서 ``href``속성 값입니다.
![https://chohz1003.github.io/](https://chohz1003.github.io/image/naver-movie.png)

```python
print("\n" + str(ranking) + '위 : ' + tag.text.strip())
```
영화 순위와 영화 이름이 ``print`` 됩니다.

```python
ranking = ranking + 1
```
랭킹을 ``1``씩 더합니다.

```python
a= requests.get('(https://movie.naver.com/)'+url)
b = a.text
```
**a**는 가져온 영화  페이지로 넘어가고
**b**는 **a**의 ``text``정보입니다.
```python
c=BeautifulSoup(b, 'html.parser')
```
**c**는**b**가 ``html``코드라고 알려줍니다.


```python
for d in c.select('div[class=score_result] li'):  
	v= d.select('div[class=score_reple] p')[0]
```
**d**는 **c**안에있는 정보중에서 ``div``태그의 ``class="score_result"`` 속성 값중 ``li``로시작하는 속성의 값이고
**v**는 **d**에서 ``div``태그의 ``class="score_reple"`` 속성 값중 ``p``로 시작하는 속성의 값입니다.
![https://chohz1003.github.io/](https://chohz1003.github.io/image/naver-movie1.png)
```python
print(v.text.strip())
```
영화의 댓글이 ``print`` 됩니다.

```python
for e in d.select('div[class=btn_area] a'):  
```
**e**는 **d**안에있는 정보중에서 ``div``태그의 ``class="class=btn_area"`` 속성 값중 ``a``로시작하는 속성의 값입니다.
![https://chohz1003.github.io/](https://chohz1003.github.io/image/naver-movie2.png)
```python
print(e.text.strip())
```
공감수와 비공감수가 `` print``됩니다.

# 전체 코드
```python
import requests  
from bs4 import BeautifulSoup  
response = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn')  
html = response.text  
soup = BeautifulSoup(html, 'html.parser')  
ranking = 1  
for tag in soup.select('div[class=tit3] a' ):  
	url = tag.get('href')  
	print("\n" + str(ranking) + '위 : ' + tag.text.strip())  
	ranking = ranking + 1  
	a= requests.get('https://movie.naver.com/'+url)  
	b = a.text  
	c=BeautifulSoup(b, 'html.parser')  
		for d in c.select('div[class=score_result] li'):  
		v= d.select('div[class=score_reple] p')[0]  
		print(v.text.strip())  
		for e in d.select('div[class=btn_area] a'):  
			print(e.text.strip())
```
