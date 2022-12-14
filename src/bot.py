import os
import discord
from src import reyn

from dotenv import load_dotenv

# -------------------- BOT SETUP --------------------

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.members = True

initial_extensions = ['cogs.text',
                      'cogs.voice']


bot = reyn.Reyn(command_prefix='.', intents=intents)

if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)


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

bot.run(TOKEN)
