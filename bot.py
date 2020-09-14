
import os

import discord

TOKEN = "NzU0NDI3NTA0OTAyNTM3MjE2.X10lXQ.7w4ksKgtiaodJa2XRA9ctcXEj-k"

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to discord!')

@client.event
async def on_message(message):
    # make sure the bot does not talk to itself
    if message.author == client.user:
        return

    if message.content == '!dani': 
        print(f'triggered: {message}')
        await message.channel.send(file=discord.File('dani.jpg'))

    if message.content == '!dani2': 
        print(f'triggered: {message}')
        await message.channel.send(file=discord.File('cap.png'))

    if message.content == '!dani3': 
        print(f'triggered: {message}')
        await message.channel.send(file=discord.File('die 1.jpg'))

    if message.content == '!dani4': 
        print(f'triggered: {message}')
        await message.channel.send(file=discord.File('die 2.jpg'))

    if message.content == '!dani5': 
        print(f'triggered: {message}')
        await message.channel.send(file=discord.File('tenor.gif'))

    if message.content == '!dani6': 
        print(f'triggered: {message}')
        await message.channel.send(file=discord.File('image0.jpg'))

    if message.content == '!daniGN': 
        print(f'triggered: {message}')
        await message.channel.send("GOOD NIGHT THO")
        
        
        
    

client.run(TOKEN)
