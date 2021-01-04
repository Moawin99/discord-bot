import discord
from discord.ext import commands
from typing import Optional

class Economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def deposit(self, member: discord.Member, money:int):
        

