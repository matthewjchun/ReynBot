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
        self.db = self.cluster["UserData"]
        self.collection = self.db["UserData"]
        self.clips = self.bot.get_clips()

    async def lvl(self, ctx):
        id_query = {"_id": ctx.author.id}
        if self.collection.count_documents(id_query) == 0:
            post = {"_id": ctx.author.id, "name": ctx.author.name, "score": 1}
            self.collection.insert_one(post)
        else:
            user = self.collection.find(id_query)
            for result in user:
                score = result["score"]
            score = score + 1
            self.collection.update_one({"_id": ctx.author.id}, {"$set": {"score": score}})
        print(f"user {ctx.author.name}'s score has been updated.")

    @commands.command(name='quote')
    @commands.after_invoke(lvl)
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
    @commands.after_invoke(lvl)
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
    @commands.after_invoke(lvl)
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
