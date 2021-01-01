from Bank.bank import Economy
from typing import Optional
import discord

class BankBag():
    def __init__(self):
        self.list = []

    def add(self, user:Economy):
        list.append(user)

    def get(self, user:Optional[discord.Member]):
        for member in list:
            if(user.id == member.user):
                return member
        return False

    
