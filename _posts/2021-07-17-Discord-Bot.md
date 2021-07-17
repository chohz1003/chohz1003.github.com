---
layout: post
title: "Discord Bot"
date: 2021-07-17 18:00:00
categories: jekyll update
permalink: /archivers/Discord Bot
---

# 디스코드봇 일지
파이썬으로 디스코드 음악 봇 만들기

## 0일차(1일차부터 기록 시작함)
1. 디스코드봇을 만들고 필요한 오픈소스들을 찾음.
2. 디스코드에서 **!음악 "검색어"** 를 통해 유튜브에 "검색어"를 쳤을때 나오는 영상의 주소를 얻어옴.
3. 영상의 주소를 통해 영상을 다운받음.
4. 다운받은 영상을 mp3로 바꿈.

### 오픈소스
```python
import youtube_dl #유튜브영상다운
import ffmpeg #영상을 mp3로 변환
from googleapiclient.discovery import build #유튜브 영상 주소 찾기
import discord #디스코드
from discord.ext.commands import Bot #디스코드
```

## 1일차
1. 영상의 주소를 얻어올때 조회수가 높은 순으로 5개만 얻어오게 바꿈.
2. 영상을 mp3로 바꿀때 이미 다운받았던 mp3가 있다면 기존의 mp3를 지우고 새로운 mp3를 다운받게 바꿈.

## 2일차
