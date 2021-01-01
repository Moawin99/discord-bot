import discord
from discord.ext import commands
from typing import Optional

class Economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
