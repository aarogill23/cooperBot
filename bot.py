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

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")

@bot.event
async def on_message(message):
    print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")
    await bot.process_commands(message)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Command not found use !help for a list of commands")

@bot.event
async def on_message_delete(message):
    print(f"In {message.channel}: {message.author}: deleted a message that said {message.content}")

@bot.event
async def on_message_edit(before, after):
    print(f"In {before.channel}: {before.author}: edited a message from {before.content} to {after.content}")

@bot.event
async def on_user_join(ctx, member):
    await ctx.send(f"Welcome {member.name} to the server!")
    print(f"{member.name} joined the server")

bot.run(TOKEN)


