import discord
from discord.ext import commands
import random
from settings.settings import DISCORD_TOKEN

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event  
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

bot.load_extension('cogs.gamble.gamble')
bot.load_extension('cogs.text.text')
bot.load_extension('cogs.info.info')
bot.load_extension('cogs.games.games')


bot.run(DISCORD_TOKEN)