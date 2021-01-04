import discord
from discord.ext import commands
from typing import Optional

class Economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
<<<<<<< HEAD

    async def deposit(self, member: discord.Member, money:int):
        

=======
        self.money = 500

    async def withdraw(self, member:Optional[discord.Member], amount:int):
        if(amount > self.money):
            return False
        await self.money -= amount

    async def deposit(self, member:Optional[discord.Member], amount:int):
        await self.money += amount


def setup(bot):
    bot.add_cog(Economy(bot))
>>>>>>> 4928426ce2c327d15255f9914ddb4c6e2f18c7e4
