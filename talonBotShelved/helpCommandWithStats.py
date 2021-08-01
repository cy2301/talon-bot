# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 20:12:19 2021

"""

import discord
import os
from discord.ext import commands
import nest_asyncio
import asyncio
import time
nest_asyncio.apply()

client = commands.Bot(command_prefix = commands.when_mentioned, case_insensitive = True)
client.remove_command('help')

live = #Bot ID here

@client.event
async def on_ready():
    await client.change_presence(activity = discord.Game('with blades'))
    print("Bot online")

@client.event    
async def on_command_error(ctx,error):
    if isinstance(error,commands.CommandNotFound):
        return
    if isinstance(error,commands.CommandOnCooldown):
        message = await ctx.send('This command is on cooldown, please try again in {:.2f}s'.format(error.retry_after))
        time.sleep(5)
        await message.delete()
        return
    print(error)
    
@client.command(name = 'help')
async def help(ctx):
    embed1 = discord.Embed(
            title = 'Talon Bot',
            description = 'Click the emojis to change pages.',
            color = discord.Color.blue()
    )
    embed1.add_field(name = '1 - Commands', value = 'A list of the commands the bot has.', inline = False)
    embed1.add_field(name = '2 - Stats command', value = 'A description of how to use the stats command.', inline = False)
    embed1.add_field(name = '3 - Matchups', value = 'A list of all the matchups supported by the bot', inline = False)
    embed1.add_field(name = '4 - Acknowledgements', value = 'Credits', inline = False)
    embed1.set_footer(text = 'If you have any feedback or suggestions, send them to @Andevar#4110.')
    
    embed2 = discord.Embed(
            title = 'Commands',
            description = '**@Talon Bot <command>**; Case insensitive.',
            color = discord.Color.blue()
    )
    embed2.add_field(name = 'Conq', value = 'Displays the Conqueror runes for Talon.', inline = False)
    embed2.add_field(name = 'Elec', value = 'Displays the Electrocute runes for Talon.', inline = False)
    embed2.add_field(name = 'Lethality', value = 'Displays a pool of items lethality Talon can build and descriptions on them.', inline = False)
    embed2.add_field(name = 'Bruiser', value = 'Displays a pool of items bruiser Talon can build and descriptions on them.', inline = False)
    embed2.add_field(name = 'Combos', value = 'Core Talon combos.', inline = False)
    embed2.add_field(name = 'Skills', value = 'Skill order for Talon.', inline = False)
    embed2.add_field(name = 'Starter', value = 'Starting items for Talon.', inline = False)
    embed2.add_field(name = 'Boots', value = 'Boots options for Talon.', inline = False)
    embed2.set_footer(text = 'Page 1 of 4')
    
    embed3 = discord.Embed(
            title = 'Stats',
            description = '**@Talon Bot stats <rank> <region> <role>**; Displays the winrate, pickrate, and banrate for the selected tags. This command has a 5 second cooldown for performance reasons. Stats taken from U.GG.',
            color = discord.Color.blue()
    )
    embed3.add_field(name = 'Rank', value = 'Platinum, Diamond or their respective abbreviations (plat, dia). This will return stats for Plat+ and Dia+ respectively.', inline = False)
    embed3.add_field(name = 'Region', value = 'Region abbreviations (euw, na, kr, eune, etc). This will return the stats for that region.', inline = False)
    embed3.add_field(name = 'Role', value = 'Standard role names (top, jg, mid, bot, supp). This will return the stats for that role.', inline = False)
    embed3.set_footer(text = 'Page 2 of 4')
    
    embed4 = discord.Embed(
            title = 'Matchups',
            description = '**@Talon Bot <matchup>**',
            color = discord.Color.blue()
    )
    embed4.add_field(name = 'Matchups', value = 'Ahri / Akali / Anivia / Annie / ASol / Azir / Brand / Cassiopeia / Chogath / Corki / Diana / Ekko / Fizz / Galio / Garen / Gragas / Heimerdinger / Irelia /\
 Jayce / Karma / Kassadin / Katarina / Leblanc / Lissandra / Lucian / Lux/ Malphite / Malzahar / Morgana / Neeko / Orianna / Pantheon / Pyke / Qiyana / Renekton / Rumble / Ryze / Seraphine / Sett / Swain /\
 Sylas / Syndra / Tristana / TwistedFate / Veigar / Velkoz / Viego / Viktor / Vladimir / Xerath / Yasuo / Yone / Zed / Ziggs / Zilean / Zoe', inline = False)
    embed4.set_footer(text = 'Page 3 of 4')
    
    embed5 = discord.Embed(
            title = 'Acknowledgements',
            description = 'Big thanks to everyone who helped with this project.',
            color = discord.Color.blue()
    )
    embed5.set_footer(text = 'Page 4 of 4')
    
    contents = [embed1, embed2, embed3, embed4, embed5]
    cur_page = 1
    message = await ctx.send(embed = contents[cur_page - 1])
    await message.add_reaction('\U0001F516')
    await message.add_reaction('1️⃣')
    await message.add_reaction('2️⃣')
    await message.add_reaction('3️⃣')
    await message.add_reaction('4️⃣')
    await message.add_reaction('\U0001F5D1')
    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in {'\U0001F516', '1️⃣', '2️⃣', '3️⃣', '4️⃣', '\U0001F5D1'} and reaction.message.id == message.id
    while True:
        try:
            reaction, user = await client.wait_for('reaction_add', timeout = 300, check = check)
            if str(reaction.emoji) == '\U0001F516' and cur_page != 1:
                cur_page = 1
                await message.edit(embed = contents[cur_page - 1])
                await message.remove_reaction(reaction, user)
            elif str(reaction.emoji) == '1️⃣' and cur_page != 2:
                cur_page = 2
                await message.edit(embed = contents[cur_page - 1])
                await message.remove_reaction(reaction, user)
            elif str(reaction.emoji) == '2️⃣' and cur_page != 3:
                cur_page = 3
                await message.edit(embed = contents[cur_page - 1])
                await message.remove_reaction(reaction, user)
            elif str(reaction.emoji) == '3️⃣' and cur_page != 4:
                cur_page = 4
                await message.edit(embed = contents[cur_page - 1])
                await message.remove_reaction(reaction, user)
            elif str(reaction.emoji) == '4️⃣' and cur_page != 5:
                cur_page = 5
                await message.edit(embed = contents[cur_page - 1])
                await message.remove_reaction(reaction, user)
            elif str(reaction.emoji) == '\U0001F5D1':
                await message.delete()
                break
            else:
                await message.remove_reaction(reaction, user)
                
        except asyncio.TimeoutError:
            await message.clear_reactions()
            break
        
for file in os.listdir('./cogs'):
    if file.endswith('.py') and file != 'webscraper.py':
        client.load_extension(f'cogs.{file[:-3]}')

client.run(live)
