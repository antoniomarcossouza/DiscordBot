import discord
from discord.ext import commands


class CustomHelpCommand(commands.HelpCommand):
    def __init__(self):
        super().__init__()

    async def send_bot_help(self, mapping):
        for cog in mapping:
            await self.get_destination().send(
                f"{cog.qualified_name}:{[command.name for command in mapping[cog]]}"
            )

    async def send_cog_help(self, cog):
        await self.get_destination().send(
            f"{cog.qualified_name}:{[command.name for command in cog.get_commands()]}"
        )

    async def send_group_help(self, group):
        await self.get_destination().send(
            f"{group.name}:{[command.name for index, command in enumerate(group.commands)]}"
        )

    async def send_command_help(self, command):
        await self.get_destination().send(command.name)


class Help(commands.Cog):
    # Constructor
    def __init__(self, client):
        self._original_help_command = client.help_command
        self.client = client
        client.help_command = CustomHelpCommand()
        client.help_command.cog = self

    ##### Commands #####

    ##### Events #####


def setup(client):
    client.add_cog(Help(client))