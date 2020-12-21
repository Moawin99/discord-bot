import discord
from discord.ext import commands

client = discord.Client()
intents = discord.Intents.default()
bot = commands.Bot(command_prefix='$')


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def ping(ctx):
        await ctx.send('Pong!')

@bot.command()
async def hello(ctx):
    await ctx.send('Hello!')

@bot.command()
async def work(ctx):
    await ctx.send('I am Working!')


bot.run('Nzg5NTI4MzQzMTEyMTg3OTI0.X9zXkQ.OhKWXomXABoVqLgcFM51CgXaIgY')