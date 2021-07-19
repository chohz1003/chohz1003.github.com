---
layout: post
title: "Discord Bot"
date: 2021-07-17 18:00:00
categories: jekyll update
permalink: /archivers/Discord Bot
---

# 디스코드봇 일지
파이썬으로 디스코드 음악 봇 만들기.

## 0일차(1일차부터 기록 시작함)
1. 디스코드봇을 만들고 필요한 오픈소스들을 다운받음.
2. 디스코드에서 **!음악 "검색어"** 를 통해 유튜브에 "검색어"를 쳤을때 나오는 영상의 주소를 얻어오는 코드를 작성함.
3. 영상의 주소를 통해 해당 주소의영상을 다운받는 코드를 작성함.
4. 영상을 mp3로 바꾸는 코드를 작성함.

### pip 모듈
```python
pip install PyNaCl #음성기능
pip install -U discord #디스코드
pip install ffmpeg #영상을 mp3로 변환
pip install google-api-python-client #유튜브 api
pip install youtube-dl #유튜브영상 다운
```

## 1일차
1. 영상의 주소를 얻어올때 조회수가 높은 순으로 5개만 얻어오게 코드를 수정함.
2. 영상을 mp3로 바꿀때 이미 다운받았던 mp3가 있다면 기존의 mp3를 지우고 새로운 mp3를 다운받게 코드를 수정함.

## 2일차
1. client방법의 어려움을 느낌.
2. client방법에서 ext방법으로 바꾸기로함.

## 3일차
1. client방법에서 ext방법으로 바꿈.
2. 음성채널에 봇을 입장,퇴장 시키는 코드를 작성함.
3. 디스코드기능class를 만들어야할것같음.

## 4일차
