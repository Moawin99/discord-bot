import discord
from discord.ext import commands
import random

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

bot.run('Nzg5NTI4MzQzMTEyMTg3OTI0.X9zXkQ.OhKWXomXABoVqLgcFM51CgXaIgY')