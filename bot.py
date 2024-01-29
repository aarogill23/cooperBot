import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import random

load_dotenv("token.env")
TOKEN = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.message_content = True

class myBot (commands.Bot):
    async def get_context(self, message):
        return await super().get_context(message)

bot = myBot(command_prefix = '!', intents=intents)

@bot.command()
async def ping(ctx):
    await ctx.send('pong!')

@bot.command()
async def randNum(ctx, number: int):
    value = random.randint(1, number)
    await ctx.send(f"Your random number is {value}")

bot.run(TOKEN)


