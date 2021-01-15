from discord.ext import commands
import discord
import requests

class Text(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief="--Slaps member for reason specified by user")
    async def slap(self, ctx, member: discord.Member, *, reason):
        await ctx.send('You slapped {} for {}'.format(member.mention, reason))

    @commands.command(brief="--input artist and song to get lyrics", aliases=['lyrics'])
    async def get_lyrics(self, ctx, artist: str, song:str):
        api = 'https://api.lyrics.ovh/v1/{}/{}'.format(artist,song)
        print(api)
        response = requests.get('https://api.lyrics.ovh/v1/{}/{}'.format(artist,song))
        await ctx.send(response.json())

    @commands.command(brief="--gives good advice!")
    async def advice(self, ctx):
        advice = requests.get('https://api.adviceslip.com/advice')
        data = advice.json()
        await ctx.send(data)
        

def setup(bot):
    bot.add_cog(Text(bot))