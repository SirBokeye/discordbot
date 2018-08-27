import discord
import asyncio
import time
import youtube_dl
import os
from discord.ext.commands import Bot
from discord.ext import commands
from discord.voice_client import VoiceClient

Client = discord.Client() #Initialise Client 
client = commands.Bot(command_prefix = "!") #Initialise client bot

players = {}

@client.event 
async def on_ready():
    print("Bixby werkt!")

async def on_message(message):
    if message.content.startswith('!cookie'):
	msg = 'Lekker een sappig koekje'.format(message)
        await client.send_message(message.channel, ":cookie:")

        
@client.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)

@client.command(pass_context=True)
async def leave(ctx):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    await voice_client.disconnect()
    
@client.command(pass_context=True)
async def play(ctx, url):
	server = ctx.message.server
	voice_client = client.voice_client_in(server)
	player = await voice_client.create_ytdl_player(url)
	players[server.id] = player
	player.start()

client.run(os.getenv('TOKEN'))
