import discord
from discord.ext import commands
from discord.ext.commands import Bot
from bot import playlists

import urllib
import lxml
from lxml import etree

class Radio(commands.Cog, name='Radio'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def playlist(self, ctx):
        await ctx.send('not done yet')

    @commands.command()
    async def playlists(self, ctx):
        embed = discord.Embed(title='Playlists:', color=0xbe38f3)

        for x in playlists:
            embed.add_field(name=x)
            for i in playlists[x]:
                streamLink = etree.HTML(urllib.urlopen(i).read())
                streamTitle = streamLink.xpath("//span[@id='eow-title']@title")
                embed.add_field(streamTitle)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Radio(bot))
