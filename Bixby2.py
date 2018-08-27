import discord
import asyncio
import time
import youtube_dl
import os
from discord.ext.commands import Bot
from discord.ext import commands
from discord.voice_client import VoiceClient

client = discord.Client() #Initialise Client 
client = commands.Bot(command_prefix = "!") #Initialise client bot

players = {}

@client.event 
async def on_ready():
    print("Bixby werkt!")

async def on_message(message):
    if message.content.startswith('!cookie'):
        msg = 'Lekker een sappig koekje'.format(message)
        await client.send_message(message.channel, ":cookie:")
        
    if message.content == "BOK.":
        await client.send_message(message.channel, ":goat:") 

    if message.content == "Bixby":
        await client.send_message(message.channel, "BIXBY!") 

    if message.content == "BIXBY":
        await client.send_message(message.channel, "BIXBY FTW!")

    if message.content == "Fuck off":
        await client.send_message(message.channel, "Zuig een piemel!")

    if message.content == "Homo":
        await client.send_message(message.channel, "Kijk naar jezelf!")
        
    if message.content == "Ga weg":
        await client.send_message(message.channel, "Niet lief!")

    if message.content == "Zuig een piemel":
        await client.send_message(message.channel, "Nee gadver!")

    if message.content == "Zuig een lul":
        await client.send_message(message.channel, "Ga dat lekker zelf doen viezerik!")

    if message.content.startswith('!Hi'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> Hi!" % (userID))
        

client.run(os.getenv('TOKEN'))
