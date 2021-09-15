import discord
from discord.ext import commands


class CogTemplate(commands.Cog):
    # Constructor
    def __init__(self, client):
        self.client = client

    ##### Commands #####

    ##### Events #####


def setup(client):
    client.add_cog(CogTemplate(client))