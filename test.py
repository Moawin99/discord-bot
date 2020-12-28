import discord
from discord.ext import commands
import random

bot = commands.Bot(command_prefix='$')

@bot.event  
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

bot.load_extension('cogs.gamble.gamble')
bot.load_extension('cogs.text.text')

@bot.command()
async def mem(ctx):
   await ctx.send(ctx.guild.member_count)

bot.run('Nzg5NTI4MzQzMTEyMTg3OTI0.X9zXkQ.OhKWXomXABoVqLgcFM51CgXaIgY')