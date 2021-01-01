from discord.ext import commands
import random
import discord
from Bank.bankbag import BankBag
from Bank.bank import Economy
from typing import Optional

class Gamble(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bag = BankBag()

    @commands.command(brief='--begins gambinling for server')
    async def gamble(self, ctx):
        for member in ctx.guild.members:
            bag.add(Economy(member))
        ctx.send('All members have 5000 coins to bet, let the Gambling Begin!')

       
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
        


def setup(bot):
    bot.add_cog(Gamble(bot))