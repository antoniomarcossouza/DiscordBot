import discord
from discord.ext import commands
import youtube_dl
import asyncio


ytdl_format_options = {
    "format": "bestaudio/best",
    "outtmpl": "%(extractor)s-%(id)s-%(title)s.%(ext)s",
    "restrictfilenames": True,
    "noplaylist": True,
    "nocheckcertificate": True,
    "ignoreerrors": False,
    "logtostderr": False,
    "quiet": True,
    "no_warnings": True,
    "default_search": "auto",
    "source_address": "0.0.0.0",  # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {"options": "-vn"}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)


class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get("title")
        self.url = data.get("url")

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(
            None, lambda: ytdl.extract_info(url, download=not stream)
        )

        if "entries" in data:
            # Takes first item from a playlist
            data = data["entries"][0]

        filename = data["url"] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)


class Music(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Plays a file from the local filesystem
    @commands.command()
    async def playlocal(self, ctx, arg):
        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(f"./audio/{arg}"))
        ctx.voice_client.play(
            source, after=lambda e: print(f"Erro: {e}") if e else None
        )

        await ctx.send(f"Agora tocando `{arg}`!")

    # Streams music from a url
    @commands.command()
    async def play(self, ctx, url):
        player = await YTDLSource.from_url(url, loop=self.client.loop, stream=True)
        ctx.voice_client.play(
            player, after=lambda e: print(f"Erro: {e}") if e else None
        )

        await ctx.send(f"Agora tocando `{player.title}`!")

    # Changes volume
    @commands.command()
    async def volume(self, ctx, volume: int):
        if ctx.voice_client is None:
            return await ctx.send("N??o estou conectado ?? um canal de voz.")

        ctx.voice_client.source.volume = volume / 100
        await ctx.send(f"Volume alterado para {volume}%")

    # Bot stops playing and disconnects
    @commands.command()
    async def stop(self, ctx):
        await ctx.voice_client.disconnect()

    # Bot pauses the reproduction
    @commands.command()
    async def pause(self, ctx):
        await ctx.voice_client.pause()
        await ctx.channel.send("Reprodu????o pausada!")

    # Bot resumes the reproduction
    @commands.command()
    async def resume(self, ctx):
        await ctx.voice_client.resume()
        await ctx.channel.send("Reprodu????o resumida!")

    @playlocal.before_invoke
    @play.before_invoke
    async def ensure_voice(self, ctx):
        if ctx.voice_client is None:
            if ctx.author.voice:
                await ctx.author.voice.channel.connect()
            else:
                await ctx.send("Voc?? n??o est?? conectado ?? um canal de voz!")
                raise commands.CommandError(
                    "Autor n??o est?? conectado ?? um canal de voz."
                )
        elif ctx.voice_client.is_playing():
            ctx.voice_client.stop()


def setup(client):
    client.add_cog(Music(client))