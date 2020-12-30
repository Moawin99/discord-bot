from discord.ext import commands
import discord

class Text(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief="--Slaps member for reason specified by user")
    async def slap(self, ctx, member: discord.Member, *, reason):
        await ctx.send('You slapped {} for {}'.format(member.mention, reason))

def setup(bot):
    bot.add_cog(Text(bot))