import discord
import asyncio


client = discord.Client()







@client.event

async def on_ready():

    print("실행중")

    print("...")

    print("클라이언트 이름 :", client.user.name)

    print("클라이언트 아이디 :", client.user.id)

    print("------------------------------------------------")

    await client.change_presence(game=discord.Game(name=' 명령어목록은 !명령어목록 ', type=1))





@client.event

async def on_message(message):

    if message.content.startswith('ㅎㅇ'):

        await client.send_message(message.channel, "안녕하세요")
        
    if message.content.startswith('인사'):

        await client.send_message(message.channel, "안녕하세요")
        
    if message.content.startswith('따까리인사해봐'):

        await client.send_message(message.channel, "싫어니가먼데")
        
    if message.content.startswith('따까리인사'):

        await client.send_message(message.channel, "싫어니가먼데")
        
    if message.content.startswith('!제작자'):

        await client.send_message(message.channel, "저를만든사람은위데하고위대하신메호님입니다")

    if message.content.startswith('!제작자유튜브'):

        await client.send_message(message.channel, "https://goo.gl/tVDhYA")
        
    if message.content.startswith('!명령어목록'):

        await client.send_message(message.channel, "1.ㅎㅇ  2.인사 3.따까리인사해봐 4.!제작자 5.!제작자유튜브 6.!명령어목록 7.(추후명령어는추가될수있습니다)")
       
client.run('')
