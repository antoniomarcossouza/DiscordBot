import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions

from env import *


class General(commands.Cog):
    # Constructor
    def __init__(self, client):
        self.client = client

    ##### Commands #####
    @commands.command()
    @has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int):
        await ctx.channel.purge(limit=amount + 1)a
        await ctx.channel.send(f"{amount} mensagens apagadas!")

    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f"Você não tem permissão para deletar mensagens!")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(
                f"Por favor, especifique o número de mensagens a serem deletadas! Se precisar de ajuda, use {PREFIX}help."
            )

    ##### Events #####


def setup(client):
    client.add_cog(General(client))