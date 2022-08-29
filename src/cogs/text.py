import json
import random
import discord

from discord.ext import commands


class TextCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db = self.bot.get_cluster()["UserData"]
        self.collection = self.db["UserData"]

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

    @commands.command()
    @commands.after_invoke(lvl)
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
    @commands.after_invoke(lvl)
    async def reyn_time(self, ctx):
        await ctx.channel.send('imagine this is a picture')


def setup(bot):
    bot.add_cog(TextCog(bot))
