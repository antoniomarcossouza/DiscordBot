import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions


class Admin(commands.Cog):
    # Constructor
    def __init__(self, client):
        self.client = client

    ##### Commands #####

    # Kicks someone from the server
    @commands.command()
    @has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f"{member} foi expulso do servidor!")

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("Você não tem permissão pra expulsar alguém!")

    # Ban someone from the server
    @commands.command()
    @has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f"{member} foi banido do servidor!")

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("Você não tem permissão pra banir alguém!")

    # Bot sends User a PM
    @commands.command(aliases=["pm"])
    # @has_permissions(administrator=True)
    async def private_message(self, ctx, user: discord.Member, *, message: str):
        message = message
        embed = discord.Embed(title=message)
        await user.send(embed=embed)

    ##### Events #####

    # Missing permissions Error
    # @commands.Cog.listener()
    # async def on_command_error(ctx, error):
    #     if isinstance(error, commands.MissingPermissions):
    #         await ctx.send("Você não tem permissão para usar esse comando!")


def setup(client):
    client.add_cog(Admin(client))