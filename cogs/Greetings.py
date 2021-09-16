import discord
from discord.ext import commands

from env import *


class Greetings(commands.Cog):
    # Constructor
    def __init__(self, client):
        self.client = client

    ##### Commands #####

    # Hello command
    @commands.command(aliases=["hi", "oi"])
    async def hello(self, ctx):
        await ctx.send("Opa, bão?")

    ##### Events #####

    # Welcome message when someone enters the server
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.client.get_channel(WELCOME_CHANNEL_ID)
        await channel.send(f"Seja bem vindo(a), {member.mention}!")

    # Goodbye message when someone leaves the server
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.client.get_channel(WELCOME_CHANNEL_ID)
        try:
            await member.guild.fetch_ban(member)
            await channel.send(f"{member.mention} foi banido do servidor! Adeus!")
            return
        except discord.NotFound:
            await channel.send(f"{member.mention} saiu do servidor! Tchau!")


def setup(client):
    client.add_cog(Greetings(client))