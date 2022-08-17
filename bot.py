import os
import random
import discord

from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='R!', intents=intents)

# -------------------- EVENTS --------------------


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord.')


@bot.event
async def on_member_join(member):
    print('NEW MEMBA\' DETECTED')
    await member.create_dm()
    await member.dm_channel.send(
        f'Reyn time, {member.name}'
    )

# -------------------- COMMANDS --------------------


@bot.command(name='talk')
async def talk(ctx):
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


@bot.command(name='voice', pass_context=True)
async def voice(ctx):
    if ctx.author.voice:
        channel = ctx.message.author.voice.channel
        print(channel)
        await channel.connect()
    else:
        await ctx.send("Man, wha' a buncha jokas!")


bot.run(TOKEN)