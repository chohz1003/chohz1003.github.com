import discord
from googleapiclient.discovery import build
from discord.ext.commands import Bot
from discordbotclass import discordbotclass
import asyncio
from dislash import SlashClient, SelectMenu

DEVELOPER_KEY = 'AIzaSyCfhAenYnxIP5u8QCgNZOg81pn3MZZVJY4'
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
    if ctx.author.voice and ctx.author.voice.channel:
        channel = ctx.author.voice.channel
        await channel.connect()

@bot.command()
async def 나가(ctx):
    await bot.voice_clients[0].disconnect()

@bot.command()
async def 음악(ctx,m):
    a.youtubelink(m)
    d = a.bbut()
    option = d[1]
    cc = d[0]
    msg = await ctx.send(
        "음악을 선택하세요",
        components=[
            SelectMenu(
                custom_id="음악",
                placeholder="개수 제한 없음",
                max_values=len(cc),
                options=option
            )
        ]
    )
    inter = await msg.wait_for_dropdown()
    labels = [option.value for option in inter.select_menu.selected_options]
    k=a.addbbut(labels)
    await inter.reply(f"음악선택완료 {''.join('')}")
    a.addplist(k)
    y=0
    while 1:
        b=a.flist()
        y=y+1
        if len(b) == 0:
            break
        else:
            try:
                if ctx.author.voice and ctx.author.voice.channel:
                    channel = ctx.author.voice.channel
                    await channel.connect()
            except:
                pass
            url = b[0]
            c = a.ydll(url)
            URL = c[0]
            FFMPEG_OPTIONS = c[1]
            voice = bot.voice_clients[0]
            try:
                voice.play(discord.FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
            except:
                pass
            await asyncio.sleep(c[2] + 1)
            #k=a.flist()
            #if k[0]==b[0]:
            a.llist()
            await bot.voice_clients[0].disconnect()

@bot.command()
async def 리스트(ctx):
    b=a.plist()
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
async def 초기화(ctx):
    a.nplist()
    await ctx.send('초기화 완료')

#@bot.command()
#async def 스탑(ctx):
#    if not bot.voice_clients[0].is_paused():
#        bot.voice_clients[0].pause()

#@bot.command()
#async def 재생(ctx):
#    if bot.voice_clients[0].is_paused():
#        bot.voice_clients[0].resume()

# @bot.command()
# async def 스킵(ctx):
#     await bot.voice_clients[0].disconnect()
#     while 1:
#         b = a.llist()
#         if len(b) == 0:
#             break
#         else:
#             channel = ctx.author.voice.channel
#             await channel.connect()
#             url = b[0]
#             c = a.ydll(url)
#             URL = c[0]
#             FFMPEG_OPTIONS = c[1]
#             voice = bot.voice_clients[0]
#             voice.play(discord.FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
#             await asyncio.sleep(c[2] + 1)
#             a.llist()
#             await bot.voice_clients[0].disconnect()

@bot.command()
async def 삭제(ctx):
    d = a.pplist()
    option = d[1]
    cc = len(d[0])-1
    msg = await ctx.send(
        "음악을 선택하세요",
        components=[
            SelectMenu(
                custom_id="음악",
                placeholder="음악선택",
                max_values=cc,
                options=option
            )
        ]
    )
    inter = await msg.wait_for_dropdown()
    labels = [option.value for option in inter.select_menu.selected_options]
    k = a.adpplist(labels)
    await inter.reply(f"음악삭제완료{''.join('')}")
    a.nnplist(k)

bot.run('ODUwOTMxNzIxNzM0MDYyMTAw.YLw57A.oO_yIRdCigPxHPn4ZDy9ZmsPw28')

##멈췄을때 sleep시간
##중지중 음악시 처음부터재생
##스킵
