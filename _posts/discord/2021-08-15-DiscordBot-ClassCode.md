---
layout: post
title:  "Discord Bot Class Code"
date:   2021-08-15 16:00:00
categories: jekyll update
permalink: /archivers/DiscordBotClassCode
---
```python
import youtube_dl
import json
from googleapiclient.discovery import build
from dislash import SelectOption

class discordbotclass:
    playlist=[]
    addplaylist=[]
    titlelist=[]
    addtitlelist=[]

    def youtubelink(self,m):
        DEVELOPER_KEY = 'AIzaSyCfhAenYnxIP5u8QCgNZOg81pn3MZZVJY4'
        YOUTUBE_API_SERVICE_NAME = "youtube"
        YOUTUBE_API_VERSION = "v3"
        youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
        search_response = youtube.search().list(
            q=m,
            order="viewCount",
            part="snippet",
            maxResults=5
        ).execute()
        json1 = json.loads(json.dumps(search_response))
        json2 = json1.get("items")
        self.addplaylist = []
        self.addtitlelist = []
        for a in json2:
            b = a.get('id')
            if b.get('videoId') == None:
                pass
            else:
                self.addplaylist.append('https://www.youtube.com/watch?v='+b.get('videoId'))
        for a in json2:
            b = a.get('snippet')
            if b.get('title') == None:
                pass
            else:
                self.addtitlelist.append(b.get('title').replace('&#39;',"'"))
        return None

    def addplist(self, m):
        b=m.split(',')
        b=list(map(int, b))
        for d in b:
            self.playlist.append(self.addplaylist[d])
        self.addplaylist=[]
        for d in b:
            self.titlelist.append(self.addtitlelist[d])
        self.addtitlelist = []
        return None

    def plist(self):
        return self.titlelist

    def flist(self):
        return self.playlist

    def nplist(self):
        del self.playlist[1:]
        del self.titlelist[1:]
        return None

    def ydll(self,url):
        ydl_opts = {'format': 'bestaudio'}
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
                            'options': '-vn'}
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            URL = info['formats'][0]['url']
            t=info['duration']
        return URL,FFMPEG_OPTIONS,t

    def llist(self):
        del self.titlelist[0]
        del self.playlist[0]
        return self.playlist

    def nnplist(self,m):
        b = m.split(',')
        b = list(map(int, b))
        b.reverse()
        for d in b:
            del self.titlelist[d]
        for d in b:
            del self.playlist[d]
        return None

    def bbut(self):
        c=[]
        d=0
        a = self.addtitlelist
        for b in a:
            d=d+1
            c.append(SelectOption("%s" % b[:25], "%s" % b+str(d)))
        return a,c

    def addbbut(self,m):
        c=''
        d=0
        f=0
        if len(m)==1:
            for a in self.addtitlelist:
                f=f+1
                for b in m:
                    if b[:-1] == a:
                        c=c+str(d)+','
                        d=d+1
                        break
                if f == d:
                    pass
                else:
                    d = d + 1
                if c=='':
                    pass
                else:
                    break
        else:
            for a in self.addtitlelist:
                f=f+1
                for b in m:
                    if b[:-1] == a:
                        c=c+str(d)+','
                        d=d+1
                        break
                if f == d:
                    pass
                else:
                    d = d + 1
        c=c[:-1]
        return c

    def pplist(self):
        c = []
        d = 0
        a = self.titlelist[1:]
        for b in a:
            d = d + 1
            c.append(SelectOption("%s" % b[:25], "%s" % b + str(d)))
        return a, c

    def adpplist(self,m):
        c = ''
        d = 0
        f = 0
        for a in self.titlelist:
            f = f + 1
            for b in m:
                if b[:-1] == a:
                    c = c + str(d) + ','
                    d = d + 1
                    break
            if f == d:
                pass
            else:
                d = d + 1
        c=c[:-1]
        return c
```
