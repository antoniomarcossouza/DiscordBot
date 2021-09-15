import discord
from discord import channel
from discord.ext import commands

from env import *

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix=PREFIX, intents=intents)


@client.event
async def on_ready():
    print("Bot rodando!")
    print("————————————")


# Hello command
@client.command()
async def oi(ctx):
    await ctx.send("Opa, bão?")


# Welcome message when someone enters the server
@client.event
async def on_member_join(member):
    channel = client.get_channel(WELCOME_CHANNEL_ID)
    await channel.send(f"Seja bem vindo(a), {member.name}!")


# Goodbye message when someone leaves the server
@client.event
async def on_member_remove(member):
    channel = client.get_channel(WELCOME_CHANNEL_ID)
    await channel.send(f"{member.name} saiu do servidor! Tchau!")


# Command to join voice channel
@client.command(pass_context=True)
async def join(ctx):
    if ctx.author.voice:
        channel = ctx.message.author.voice.channel
        await channel.connect()
    else:
        await ctx.send("Você não está em um canal de voz!")


# Command to leave voice channel
@client.command(pass_context=True)
async def leave(ctx):
    if ctx.voice_client:
        await ctx.guild.voice_client.disconnect()
        await ctx.send("Tchau!")
    else:
        await ctx.send("Eu não estou em um canal de voz!")


client.run(BOT_TOKEN)