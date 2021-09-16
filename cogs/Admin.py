import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
import asyncio

from env import *


class Admin(commands.Cog):
    # Constructor
    def __init__(self, client):
        self.client = client

    ##### Commands #####

    # Kicks someone from the server
    @commands.command()
    @has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member):
        await member.kick()
        await ctx.send(f"{member.mention} foi expulso do servidor!")

    # Kick command error if user doesn't have permission or did not specify an user to kick
    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f"Você não tem permissão para expulsar alguém!")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(
                f"Por favor, especifique quem você quer expulsar! Se precisar de ajuda, use {PREFIX}help."
            )

    # Bans someone from the server
    @commands.command()
    @has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f"{member.mention} foi banido do servidor!")

    # Ban command error if user doesn't have permission or did not specify an user to ban
    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f"Você não tem permissão para banir alguém!")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(
                f"Por favor, especifique quem você quer banir! Se precisar de ajuda, use {PREFIX}help."
            )

    # Unbans someone from the server
    @commands.command()
    @has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split("#")

        for ban_entry in banned_users:
            user = ban_entry.user
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f"{user.mention} foi desbanido!")
                return

    # Converts a string like '1s' into 1, 's'
    class DurationConverter(commands.Converter):
        async def convert(self, ctx, arg):
            amount = arg[:-1]
            unit = arg[-1]

            if amount.isdigit() and unit in ["s", "m", "h"]:
                return (int(amount), unit)

            raise commands.BadArgument(message="Não é uma duração válida!")

    # Bans someone from the server temporarily
    @commands.command()
    @has_permissions(ban_members=True)
    async def tempban(
        self, ctx, member: commands.MemberConverter(), duration: DurationConverter
    ):
        multiplier = {"s": 1, "m": 60, "h": 3600}
        amount, unit = duration

        await ctx.guild.ban(member)
        await ctx.send(f"{member.mention} foi banido por {amount}{unit}!")
        await asyncio.sleep(amount * multiplier[unit])
        await ctx.guild.unban(member)
        await ctx.send(f"{member.mention} foi desbanido após {amount}{unit}!")

    # Tempban command error if user doesn't have permission, did not specify an user to ban or amount of time to be banned for
    @tempban.error
    async def tempban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f"Você não tem permissão para banir alguém!")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(
                f"Por favor, coloque todos os argumentos! Se precisar de ajuda, use {PREFIX}help."
            )

    # Bot sends User a PM
    @commands.command(aliases=["pm"])
    @has_permissions(administrator=True)
    # @has_permissions(administrator=True)
    async def private_message(self, ctx, user: discord.Member, *, message: str):
        message = message
        embed = discord.Embed(title=message)
        await user.send(embed=embed)

    ##### Events #####


def setup(client):
    client.add_cog(Admin(client))