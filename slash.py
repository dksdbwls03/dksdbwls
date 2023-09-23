import random
from typing import Any
import discord
from discord import app_commands 
import asyncio
import aiohttp
import datetime
from discord.flags import Intents
import openpyxl
import json
import requests
from discord import app_commands, Interaction, Object
from discord.ext import commands
from discord.ui import Button, View
from discord import ButtonStyle
import os

now = datetime.datetime.now()
time = f"{str(now.year)}년 {str(now.month)}월 {str(now.day)}일 {str(now.hour)}시 {str(now.minute)}분 {str(now.second)}초"


class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents = discord.Intents.default())
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced: 
            await tree.sync() 
            self.synced = True
        print(f'{self.user}이 시작되었습니다')  #  봇이 시작하였을때 터미널에 뜨는 말
        game = discord.Game('안유진 봇')          # ~~ 하는중
        await self.change_presence(status=discord.Status.online)#, activity=game)

client = aclient()
tree = app_commands.CommandTree(client)


@tree.command(name= '공지', description= '봇을 통해 공지를 할 수 있습니다.')
async def slash2(interaction: discord.Interaction, 공지내용: str):
    if interaction.user.guild_permissions.administrator:
        embed = discord.Embed(title=f"📢 {interaction.guild.name}에서 알립니다.", description=f"**모든 문의 사항은 {interaction.user.mention}에게 주세요.**", color=0x6ccad0)
        embed.add_field(name="공지 내용", value="{}".format(공지내용), inline=False)
        embed.set_footer(text=f"- 담당 관리자 : {interaction.user.mention}ㅣ{time}")
    
        await interaction.response.send_message(embed=embed)
    else:
        embed=discord.Embed(title="사용 불가", description=f"{interaction.user.mention}님은 관리자 권한이 없기 때문에 사용이 불가합니다.", color=discord.Color.red())
        embed.set_footer(text=f"{time}")
        await interaction.response.send_message(embed=embed)
        

@tree.command(name= "동전던지기", description="동전을 던져 앞/뒤를 정합니다.")
async def slash2(interaction: discord.Interaction):
    ran = random.randint(0,1)
    if ran == 0:
        d = "앞"
    if ran == 1:
        d = "뒤"
    await interaction.response.send_message(d)



@tree.command(name= "룰렛", description="룰렛을 돌립니다.")
async def slash2(interaction: discord.Interaction):
    ran = random.randint(0,9)
    if ran == 0:
        d = 1
    if ran == 1:
        d = 2
    if ran == 2:
        d = 3
    if ran == 3:
        d = 4
    if ran == 4:
        d = 5
    if ran == 5:
        d = 6
    if ran == 6:
        d = 7
    if ran == 7:
        d = 8
    if ran == 8:
        d = 9
    if ran == 9:
        d = 10
    await interaction.response.send_message(d)

#@tree.command(name = '랜사',description='랜덤사진')
#async def slash2(interaction: discord.Interaction):

        #ran = random.randint(0,2)
        #if ran == 0:
            #d = await interaction.response.send_message(file=discord.File("IMG_2361.jpg"))
        #if ran == 1:
            #d = await interaction.response.send_message(file=discord.File("IMG_1354.JPG"))
        #if ran == 2:
            #d = await interaction.response.send_message(file=discord.File("i14897905258.jpg"))
        #await interaction.response.send_message(d)



@tree.command(name = '문의', description = '봇을 통해 문의를 할 수 있습니다')  # 문의 명령어
async def slash2(interaction: discord.Interaction, 문의내용: str):  # 옵션

    
    embed = discord.Embed(title="📑 봇 문의 📑", description="ㅤ", color=0x4000FF)  # 문의 보낸 후 결과 임베드
    embed.add_field(name="봇 문의가 접수되었습니다", value="ㅤ", inline=False)
    embed.add_field(name="문의 내용", value="{}".format(문의내용), inline=False)  # 문의 내용
    embed.add_field(name="ㅤ", value="**▣ 문의 내용에 대한 답장은 관리자가 확인 후\n24시간 내에 답장이 오니 기다려 주시면 감사하겠습니다**", inline=False) 
    embed.add_field(name="ㅤ", value=f"- **{interaction.user.mention}** -", inline=False)  # 관리자 이름
    embed.set_footer(text=f"{time}에 접수 완료.")

    await interaction.response.send_message(embed=embed)
    
    


    #users = await client.fetch_user[874097871937495092, 706491922356895854, 717322952470954046, 1068757861829722203]
    users = await client.fetch_user("874097871937495092")   # 문의 온 문의 내용을 DM으로 받을 사람의 ID
    #Fucks = await client.fetch_user("706491922356895854")
    #admin = await client.fetch_user("844755262874845184")
    await users.send(f"{interaction.user.mention}에게 문의가 왔습니다.")
    await users.send("유저 아이디 : {}  / 문의 내용 : {}".format(interaction.user.id, 문의내용)) # 그 사람에게 올 유저 ID와 문의 내용
    #await Fucks.send(f"{interaction.user.mention}에게 문의가 왔습니다.")
    #await Fucks.send("유저 아이디 : {}  / 문의 내용 : {}".format(interaction.user.id, 문의내용))
    #await admin.send(f"{interaction.user.mention}에게 문의가 왔습니다.")
    #await admin.send("유저 아이디 : {}  / 문의 내용 : {}".format(interaction.user.id, 문의내용))




@tree.command(name = '문의답변', description = '봇을 통해 문의에 답변을 할 수 있습니다') #답변하기
async def slash2(interaction: discord.Interaction, 아이디: str, 답변: str):   # 옵션
    if interaction.user.guild_permissions.administrator:
        embed = discord.Embed(title="📑 봇 답변 📑", description="ㅤ", color=0x4000FF)   # 답변 임베드
        embed.add_field(name="문의에 대한 답변 내용", value="{}".format(답변) , inline=False)   


        #embed=discord.Embed(title="답변 완료.", description=f"{time}에 답변이 완료 되었습니다.", color=discord.Color.green())
        await interaction.response.send_message(f"{time}에 답변이 완료 되었습니다.")
        #await interaction.response.send_message(f"✅")  # 보내졌을시 나오는 확인 이모티콘
        user = await client.fetch_user("{}".format(아이디))
        await user.send(embed=embed)
    else:
        embed=discord.Embed(title="사용 불가", description=f"{interaction.user.mention}님은 관리자 권한이 없기 때문에 사용이 불가합니다.", color=discord.Color.red())
        embed.set_footer(text=f"{time}")
        await interaction.response.send_message(embed=embed)


access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
