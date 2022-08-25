import asyncio
import discord
import random
import os

from discord import FFmpegPCMAudio
from discord.ext import commands


def is_connected(ctx):
    voice_client = discord.utils.get(ctx.bot.voice_clients, guild=ctx.guild)
    return voice_client and voice_client.is_connected()


class VoiceCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.cluster = self.bot.get_cluster()
        self.clips = self.bot.get_clips()

    @commands.command(name='quote')
    async def quote(self, ctx, number_of_quotes: int = 1):
        if ctx.author.voice:
            if not is_connected(ctx):
                channel = ctx.message.author.voice.channel
                connection = await channel.connect()
            else:
                connection = discord.utils.get(ctx.bot.voice_clients, guild=ctx.guild)
            for _ in range(number_of_quotes):
                clip = os.path.basename(random.choice(os.listdir("./clips")))
                source = FFmpegPCMAudio("./clips/" + clip)
                connection.play(source)
                await asyncio.sleep(4)
        else:
            await ctx.send("Man, wha' a buncha jokas! You've gotta be in a voice channel!")

    @commands.command(name='jokas')
    async def jokas(self, ctx, number_of_quotes: int = 1):
        if ctx.author.voice:
            if not is_connected(ctx):
                channel = ctx.message.author.voice.channel
                connection = await channel.connect()
            else:
                connection = discord.utils.get(ctx.bot.voice_clients, guild=ctx.guild)
            for _ in range(number_of_quotes):
                source = FFmpegPCMAudio('./clips/JOHKAS.mp3')
                connection.play(source)
                await asyncio.sleep(3)
        else:
            await ctx.send("You've gotta be in a voice channel!")

    @commands.command(name='leave')
    async def leave(self, ctx):
        if ctx.voice_client:
            await ctx.guild.voice_client.disconnect()
            await ctx.send("Ugh... Let's split!")
        else:
            await ctx.send("Lets not lose our heads though!")

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if not member.id == self.bot.user.id:
            return

        elif before.channel is None:
            voice = after.channel.guild.voice_client
            time = 0
            while True:
                await asyncio.sleep(1)
                time = time + 1
                if voice.is_playing() and not voice.is_paused():
                    time = 0
                if time == 5:
                    await voice.disconnect()
                if not voice.is_connected():
                    break

    # potentially try to intentionally throw another more specific error for this case
    # intended throw case: when users try to send play another command while one is currently playing
    @quote.error
    @jokas.error
    async def quote_and_jokas_handler(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send('Ain\'t over yet!')


def setup(bot):
    bot.add_cog(VoiceCog(bot))
