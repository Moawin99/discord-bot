from datetime import datetime
from typing import Optional
from discord.ext import commands
from discord.ext.commands import Cog
from discord import Embed
import discord
intents = discord.Intents.default()
intents.members = True

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="userinfo", aliases=["ui", "mi"], brief="--displays userInfo")
    async def user_info(self, ctx, member:Optional[discord.Member]):
        member = member or ctx.author
        embed = Embed(title="User Information",
                      color=member.color,
                      timestamp=datetime.utcnow())
        embed.set_thumbnail(url=member.avatar_url)
        fields = [("ID", member.id, False),
                  ("Name", member.display_name, False),
                  ("Top Role", member.top_role.mention, True),
                  ("Status", member.status, True),
                  ]
        for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=inline)
        await ctx.send(embed=embed)

   
    

def setup(bot):
    bot.add_cog(Info(bot))