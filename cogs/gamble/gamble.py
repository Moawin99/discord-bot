from discord.ext import commands
import random
import discord
from Bank.bank import Economy
from typing import Optional

class Gamble(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief='--begins gambinling for server')
    async def gamble(self, ctx):
        await ctx.send('Gaminbling is still a work in progress')

       
    @commands.command(brief="--flips coin. If heads then double your bet")
    async def heads(self, ctx, bet:int):
        flip = random.randint(0,1)
        if(flip == 1):
            await ctx.send('You WON ${}!'.format(bet*2))
        else:
            await ctx.send('You Lost ${}'.format(bet))

    @commands.command(brief="--flips coin. If heads then double your bet")
    async def tails(self, ctx, bet: int):
        flip = random.randint(0,1)
        if (flip == 1):
            await ctx.send('You WON ${}!'.format(bet*2))
        else:
            await ctx.send('You Lost ${}'.format(bet))

    @commands.command(brief="--Checkes mentioned user's earnings")
    async def amount(self, ctx, member:Optional[discord.Member]):
        member = member or ctx.author
        earnings = list[list.index(member.id)]
        await ctx.send('{} has ${}'.format(member.mention, earnings.money))

    @commands.Cog.listener()
    async def on_command_error(self, ctx, ex):
        print(ex)
        await ctx.send('Nah you did something wrong. Type $help for the list of commands')
        

def setup(bot):
    bot.add_cog(Gamble(bot))