import discord
from discord.ext import commands
import random

client = discord.Client()
bot = commands.Bot(command_prefix='$')

coin_flip = ['heads', 'tails']

@bot.event  
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def heads(ctx, bet: int):
    if coin_flip[random.randint(0,1)] == 'heads':
        await ctx.send('You WON ${}!'.format(bet*2))
    else:
        await ctx.send('You Lost ${}'.format(bet))


@bot.command()
async def tails(ctx, bet: int):
    if coin_flip[random.randint(0,1)] == 'tails':
        await ctx.send('You WON ${}!'.format(bet*2))
    else:
        await ctx.send('You Lost ${}'.format(bet))

@bot.command()
async def slap(ctx, member: discord.Member, *, reason):
    await ctx.send('You slapped {} for {}'.format(member.display_name, reason))

@bot.command()
async def mem(ctx):
    list = await ctx.guild.fetch_members().flatten()
    for members in list:
        ctx.send(members)

bot.run('Nzg5NTI4MzQzMTEyMTg3OTI0.X9zXkQ.OhKWXomXABoVqLgcFM51CgXaIgY')