# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 00:35:05 2021

"""

import discord
from discord.ext import commands
import nest_asyncio
import json
nest_asyncio.apply()

with open("./cogs/matchups.json", "r") as f, open("./cogs/aliases.json","r") as x:
    jmatch = json.load(f, strict = False)
    jalias = json.load(x, strict = False)

class Matchups(commands.Cog):
    def __init__(self,client):
        self.client = client
        
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.client.user:
            return
        if self.client.user.mentioned_in(message):
            splitMessage = message.content.split(None, 1)[1].lower()
            try:
                matchup = jmatch[jalias[splitMessage]]
                embed = discord.Embed(title = jalias[splitMessage], description = matchup['difficulty'], color = discord.Color.blue())
                embed.add_field(name = 'Pre-6', value = matchup['pre-6'], inline = False)
                embed.add_field(name = 'Post-6', value = matchup['post-6'], inline = False)
                await message.channel.send(embed = embed)
            except KeyError:
                return

def setup(client):
    client.add_cog(Matchups(client))

