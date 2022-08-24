import asyncio
import discord
import random
import os

from discord import FFmpegPCMAudio
from discord.ext import commands


class VoiceCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.cluster = self.bot.get_cluster()
        self.clips = self.bot.get_clips()

    @commands.command(name='quote')
    async def quote(self, ctx):
        if ctx.author.voice:
            channel = ctx.message.author.voice.channel
            connection = await channel.connect()
            clip = os.path.basename(random.choice(os.listdir("./clips")))
            source = FFmpegPCMAudio("./clips/" + clip)
            connection.play(source)
        else:
            await ctx.send("Man, wha' a buncha jokas! You've gotta be in a voice channel!")

    @commands.command(name='jokas')
    async def jokas(self, ctx):
        if ctx.author.voice:
            channel = ctx.message.author.voice.channel
            connection = await channel.connect()
            source = FFmpegPCMAudio('./clips/JOHKAS.mp3')
            connection.play(source)
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


def setup(bot):
    bot.add_cog(VoiceCog(bot))
