import discord
from discord.ext import commands
import random

from discord.ext.commands.core import command


class RPG(commands.Cog):
    def __init__(self, client):
        self.client = client

    ##### Commands #####

    # Rolls a dice in NdN format
    @commands.command()
    async def roll(self, ctx, die: str):
        try:
            rolls, limit = map(int, die.split("d"))
            total = 0
        except Exception:
            await ctx.send("Formato tem que ser NdN!")
            return

        dice = []
        result = ""
        for i in range(rolls):
            dice.append(str(random.randint(1, limit)))
            total += int(dice[i])

        result = ", ".join(dice)
        embed = discord.Embed(
            title=f"Rolando {die}",
            description=f"Os resultados são {result} e o total é **{str(total)}**",
            color=discord.Colour.blue(),
        )
        await ctx.send(embed=embed)

    # Alchemist — Experimental Elixir
    @commands.command()
    async def elixir(self, ctx):
        elixir = [
            "**Healing.** The drinker regains a number of hit points equal to 2d4 + your Intelligence Modifier",
            "**Swiftness.** The drinker's walking speed increases by 10 feet for 1 hour.",
            "**Resilience.** The drinker gains a +1 bonus to AC for 10 minutes.",
            "**Boldness.** The drinker can roll a d4 and add the number rolled to every attack roll and saving throw they make for the next minute.",
            "**Flight.** The drinker gains a flying speed of 10 feet for 10 minutes.",
            "**Transformation.** The drinker's body is transformed as if by the Alter Self spell. The drinker determines the transformation caused by the spell, the effects of which last for 10 minutes.",
        ]
        colors = [0xBE1D25, 0xF3E88C, 0x23BB5B, 0xD04A17, 0xBFD3D3, 0x6533BC]
        result = random.randint(0, 5)
        embed = discord.Embed(
            title="Elixir Experimental",
            description=elixir[result],
            color=colors[result],
        )
        await ctx.send(embed=embed)

    # Heads or Tails
    @commands.command()
    async def coinflip(self, ctx):

        coin = ["Cara", "Coroa"]
        result = random.choice(coin)
        embed = discord.Embed(
            title="Cara ou Coroa?",
            description=f"{result}!",
            color=0xFFD700,
        )
        await ctx.send(embed=embed)

    @commands.group(invoke_without_command=True)
    async def crowley(self, ctx):
        pass

    # Crowley - Death Curse
    @crowley.command()
    async def death(self, ctx):
        death_curse = [
            "-6 do maior atributo",
            "-1d6 do maior atributo",
            "-1d6 do maior atributo",
            "-1d6 do maior atributo",
            "-1d6 do maior atributo",
            "-1d6 do maior atributo",
            "**Fobia.** Toda criatura que o personagem enfrentar, ele terá que girar um saving throw de inteligência com desvantagem. Se ele falhar, a criatura será muito mais assustadora do que realmente é, causando desvantagens em todas as rolagens do personagem durante esse combate.",
            "**Fobia.** Toda criatura que o personagem enfrentar, ele terá que girar um saving throw de inteligência com desvantagem. Se ele falhar, a criatura será muito mais assustadora do que realmente é, causando desvantagens em todas as rolagens do personagem durante esse combate.",
            "**Fobia.** Toda criatura que o personagem enfrentar, ele terá que girar um saving throw de inteligência com desvantagem. Se ele falhar, a criatura será muito mais assustadora do que realmente é, causando desvantagens em todas as rolagens do personagem durante esse combate.",
            "**Alvo.** O personagem sempre será o primeiro a ser atacado e o inimigo que atacar primeiro terá vantagem em todos os ataques subsequentes.",
            "**Alvo.** O personagem sempre será o primeiro a ser atacado e o inimigo que atacar primeiro terá vantagem em todos os ataques subsequentes.",
            "**Parasitas no corpo.** Quaisquer pontos de vida recuperados ao gastar um dado de vida são cortados pela metade.",
            "**Dor nas juntas.** O personagem terá desvantagem em rolagens de destreza.",
            "**Na companhia da peste.** Ratos, corvos, doenças e insetos te acompanham. O modificador de carisma se transforma em negativo em qualquer teste que não seja de conjuração, porém ele duplica em testes de intimidação.",
            "**Alucinações.** O personagem tem alucinações, levando a desvantagem e testes de percepção.",
            "**Alucinações.** O personagem tem alucinações, levando a desvantagem e testes de percepção.",
            "**Paranóico.** Ninguém é confiável, o personagem não usará magias que beneficiam outros personagens além de si mesmo.",
            "**Paranóico.** Ninguém é confiável, o personagem não usará magias que beneficiam outros personagens além de si mesmo.",
            "**Paranóico.** Ninguém é confiável, o personagem não usará magias que beneficiam outros personagens além de si mesmo.",
            "Nada acontece.",
        ]

        result = random.randint(0, 19)
        embed = discord.Embed(
            title="Crowley — Maldição de Ressureição",
            description=f"Voltar dos mortos é uma provação. O alvo sofre -4 de penalidade em todas as rolagens de Ataque, Testes de Resistência e Testes de Habilidade. Cada vez que o alvo termina um descanso longo, a penalidade é reduzida em 1 até que desapareça.\n\n{death_curse[result]}",
            color=0x000000,
        )
        await ctx.send(embed=embed)

    # Crowley - Daily Curse
    @crowley.command()
    async def daily(self, ctx):
        daily_curse = [
            "-6 do maior atributo",
            "-1d6 do maior atributo",
            "**Fobia.** Toda criatura que o personagem enfrentar, ele terá que girar um saving throw de inteligência com desvantagem. Se ele falhar, a criatura será muito mais assustadora do que realmente é, causando desvantagens em todas as rolagens do personagem durante esse combate.",
            "**Alvo.** O personagem sempre será o primeiro a ser atacado e o inimigo que atacar primeiro terá vantagem em todos os ataques subsequentes.",
            "**Parasitas no corpo.** Quaisquer pontos de vida recuperados ao gastar um dado de vida são cortados pela metade.",
            "**Dor nas juntas.** o personagem terá desvantagem em rolagens de destreza.",
            "**Na companhia da peste.** Ratos, corvos, doenças e insetos te acompanham. O modificador de carisma se transforma em negativo em qualquer teste que não seja de conjuração, porém ele duplica em testes de intimidação.",
            "**Alucinações.** O personagem tem alucinações, levando a desvantagem e testes de percepção.",
            "**Paranóico.** Ninguém é confiável, o personagem não usará magias que beneficiam outros personagens além de si mesmo.",
            "Nada acontece.",
            "**Olhos do Vazio.** Os olhos ficam pretos, o personagem ganha visão noturna e vantagem em testes de percepção no escuro, e desvantagem em testes em lugares claros.",
            "**Impulsivo.** O personagem terá desvantagem se o inimigo atacar primeiro, porém terá vantagem caso realize o primeiro ataque.",
            "**Espirito Bruto.** a cada ataque corpo a corpo, o personagem perderá HP no valor da metade do dano, porém seus ataques darão o dobro de dano.",
            "AINDA N TEM. ROLE DNV.",
            "AINDA N TEM. ROLE DNV.",
            "AINDA N TEM. ROLE DNV.",
            "AINDA N TEM. ROLE DNV.",
            "+1d6 na próxima rolagem de ressurreição",
            "**Ж Marca da Maldição Ж.** O personagem fica incapaz de ser curado através de qualquer magia de cura, porém ele passa a se curar pela metade de todo dano que causar.",
            "Se o personagem morrer no período desse dia, ele renasce instantaneamente e sem maldições.",
        ]

        result = random.randint(0, 19)
        embed = discord.Embed(
            title="Crowley — Maldição Diária",
            description=daily_curse[result],
            color=0x000000,
        )
        await ctx.send(embed=embed)

    ##### Events #####


def setup(client):
    client.add_cog(RPG(client))