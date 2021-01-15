from discord.ext import commands
import random
from rps.rpsConverter import RpsConverter
from rps.model import RPS

class Games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(usage = "rock | paper | scissor")
    async def rps(self, ctx, user_choice: RpsConverter):
        rps = RPS()
        bot_choice = random.choice(rps.get_choices())
        user_choice = user_choice.choice
        win_check = {
            (RPS.ROCK, RPS.SCISSOR): True,
            (RPS.ROCK, RPS.PAPER): False,
            (RPS.PAPER, RPS.SCISSOR): False,
            (RPS.PAPER, RPS.ROCK): True,
            (RPS.SCISSOR, RPS.ROCK): False,
            (RPS.SCISSOR, RPS.PAPER): True
        }
        won = None
        if bot_choice == user_choice:
            won = None
        else:
            won = win_check[(user_choice, bot_choice)]
        
        if won is None:
            message = "Draw!"
        elif won is True:
            message = "You win!"
        elif won is False:
            message = "HA you lost to a bot"
        
        await ctx.send(message)
        

def setup(bot):
    bot.add_cog(Games(bot))