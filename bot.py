import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv("token.env")
TOKEN = os.getenv('TOKEN')

class myClient(discord.Client):

    async def on_ready(self):
        print(f'We have logged in as {self.user}')
    
    async def on_message(self, message):
        print(f"{message.channel}: {message.author}: {message.content}")

        if message.author == client.user:
            return
        
        if message.content.startswith('!ping'):
            await message.channel.send('pong!')
        
    async def on_message_delete(self, message):
        print(f"Deleted message from {message.author}: {message.content}")
    
    async def on_message_edit(self, before, after):
        print(f"Edited message from {before.author}: {before.content} to {after.content}")

intents = discord.Intents.default()
intents.message_content = True



client = myClient(intents=intents)
client.run(TOKEN)


