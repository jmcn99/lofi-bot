import discord
from discord.ext import commands

class Test(commands.Cog):
    def __init__(bot, self):
        self.bot = bot

    @commands.command
    async def test(ctx):
        ctx.send('test')

def setup(bot):
    bot.add_cog(Test(bot))