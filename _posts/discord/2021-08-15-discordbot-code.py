import discord
from googleapiclient.discovery import build
from discord.ext.commands import Bot
from discordbotclass import discordbotclass
import asyncio
from dislash import SlashClient, SelectMenu

DEVELOPER_KEY = 'key'
YOUTUBE_API_SERVICE_NAME="youtube"
YOUTUBE_API_VERSION="v3"
youtube = build(YOUTUBE_API_SERVICE_NAME,YOUTUBE_API_VERSION,developerKey=DEVELOPER_KEY)
a=discordbotclass()
intents=discord.Intents.default()
bot = Bot(command_prefix='!', intents=intents)
slash = SlashClient(bot)

@bot.event
async def on_ready():
    print(f'{bot.user} 에 로그인하였습니다!')

@bot.command()
async def ping(ctx):
    await ctx.send('pong!')

@bot.command()
async def hello(ctx):
    await ctx.reply('hello!')

@bot.command()
async def 들어와(ctx):
    if ctx.author.voice and ctx.author.voice.channel: #유저가 음성채널에 있는지 확인
        channel = ctx.author.voice.channel
        await channel.connect() #봇이 음성채널에 연결
        
@bot.command()
async def 나가(ctx):
    await bot.voice_clients[0].disconnect() #봇이 음성채널에 연결끊음

@bot.command()
async def 음악(ctx,m): #m= 검색어
    a.youtubelink(m) #링크와 제목을 클래스에 임시저장
    d = a.bbut() 
    option = d[1] #임시저장된 제목(최대25글자)
    cc = d[0] #임시저장된 제목(제한없음)
    msg = await ctx.send(                       #
        "음악을 선택하세요",
        components=[
            SelectMenu(
                custom_id="음악",
                placeholder="음악 선택",    #버튼생성
                max_values=len(cc),
                options=option
            )
        ]
    )                                           #
    inter = await msg.wait_for_dropdown()
    labels = [option.value for option in inter.select_menu.selected_options]
    k=a.addbbut(labels) #선택한 음악의 링크와 제목
    await inter.reply(f"음악선택완료 {''.join('')}")
    a.addplist(k) #k값을 클래스에 저장
    y=0
    while 1:
        b=a.flist() #저장된 음악 링크
        y=y+1
        if len(b) == 0: 
            break 
        else:
            try:
                if ctx.author.voice and ctx.author.voice.channel: #유저가 음성채널에 있는지 확인
                    channel = ctx.author.voice.channel
                    await channel.connect() #봇이 음성채널에 연결
            except:
                pass
            url = b[0] #저장된 음악 링크중 첫번째 링크
            c = a.ydll(url)
            URL = c[0] 
            FFMPEG_OPTIONS = c[1] 
            voice = bot.voice_clients[0] 
            try:
                voice.play(discord.FFmpegPCMAudio(URL, **FFMPEG_OPTIONS)) #봇이 음악 재생
            except:
                pass
            await asyncio.sleep(c[2] + 1) #음악 재생길이+1초 뒤에 다음코드가 작동함
            #k=a.flist()
            #if k[0]==b[0]:
            a.llist() 저장된 음악 링크와 제목중에서 첫번째 링크와 제목을 삭제
            await bot.voice_clients[0].disconnect() #봇이 음성채널에 연결끊음

@bot.command()
async def 리스트(ctx):
    b=a.plist() #저장된 음악 제목
    d=0
    if b==[]:
        await ctx.send('플레이리스트없음')
    else:
        for c in b:
            if d == 0:
                await ctx.send(c + '(듣는중)')
                d = d + 1
            else:
                await ctx.send(c)

@bot.command()
async def 초기화(ctx): #(듣고있는것 제외)
    a.nplist() #저장된 음악 링크와 제목중 첫번째 링크와 제목빼고 삭제
    await ctx.send('초기화 완료')

@bot.command()
async def 삭제(ctx):
    d = a.pplist()
    option = d[1] 저장된 제목
    cc = len(d[0])-1 #저장된 제목 개수-1 (듣고있는 음악 제외)

    msg = await ctx.send(                  #
        "음악을 선택하세요",
        components=[                       
            SelectMenu(
                custom_id="음악",
                placeholder="음악선택",     #버튼생성
                max_values=cc,
                options=option
            )
        ]
    )                                      #
    inter = await msg.wait_for_dropdown()
    labels = [option.value for option in inter.select_menu.selected_options]
    k = a.adpplist(labels) #선택한 음악의 링크와 제목
    await inter.reply(f"음악삭제완료{''.join('')}")
    a.nnplist(k) #k값 클래스에서 삭제

bot.run('토큰')
