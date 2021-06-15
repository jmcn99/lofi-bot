import discord
from discord.ext import commands
from discord.ext.commands import Bot

import sys
import os

import urllib.request
import urllib
import json

import yaml

playlists = ''

if not os.path.isfile("playlists.yaml"):
    sys.exit("'playlists.yaml' not found! Please add it and try again.")
else:
    with open("playlists.yaml") as file:
        playlists = yaml.load(file, Loader=yaml.FullLoader)

class Radio(commands.Cog):


    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def playlist(self, ctx, name):
        if name.lower() in playlists:
            print('test')
        else:
            await ctx.send("Sorry, that playlist doesn't exist! Use .playlists for a list.")


    @commands.command()
    async def playlists(self, ctx):
        embed = discord.Embed(title='Playlists:', color=0xbe38f3)

        

        for x in playlists:
            
            list = ' '
            
            for i in playlists[x]:
                params = {"format": "json", "url": i}
                url = "https://www.youtube.com/oembed"
                query_string = urllib.parse.urlencode(params)
                url = url + "?" + query_string

                with urllib.request.urlopen(url) as response:
                    response_text = response.read()
                    data = json.loads(response_text.decode())
                list = list + ('\n - ' + (data['title']))

            embed.add_field(name=x, value=list)

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Radio(bot))

