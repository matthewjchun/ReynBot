import random
import discord

from discord.ext import commands


class TextCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db = self.bot.get_cluster()["UserData"]
        self.collection = self.db["UserData"]

    @commands.command(name='talk')
    @commands.guild_only()
    async def talk(self, ctx):
        reyn_quotes = [
            "Now it\'s Reyn time!",
            "Watch out! Mad hairball on the loose!",
            "I\'m powering up!",
            "The adults are talking here pops!",
            "Let\'s not lose our heads, though.",
            "Good thing I\'m here? No? Anyone?",
            "Cheers!",
            "Shulk? You saw another one didn\'t you?",
            "Who else wants some?",
            "Haha! In your face!",
            "It just goes to show, brawn is better than brains.",
            "Yeah! Reyn time!",
            "Yeaah, I\'m turnin\' up the heat!",
            "Give it some Oomph!",
            "Gotta focus on... GUARDING!",
            "Alley-oop!"
        ]
        response = random.choice(reyn_quotes)
        await ctx.send(response)

    @commands.command()
    async def reyn_time(self, ctx):
        await ctx.channel.send('imagine this is a picture')

    @commands.command()
    async def lvl(self, ctx):
        post = {"_id": ctx.author.id, "name": ctx.author.name, "score": 1}
        self.collection.insert_one(post)
        await ctx.channel.send('accepted!')


def setup(bot):
    bot.add_cog(TextCog(bot))
