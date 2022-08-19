import random

from discord.ext import commands


class TextCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

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


async def setup(bot):
    await bot.add_cog(TextCog(bot))
