from discord.ext import commands
import random
import discord

class Gamble(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
       
    @commands.command(brief="--flips coin. If heads then double your bet")
    async def heads(self, ctx, bet:int):
        flip = random.randint(0,1)
        if(flip == 1):
            await ctx.send('You WON ${}!'.format(bet*2))
        else:
            await ctx.send('You Lost ${}'.format(bet))

    @commands.command(brief="--flips coin. If heads then double your bet")
    async def tails(ctx, bet: int):
        flip = random.randint(0,1)
        if (flip == 1):
            await ctx.send('You WON ${}!'.format(bet*2))
        else:
            await ctx.send('You Lost ${}'.format(bet))


def setup(bot):
    bot.add_cog(Gamble(bot))