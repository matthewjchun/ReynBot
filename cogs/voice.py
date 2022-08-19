import asyncio

from discord import FFmpegPCMAudio
from discord.ext import commands


class VoiceCog(commands.Cog):
    def __int__(self, bot):
        self.bot = bot

    @commands.command(name='quote', pass_context=True)
    async def quote(self, ctx):
        if ctx.author.voice:
            channel = ctx.message.author.voice.channel
            await channel.connect()
        else:
            await ctx.send("Man, wha' a buncha jokas!")

    @commands.command(name='jokas', pass_context=True)
    async def jokas(self, ctx):
        if ctx.author.voice:
            channel = ctx.message.author.voice.channel
            clip = await channel.connect()
            source = FFmpegPCMAudio('JOHKAS.mp3')
            clip.play(source)
        else:
            await ctx.send("Man, wha' a buncha jokas!")

    @commands.command(name='leave', pass_context=True)
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


async def setup(bot):
    await bot.add_cog(VoiceCog(bot))
