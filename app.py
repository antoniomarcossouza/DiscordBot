# Import required dependencies
import discord
from discord.ext import commands
import os

# Environment Variables
from env import *

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix=PREFIX, intents=intents)


@client.event
async def on_ready():
    await client.change_presence(
        status=discord.Status.online,
        activity=discord.Activity(
            type=discord.ActivityType.listening, name="você ( ͡° ͜ʖ ͡°)"
        ),
    )
    print("Bot rodando!")
    print("————————————")


initial_extensions = []

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        initial_extensions.append(f"cogs.{filename[:-3]}")

if __name__ == "__main__":
    for extension in initial_extensions:
        client.load_extension(extension)

client.run(BOT_TOKEN)