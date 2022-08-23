import asyncio
import os
import random
import discord

from dotenv import load_dotenv
from discord import FFmpegPCMAudio
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.members = True

initial_extensions = ['cogs.text',
                      'cogs.voice']


bot = commands.Bot(command_prefix='.', intents=intents)

# discord.py 2.0 code
# async def load_extensions():
#     for extension in initial_extensions:
#         await bot.load_extension(extension)
# async def main():
#     async with bot:
#         await load_extensions()
#         await bot.start(TOKEN)


if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)

print(bot.extensions)

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

# discord.py 2.0 code
# asyncio.run(main())

bot.run(TOKEN)
