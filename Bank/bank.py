import discord
from typing import Optional

class Economy():
    def __init__(self, user:Optional[discord.Member]):
        self.user = user.id
        self.money = 5000

    def deposit(self, user:Optional[discord.Member], amount:int):
        self.money += int

    def withdraw(self, user:Optional[discord.Member], amount:int):
        if(amount > self.money):
            return False
        else:
            self.money -= amount
