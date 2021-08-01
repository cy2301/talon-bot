# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 00:35:05 2021

"""

import discord
from discord.ext import commands
import nest_asyncio
nest_asyncio.apply()

class Matchups(commands.Cog):
    def __init__(self,client):
        self.client = client
        
    @commands.command(name = 'Ahri')
    async def ahri(self,ctx):
        embed = discord.Embed(title = 'Ahri', description = '**Hard**', color = discord.Color.blue())
        embed.add_field(name = 'Pre-6', 
                        value = 'You should not engage on her with rQ if she has her charm up as you will be heavily outtraded. Instead, stand behind your minions to avoid being charmed.\
 This also means that you should not let her shove you under turret, as it will be easier for her to land E on you. Note that her Q does increased damage on the way back; it is\
 easier to dodge the return damage if you\'re not at the max range of her Q.',
                        inline = False)
        embed.add_field(name = 'Post-6',
                        value = 'Look to roam post-6. Generally, you will not be able to kill her unless you can flower or burst her quickly before she uses E or R.',
                        inline = False)
        await ctx.send(embed = embed)
    
    @commands.command(name = 'Akali')
    async def akali(self,ctx):
        embed = discord.Embed(title = 'Akali', description = '**Hard**', color = discord.Color.blue())
        embed.add_field(name = 'Pre-6', 
                        value = 'An Akali favored matchup usually. Her Q uses a lot of energy and her waveclear is worse when her W is down. Punish her when she\'s low on energy. \
 If she has E, don\'t rQ. Her W is 20 sec cd, wait for it to expire when she uses.',
                        inline = False)
        embed.add_field(name = 'Post-6',
                        value = 'Buy sweeper for her shroud so you can throw W accurately and track her. Then when she appears, you can AA > mQ > AA and drag back W. Generally, you do not want to fight her as she can choose when to leave and when to fight.\
 Instead, just push the wave and roam. Depending on her build (any armor, HP, etc), you might be able\
 to burst her before she can E, R, or W. Note that you can ult if she hits her E on you, preventing her from recasting. You can use this time to disengage.',
                        inline = False)
        await ctx.send(embed = embed)
        
    @commands.command(name = 'Anivia')
    async def anivia(self,ctx):
        embed = discord.Embed(title = 'Anivia', description = '**Hard**', color = discord.Color.blue())
        embed.add_field(name = 'Pre-6', 
                        value = 'Her poke is very good with Q and E. Generally, do not try to kill her unless she slips close without her stun. You will usually waste too much just for\
 her passive. Look to roam early if you can and try to match her poke with W (while also CSing). Note you can jump over her wall.',
                        inline = False)
        embed.add_field(name = 'Post-6',
                        value = 'Try your best to push and roam. Her waveclear is much better than yours. However, she does not have the mobility to follow your roams. If she tries, you can ambush her.',
                        inline = False)
        await ctx.send(embed = embed)
        
    @commands.command(name = 'Annie')
    async def annie(self,ctx):
        embed = discord.Embed(title = 'Annie', description = '**Intermediate**', color = discord.Color.blue())
        embed.add_field(name = 'Pre-6', 
                        value = 'She is very squishy early and her stun is very telegraphed. Look to trade when she\'s at 1-2 stacks and back off when she has 3-4. This entire matchup revolves around\
 playing against her stun. Her waveclear is poor early, so look to shove her in for easy prio.',
                        inline = False)
        embed.add_field(name = 'Post-6',
                        value = 'You can look to burst her, but note that she can also easily one-shot you if her stun is up. Since her waveclear is subpar to yours, you can also look to roam.',
                        inline = False)
        await ctx.send(embed = embed)
        
    @commands.command(name = 'AurelionSol', aliases = ['asol', 'aurelion'])
    async def asol(self,ctx):
        embed = discord.Embed(title = 'Aurelion Sol', description = '**Easy**', color = discord.Color.blue())
        embed.add_field(name = 'Pre-6', 
                        value = 'Look to trade if you can draw out and dodge his Q stun, which is his only disengage pre-6. Note that his Q range is the radius of his orbs. You can\
 rQ inside his orb zone, so long as his stun isn\'t up, and win pretty much all short trades. Note that his roaming is just as good as yours so ping MIA if he\'s missing.',
                        inline = False)
        embed.add_field(name = 'Post-6',
                        value = 'If you have Prowler\'s, you can either rQ or Prowler\'s first to draw the R and then gapclose with the other ability. Otherwise, you can W > R and use your R to get close and\
 combo him. Match his roams as best as you can.',
                        inline = False)
        await ctx.send(embed = embed)
        
    @commands.command(name = 'Azir')
    async def azir(self,ctx):
        embed = discord.Embed(title = 'Azir', description = '**Intermediate**', color = discord.Color.blue())
        embed.add_field(name = 'Pre-6', 
                        value = 'Very squishy, but has obnoxiously strong poke early. Try to CS and poke him with W at the same time and just let him push. You can also take trades with him when his\
 Q is on cooldown.',
                        inline = False)
        embed.add_field(name = 'Post-6',
                        value = 'Diving him post-6 is generally a bad idea. However, you can jump over his wall if he throws it down. Mainly look to roam instead of fighting him in lane.',
                        inline = False)
        await ctx.send(embed = embed)
        
    @commands.command(name = 'Brand')
    async def brand(self,ctx):
        embed = discord.Embed(title = 'Brand', description = '**Intermediate**', color = discord.Color.blue())
        embed.add_field(name = 'Pre-6', 
                        value = 'Focus on dodging his W and distance yourself from minions to avoid his E spread. His Q will stun you if you\'re on fire so dodge it if you\'re trying to trade.',
                        inline = False)
        embed.add_field(name = 'Post-6',
                        value = 'You can easily kill him since he has no mobility. However, it is very important you dodge his Q stun and W or else you will die.',
                        inline = False)
        await ctx.send(embed = embed)
        
    @commands.command(name = 'Cassiopeia', aliases = ['cass'])
    async def cassiopeia(self,ctx):
        embed = discord.Embed(title = 'Cassiopeia', description = '**Intermediate**', color = discord.Color.blue())
        embed.add_field(name = 'Pre-6', 
                        value = 'Do not walk up if posioned and avoid engaging with rQ if she has W. Focus mainly on dodging her Q\'s so she cannot E you (her main poke ability). She has poor\
 waveclear early and poor mobility all game, so use that to your advantage.',
                        inline = False)
        embed.add_field(name = 'Post-6',
                        value = 'Her R will stun you if you\'re looking at her. You can use practically any combo on her, just make sure you use the R movespeed to dodge her stun and do not run straight at her.',
                        inline = False)
        await ctx.send(embed = embed)
        
    @commands.command(name = 'Chogath', aliases = ['cho', 'cho\''])
    async def chogath(self,ctx):
        embed = discord.Embed(title = 'Cho\'Gath', description = '**Intermediate**', color = discord.Color.blue())
        embed.add_field(name = 'Pre-6', 
                        value = 'Avoid getting knocked up by his Q. Don\'t stand across from him when his E is active. You can usually look to poke him with W when he tries to CS and AA > mQ > AA him\
 for stronger melee trades.',
                        inline = False)
        embed.add_field(name = 'Post-6',
                        value = 'Roam post-6 as he will start becoming unkillable. Goredrinker/Eclipse and BC or armor pen items will help against him. His R damage is [300/475/650] so\
 keep in mind during all-in\'s.',
                        inline = False)
        await ctx.send(embed = embed)
        
    @commands.command(name = 'Corki')
    async def corki(self,ctx):
        embed = discord.Embed(title = 'Corki', description = '**Easy**', color = discord.Color.blue())
        embed.add_field(name = 'Pre-6', 
                        value = 'Take MR runes against him since his auto\'s do 80% AP damage. Whittle him down with W. You can outtrade his E with W > AA > mQ > AA. Do not let him\
 poke you out with his auto\'s.',
                        inline = False)
        embed.add_field(name = 'Post-6',
                        value = 'Look to roam post-6 and focus on dodging his R\'s in 1v1\'s. You can also whittle him down with W and burst him quickly at level 6.\
 Be careful if he picks up his package as his empowered W will be a major teamfight ability as it gives a 90% slow and is damaging.',
                        inline = False)
        await ctx.send(embed = embed)
        
    @commands.command(name = 'Diana')
    async def diana(self,ctx):
        embed = discord.Embed(title = 'Diana', description = '**Easy**', color = discord.Color.blue())
        embed.add_field(name = 'Pre-6', 
                        value = 'Dodge her Q\'s by walking towards her or away from the arc. Generally, you do not want to engage on her with rQ or want to fight her when she has W.\
 Let her engage on you and use AA > mQ > AA to win trades.',
                        inline = False)
        embed.add_field(name = 'Post-6',
                        value = 'If you take Conq against her, you can usually win duels against her. Stack Conq and use your ult at around 8-10 stacks or if you\'re getting low. Wait for your CD\'s and then\
 burst her. Otherwise, look to roam.',
                        inline = False)
        await ctx.send(embed = embed)
    
    @commands.command(name = 'Ekko')
    async def ekko(self,ctx):
        embed = discord.Embed(title = 'Ekko', description = '**Intermediate**', color = discord.Color.blue())
        embed.add_field(name = 'Pre-6', 
                        value = 'You can start Q to pressure him hard early or W to get an easy 2 stacks on him when he goes to auto minions. Always AA > mQ > AA if he is in melee range.\
 If you use rQ on him, make sure you can proc passive. His E will allow him to dodge your W2, so use it smartly. Use rQ to kite back W or W first for 2 stacks and then rQ. Respect him if he uses W and back away.',
                        inline = False)
        embed.add_field(name = 'Post-6',
                        value = 'Hard to fight post-6. You want to try to do as much damage as possible without your R and use it after he does. Ignite him before he R\'s so he has reduced healing\
 from his R. Look to roam when you can.',
                        inline = False)
        await ctx.send(embed = embed)
        
    @commands.command(name = 'Fizz')
    async def fizz(self,ctx):
        embed = discord.Embed(title = 'Fizz', description = '**Hard**', color = discord.Color.blue())
        embed.add_field(name = 'Pre-6', 
                        value = 'Start Q and trade with AA > mQ > AA lvl 1. Most Fizz\'s will use their E to dodge your W2. If they do not, you can rQ on them and force them to E. You can\
 also rQ onto him and force him to E, and then W as he lands. If he is in melee range, AA > mQ > AA and auto him until he uses E or force him to use E with W.',
                        inline = False)
        embed.add_field(name = 'Post-6',
                        value = 'Avoid his max range R. Do not use R if you get hit by his, use it after his R is over as it provides true vision. Look to roam as he cannot match your waveclear without\
 using E.',
                        inline = False)
        await ctx.send(embed = embed)
        
    @commands.command(name = 'Galio')
    async def galio(self,ctx):
        embed = discord.Embed(title = 'Galio', description = '**Easy**', color = discord.Color.blue())
        embed.add_field(name = 'Pre-6', 
                        value = 'Use W to whittle him down and AA > mQ > AA if he is in melee range. If he takes aftershock, do not full combo while it\'s active, auto him until it\'s over.\
 You generally don\'t want to rQ on him if he has his knockup since he can follow that up with his full kit. Also take note that he sets up ganks very well so ward appropriately.\
 Note that his knockup can be stopped if you get in front of it, which is useful if Galio is trying to escape with it.',
                        inline = False)
        embed.add_field(name = 'Post-6',
                        value = 'He will be able to follow your roams with his R. Burst your target fast and get out before he lands. Do not get taunted if you\'re in your ult as it will cancel your invis.',
                        inline = False)
        await ctx.send(embed = embed)
        
    @commands.command(name = 'Garen')
    async def garen(self,ctx):
        embed = discord.Embed(title = 'Garen', description = 'Intermediate', color = discord.Color.blue())
        embed.add_field(name = 'Pre-6', 
                        value = 'You usually do not want to rQ onto him. You can trade with him level 2 before he has W. Use AA > mQ > AA. Once he has W, your trades will be much weaker.\
 Instead, let him push you in as he\'s naturally tanky and has lots of sustain from his passive. He will easily outtrade you since his E stacks Conq almost immediately. Try to throw W out just before his Q lands.',
                        inline = False)
        embed.add_field(name = 'Post-6',
                        value = 'Look to roam as much as you can. At this stage, you cannot kill Garen. Note that you can \'dodge\' his R by ulting just as he R\'s, though it doesn\'t put his R on CD.',
                        inline = False)
        await ctx.send(embed = embed)
        
    @commands.command(name = 'Gragas', aliases = ['grag'])
    async def gragas(self,ctx):
        embed = discord.Embed(title = 'Gragas', description = '**Hard**', color = discord.Color.blue())
        embed.add_field(name = 'Pre-6', 
                        value = 'Do not stand in the minion wave when his Q is up, make him choose between shoving or poking you. You do not win trades if you rQ on to him, let him E\
 towards you and AA > mQ > AA.',
                        inline = False)
        embed.add_field(name = 'Post-6',
                        value = 'You will be one-shotted if you\'re caught offguard by his E flash combo. Flash or use R to dodge his E if he tries to E or E flash towards you. Look to\
 roam instead of fighting him.',
                        inline = False)
        await ctx.send(embed = embed)
        
    @commands.command(name = 'Heimerdinger', aliases = ['heimer','dinger'])
    async def heimerdinger(self,ctx):
        embed = discord.Embed(title = 'Heimerdinger', description = '**Intermediate**', color = discord.Color.blue())
        embed.add_field(name = 'Pre-6', 
                        value = 'When using W, try to rake his turrets, him, and minions. Just two of the mentioned is usually good enough for an efficient W. Do not rQ on him unless you can\
 dodge his stun grenade or it is on CD. He will most likely throw it directly in front of him if you try to rQ on him, which you can dodge with flash.',
                        inline = False)
        embed.add_field(name = 'Post-6',
                        value = 'Look to roam post-6. You will not be able to kill him unless you aren\'t hit by the stun, which you can dodge with flash or R.',
                        inline = False)
        await ctx.send(embed = embed)
        
    @commands.command(name = 'Irelia')
    async def irelia(self,ctx):
        embed = discord.Embed(title = 'Irelia', description = '**Intermediate**', color = discord.Color.blue())
        embed.add_field(name = 'Pre-6', 
                        value = 'Do not fight her when she has 4 stacks. You will lose. You can start Q level 1 and trade with her but do not take extended fights. Level 2+, you must be able\
 to sidestep her E. Pay attention to low HP ally minions, you can use W preemptively on them to try to get 2 stacks on her. However, be careful not to be hasty with W. She can use Q to dodge W2 and engage on you, losing you the trade.\
 Generally, let her push the wave and play at turret. Don\'t recklessly push or she will freeze and then run you down.',
                        inline = False)
        embed.add_field(name = 'Post-6',
                        value = 'Do not combo into her W. This also applies to pre-6. If you fight her and you have Conq, try to proc passive without using R and R when you\'re at 8-10 stacks or if you need to.\
 Then, wait for your CD\'s and burst her. You can also use R to run away from her R or to dodge it. Generally, you just want to roam.',
                        inline = False)
        await ctx.send(embed = embed)
        
    @commands.command(name = 'Jayce')
    async def jayce(self,ctx):
        embed = discord.Embed(title = 'Jayce', description = '**Intermediate**', color = discord.Color.blue())
        embed.add_field(name = 'Pre-6', 
                        value = 'Preferably do not rQ onto him as he can easily disengage with mE. Stand behind your minion wave and do your best to avoid his rQ + rE poke. Throw W into him\
 if he is looking to mQ into you and then AA > mQ > AA for passive proc.',
                        inline = False)
        embed.add_field(name = 'Post-6',
                        value = 'Usually W > R > AA > mQ > AA is enough to beat him. Try to dodge his rQ and avoid facechecking bushes into him as his rQ + rE damage will win him fights.',
                        inline = False)
        await ctx.send(embed = embed)
    
    @commands.command(name = 'Karma')
    async def karma(self,ctx):
        embed = discord.Embed(title = 'Karma', description = '**Easy**', color = discord.Color.blue())
        embed.add_field(name = 'Pre-6', 
                        value = 'She has no kill pressure on you in lane, but likewise you\'ll find it extremely hard to jump and find trades against her early.\
 Stand behind minions to avoid her poke.',
                        inline = False)
        embed.add_field(name = 'Post-6',
                        value = 'Serpent\'s Fang is recommended for her shields, bramble vest (bruiser) executioner\'s (lethality) if she rushes moonstone. Since you have better waveclear and a lot more pressure, look to roam and start impacting the map. Note that Karma\'s\
 tether grants true sight.',
                        inline = False)
        await ctx.send(embed = embed)
        
    @commands.command(name = 'Kassadin', aliases = ['kass'])
    async def kassadin(self,ctx):
        embed = discord.Embed(title = 'Kassadin', description = '**Easy**', color = discord.Color.blue())
        embed.add_field(name = 'Pre-6', 
                        value = 'Your waveclear is superior to his and you outtrade him no matter what early. Pressure him hard and bully him if he tries to CS.',
                        inline = False)
        embed.add_field(name = 'Post-6',
                        value = 'Be mindful of his roams. Make sure you follow and match them. He scales very hard so make sure you set him back or prevent him from getting any leads.',
                        inline = False)
        await ctx.send(embed = embed)
        
    @commands.command(name = 'Katarina', aliases = ['kat', 'kata'])
    async def katarina(self,ctx):
        embed = discord.Embed(title = 'Katarina', description = '**Intermediate**', color = discord.Color.blue())
        embed.add_field(name = 'Pre-6', 
                        value = 'Katarina is a weak laner but scales hard and snowballs hard. You can start W and get poke on her or start Q and AA > mQ > AA early. She will usually\
 start Q level 1, so stand away from minions about to die since she will use Q to CS. If she E\'s to her dagger, AA > mQ > AA and hold W for when she E\'s back. Be careful of\
 throwing W and having her E behind you. Generally, just keep an eye out for where her daggers land and stay out of range out of them. Don\'t give her free trades.',
                        inline = False)
        embed.add_field(name = 'Post-6',
                        value = 'You can use R to run out of her R and then full combo her. Generally, you want to just shove and start to outroam her.',
                        inline = False)
        await ctx.send(embed = embed)
        
    @commands.command(name = 'Leblanc', aliases = ['lb'])
    async def leblanc(self,ctx):
        embed = discord.Embed(title = 'Leblanc', description = '**Hard**', color = discord.Color.blue())
        embed.add_field(name = 'Pre-6', 
                        value = 'A lane bully. Back off if you get hit by Q, since she will W immediately after for increased damage. Catch her with 2W as best as you can when she W\'s\
 towards you. If she W\'s on you, you can also mQ immediately to get a fair trade back, or AA > mQ > AA depending on how long she stays. Level 3 onwards, make sure to start sidestepping when she\
 W\'s towards you since you have to dodge her E. Generally, you will not be able to kill her due to her passive. You can tell which of her clones is real as it retains\
 Talon\'s passive stacks.',
                        inline = False)
        embed.add_field(name = 'Post-6',
                        value = 'Shove and roam. She will be doing the same but her waveclear depends on using W, which is a longer CD than yours.',
                        inline = False)
        await ctx.send(embed = embed)
        
    @commands.command(name = 'Lissandra', aliases = ['liss','lis'])
    async def lissandra(self,ctx):
        embed = discord.Embed(title = 'Lissandra', description = '**Intermediate**', color = discord.Color.blue())
        embed.add_field(name = 'Pre-6', 
                        value = 'Her Q splits when it hits anything, so do not stand across from her. There is no real way to kill her early, at best level 2. She has very good gank set up\
 but also very good escape from her W (a root) and E (a blink) respectively.',
                        inline = False)
        embed.add_field(name = 'Post-6',
                        value = 'Her R and possible zhonyas buy makes her even more unkillable. Instead, shove and roam.',
                        inline = False)
        await ctx.send(embed = embed)
        
    @commands.command(name = 'Lucian', aliases = ['luc'])
    async def lucian(self,ctx):
        embed = discord.Embed(title = 'Lucian', description = '**Hard**', color = discord.Color.blue())
        embed.add_field(name = 'Pre-6', 
                        value = 'Play back and farm/poke with W. Do not stand across from him as his Q has a very long range and will poke you hard. Do not rQ on him unless he uses his E. Just play back\
 wait for your jungler, and let him push you in.',
                        inline = False)
        embed.add_field(name = 'Post-6',
                        value = 'You can burst him with flower or W > R > rQ > AA. Make sure you dodge his R as facetanking it is very painful. Since you have kill pressure, it should be\
 easy to shove the wave and start roaming. If he follows, kill him in the river.',
                        inline = False)
        await ctx.send(embed = embed)
        
    @commands.command(name = 'Lux')
    async def lux(self,ctx):
        embed = discord.Embed(title = 'Lux', description = '**Intermediate**', color = discord.Color.blue())
        embed.add_field(name = 'Pre-6', 
                        value = 'Pressure her if she uses Q, which is her only defense against you. If she uses it, you can easily rQ on her and run her down. Also, force her to choose between\
 hitting you or your minions with E by standing away from the wave. If you get hit by her spells, avoid letting her auto you for extra damage. You can shove her into turret, since she has to use abilities to help her CS.',
                        inline = False)
        embed.add_field(name = 'Post-6',
                        value = 'You can buy Serpent\'s to counter her W. Generally, she\'s very squishy so any combo will deal with her. Look to push the wave and roam since she cannot follow. Ensure you do not\
 get hit by her Q, as she will one-shot you.',
                        inline = False)
        await ctx.send(embed = embed)
        
    @commands.command(name = 'Malphite', aliases = ['malph'])
    async def malphite(self,ctx):
        embed = discord.Embed(title = 'Malphite', description = '**Intermediate**', color = discord.Color.blue())
        embed.add_field(name = 'Pre-6', 
                        value = 'Easiest to kill him at level 1-3. He will be much tankier and harder to kill as the game continues. Generally, you want to AA > mQ > AA him if possible since he has to walk up to farm.\
 If you want to pressure him, make sure to keep his passive down by doing some form of damage. You can also slow push into him so since his waveclear is very subpar. With Conq, try to maintain your stacks against him.',
                        inline = False)
        embed.add_field(name = 'Post-6',
                        value = 'Push and roam. His waveclear is inferior to yours and requires him to walk up. If you can, flash his R or dodge it with your R. It is the only ability that makes him a champion\
 later on in the game.',
                        inline = False)
        await ctx.send(embed = embed)
        
    @commands.command(name = 'Malzahar', aliases = ['malz'])
    async def malzahar(self,ctx):
        embed = discord.Embed(title = 'Malzahar', description = '**Easy**', color = discord.Color.blue())
        embed.add_field(name = 'Pre-6', 
                        value = 'Very weak early. His waveclear and damage is terrible compared to yours. Make sure to stop him from waveclearing by killing his swarm with W. Also, do not stand close to minions\
 about to die to his E. That is his main form of damage against you. Since he only has a silence as CC, you can easily rQ on him or get free trades after W hits twice. Note that his spellshield does not negate your passive stacks.',
                        inline = False)
        embed.add_field(name = 'Post-6',
                        value = 'Ward appropriately. He will press his magic outplay button (R) and call his jungler. Buy QSS if he constantly R\'s you. Generally, you want to just\
 push and roam since he cannot follow you. Note that he scales hard and shoves much better once he has his mythic.',
                        inline = False)
        await ctx.send(embed = embed)
        
    @commands.command(name = 'Morgana', aliases = ['morg'])
    async def morgana(self,ctx):
        embed = discord.Embed(title = 'Morgana', description = '**Easy**', color = discord.Color.blue())
        embed.add_field(name = 'Pre-6', 
                        value = 'She has no real kill pressure on you. Don\'t stand in her W and stand behind minions to avoid getting hit by her Q. Don\'t bother trying to rQ on her unless\
 she uses her Q.',
                        inline = False)
        embed.add_field(name = 'Post-6',
                        value = 'Look to roam. If she R\'s you, then you can just E or R away. Note that while you are tethered or if you get stunned, they will see through your invis.',
                        inline = False)
        await ctx.send(embed = embed)
        
    @commands.command(name = 'Neeko')
    async def neeko(self,ctx):
        embed = discord.Embed(title = 'Neeko', description = '**Hard**', color = discord.Color.blue())
        embed.add_field(name = 'Pre-6', 
                        value = 'Stand away from your minions. Her E will root you the more targets it goes through. You would also force her to choose\
 between poking you with Q or CSing. She also has an empowered auto after autoing you twice so do not get poked out by it. Generally, don\'t try to kill her unless she uses her E. Her W is essentially\
 Leblanc\'s passive but with movement speed, making it hard to kill her. The real one will have your passive stacks.',
                        inline = False)
        embed.add_field(name = 'Post-6',
                        value = 'Look to roam. Buy Serpent\'s if you need for her R.',
                        inline = False)
        await ctx.send(embed = embed)
        
    @commands.command(name = 'Orianna', aliases = ['ori'])
    async def orianna(self,ctx):
        embed = discord.Embed(title = 'Orianna', description = '**Intermediate**', color = discord.Color.blue())
        embed.add_field(name = 'Pre-6', 
                        value = 'Stand away from your minions and force her to choose between poking you with Q or CSing the wave. Your distance to her Q also affects travel time, so being further\
 from the orb will make it easier to dodge. She has no CC early but her W MS/slow and her E shield makes her hard to kill. Look to avoid poke and farm.',
                        inline = False)
        embed.add_field(name = 'Post-6',
                        value = 'Look to roam post-6. You can try to kill her but it is hard because of her W, E, and R.',
                        inline = False)
        await ctx.send(embed = embed)
    
    @commands.command(name = 'Pantheon', aliases = ['panth'])
    async def pantheon(self,ctx):
        embed = discord.Embed(title = 'Pantheon', description = '**Hard**', color = discord.Color.blue())
        embed.add_field(name = 'Pre-6', 
                        value = 'Play safe pre-6. The only real chance you win is if you get level 2 first. Don\'t attempt AA > mQ > AA lvl 1 as he will simply outrange you with Q. Stay out of his W range, especially if he is at full stacks and let him push.\
 Do not proc passive on him until after he uses E\'s.',
                        inline = False)
        embed.add_field(name = 'Post-6',
                        value = 'He will be able to match your roams. Ping his possible roaming paths and look to follow. Post-6, you\
 should be able to kill him, especially with the bruiser build. You can also use Prowler\'s or use R to get behind his E, just do not full combo into it.\
 Generally, you should just focus on roaming instead of fighting him.',
                        inline = False)
        await ctx.send(embed = embed)
        
    @commands.command(name = 'Pyke')
    async def pyke(self,ctx):
        embed = discord.Embed(title = 'Pyke', description = '**Intermediate**', color = discord.Color.blue())
        embed.add_field(name = 'Pre-6', 
                        value = 'Stand behind your minions when he channels Q to avoid getting hooked. You can AA > mQ > AA to outtrade him easily in melee range. Note that he can E behind you\
 to dodge your W, so do not throw it too close. Give yourself some distance to back up and avoid the stun. His waveclear is absolutely abysmal so you should be able to get prio on him. Note that he roams very heavily, especially after he has boots.',
                        inline = False)
        embed.add_field(name = 'Post-6',
                        value = 'Push him in and roam. His waveclear will never match yours. If you can proc passive before he E\'s away, that is also ideal since he is squishy. Note that you can use R to dodge his stun.',
                        inline = False)
        await ctx.send(embed = embed)
        
    @commands.command(name = 'Qiyana')
    async def qiyana(self,ctx):
        embed = discord.Embed(title = 'Qiyana', description = '**Intermediate**', color = discord.Color.blue())
        embed.add_field(name = 'Pre-6', 
                        value = 'Keep an eye on what element she has. Orange gives her extra damage (bonus below 50% HP), green gives her an invisibility blanket, and blue roots. As such, ward appropriately in case she uses blue to CC you. Ideally AA > mQ > AA whenever possible\
 but also play against her CD\'s. Do your best to dodge her Q.',
                        inline = False)
        embed.add_field(name = 'Post-6',
                        value = 'Stay away from walls. Look to roam when possile. You should buy sweeper for her invisibility. You both have the potential to one-shot each other just as fast so make sure you proc passive before she gets her CC off on you.',
                        inline = False)
        await ctx.send(embed = embed)
        
    @commands.command(name = 'Renekton', aliases = ['renek'])
    async def renekton(self,ctx):
        embed = discord.Embed(title = 'Renekton', description = '**Intermediate**', color = discord.Color.blue())
        embed.add_field(name = 'Pre-6', 
                        value = 'AA > mQ > AA if he comes by for a trade. Usually, he will look to E through your minions, W > Q, and then E away. Thus, play back and let him push you in.',
                        inline = False)
        embed.add_field(name = 'Post-6',
                        value = 'Look for roams post-6. If you are running Conq, look to stack Conq, R, and then wait your CD\'s before bursting him down. If he uses his R, try to disengage and reengage when it is over.',
                        inline = False)
        await ctx.send(embed = embed)
        
    @commands.command(name = 'Rumble')
    async def rumble(self,ctx):
        embed = discord.Embed(title = 'Rumble', description = '**Hard**', color = discord.Color.blue())
        embed.add_field(name = 'Pre-6', 
                        value = 'Level 2, you can tank his flames and W > AA > mQ > AA for a very easy passive proc. You want to stand behind your minions to avoid his E poke. Later on, you do not want to tank his abilities, especially if he\'s overheated or above 50 heat.',
                        inline = False)
        embed.add_field(name = 'Post-6',
                        value = 'Look to roam instead of fighting him. Rumble gets tanky pretty fast and his R and overheated Q do an insane amount of damage if you\'re not careful.',
                        inline = False)
        await ctx.send(embed = embed)
    
    @commands.command(name = 'Ryze')
    async def ryze(self,ctx):
        embed = discord.Embed(title = 'Ryze', description = '**Intermediate**', color = discord.Color.blue())
        embed.add_field(name = 'Pre-6', 
                        value = 'Don\'t take free poke from him at level 1, instead whittle him down with W whilst CSing. Avoid sticking close to minions once he applies his E since\
 his Q can bounce off onto you. Taking early trades with him is favorable as he has very poor mana sustain.',
                        inline = False)
        embed.add_field(name = 'Post-6',
                        value = 'You can easily burst him down but he scales hard. Look to roam instead. Be careful of him following with R.',
                        inline = False)
        await ctx.send(embed = embed)
        
    @commands.command(name = 'Seraphine', aliases = ['sera'])
    async def seraphine(self,ctx):
        embed = discord.Embed(title = 'Seraphine', description = '**Easy**', color = discord.Color.blue())
        embed.add_field(name = 'Pre-6', 
                        value = 'Look for openings after she uses her spells on the wave (play against her CD\'s). You can usually easily rQ on her so long as she doesn\'t have her empowered E, which will root you. \
 Stand away from the wave to force her to choose between poking you and CSing.',
                        inline = False)
        embed.add_field(name = 'Post-6',
                        value = 'You can either look to roam or kill her. Note that her R will set up ganks and prevent dives so preferably roam since she cannot follow you.',
                        inline = False)
        await ctx.send(embed = embed)
        
    @commands.command(name = 'Sett')
    async def sett(self,ctx):
        embed = discord.Embed(title = 'Sett', description = '**Hard**', color = discord.Color.blue())
        embed.add_field(name = 'Pre-6', 
                        value = 'Let him push you in and stay a good distance from him. Try to farm and poke with W. Usually, he will walk up and then use his Q to give him extra MS before using E\
 to grab you. Usually, you don\'t want to trade with him at all. Even if his E or W is down, his auto\'s do a lot of damage. Note that his E can drag you out of your E.',
                        inline = False)
        embed.add_field(name = 'Post-6',
                        value = 'Look for roams. If you\'re fighting him, it is imperative that you dodge his W, especially the center of it. You can\
 use Prowler\'s if you have it or R. Bramble vest (bruiser) or executioner\'s (lethality) is recommended.',
                        inline = False)
        await ctx.send(embed = embed)
        
    @commands.command(name = 'Swain')
    async def swain(self,ctx):
        embed = discord.Embed(title = 'Swain', description = '**Intermediate**', color = discord.Color.blue())
        embed.add_field(name = 'Pre-6', 
                        value = 'Avoid his E. If it hits something on the way back, it roots that instead, so use your minions to block it. His CSing is poor and requires Q, which has a 10 second CD. So pressure him when it\'s down or shove him into turret.',
                        inline = False)
        embed.add_field(name = 'Post-6',
                        value = 'Look to roam. Your waveclear should be much better than his and his mobility is too poor to follow. Bramble vest (bruiser) or executioner\'s (lethality) recommended for his R. If he uses his R, disengage and reengage after it is over.',
                        inline = False)
        await ctx.send(embed = embed)
        
    @commands.command(name = 'Sylas')
    async def sylas(self,ctx):
        embed = discord.Embed(title = 'Sylas', description = '**Intermediate**', color = discord.Color.blue())
        embed.add_field(name = 'Pre-6', 
                        value = 'You can start Q or W. If you start Q, look to AA > mQ > AA, especially if he goes for E. When trading with him, make sure to use minions to block his E2 chain so you aren\'t stunned. Also, make sure you dodge his Q explosion. An early executioner\'s is recommended\
 against him and makes trading much better. Usually, you do not want to rQ into him when he has E up. Instead, play around his cooldowns, with all his abilities have at least 10 sec CD\'s at level 1.',
                        inline = False)
        embed.add_field(name = 'Post-6',
                        value = 'Look to roam. You can fight him with Conq similar to any other bruiser. Stack it with a simple W > Q rotation and then R, wait for CD\'s, and burst him. Note that he scales pretty well.',
                        inline = False)
        await ctx.send(embed = embed)
        
    @commands.command(name = 'Syndra')
    async def syndra(self,ctx):
        embed = discord.Embed(title = 'Syndra', description = '**Hard**', color = discord.Color.blue())
        embed.add_field(name = 'Pre-6', 
                        value = 'Heavily Syndra favored. Erratic movement and early boots can help avoid her Q poke. Do not position yourself directly across from her to avoid her E stun.\
 Unless her E is down, you will find little chance to rQ on her.',
                        inline = False)
        embed.add_field(name = 'Post-6',
                        value = 'Look to roam. She has a magic outplay button (R) and will one-shot you if you\'re low enough. You can try one-shotting her first but you must dodge her stun. Hexdrinker is optional for her R.',
                        inline = False)
        await ctx.send(embed = embed)
        
    @commands.command(name = 'Tristana', aliases = ['trist'])
    async def tristana(self,ctx):
        embed = discord.Embed(title = 'Tristana', description = '**Hard**', color = discord.Color.blue())
        embed.add_field(name = 'Pre-6', 
                        value = 'A very rough matchup. Play passively whilst trying to farm as much as you can without taking poke. Usually, you want to just let her push you in. Her early burst is very strong\
 and she can easily follow you over walls with W. Play safely and just look to survive until 6. Note that her W resets on takedowns and when she fully stacks her E. Also note that she has a very strong level 2 as she can W on to you and stack her E.',
                        inline = False)
        embed.add_field(name = 'Post-6',
                        value = 'You can burst her down with a very fast flower combo. You must proc passive before she can R you or W away. Generally, you just want to roam. If she W\'s onto you, it\'s a free kill.',
                        inline = False)
        await ctx.send(embed = embed)
        
    @commands.command(name = 'TwistedFate', aliases = ['tf','twisted','fate'])
    async def TwistedFate(self,ctx):
        embed = discord.Embed(title = 'Twisted Fate', description = '**Intermediate**', color = discord.Color.blue())
        embed.add_field(name = 'Pre-6', 
                        value = 'Play carefully against his cards. Red has splash damage so back away from your minions when he pulls it. Blue does more damage. Gold stuns.\
 If his cards are on CD, you can easily rQ on him. Focus on dodging his Q as well. If he is drawing cards, respect that and back off. Note that he has excellent gank setup with his gold card, so ward appropriately.',
                        inline = False)
        embed.add_field(name = 'Post-6',
                        value = 'He will start roaming with his R. Ward the typical roam paths or the middle of the lane and follow as best you can. You can easily burst him if you catch him out of position since his only escape is drawing a gold card.\
 In teamfights, he might use R to reveal your invisibility. Edge of Night will help with that.',
                        inline = False)
        await ctx.send(embed = embed)
        
    @commands.command(name = 'Veigar')
    async def vegiar(self,ctx):
        embed = discord.Embed(title = 'Veigar', description = '**Easy**', color = discord.Color.blue())
        embed.add_field(name = 'Pre-6', 
                        value = 'Veigar\'s Q only can hit 2 targets. Use that to your advantage. His W is a fairly easy ability to dodge.\
 His E is his only major CC and gives very good gank setup, so ward appropriately. If you\'re inside it, focus on dodging his abilities. If his E is on CD, he is a free kill since he has no other CC abilities.',
                        inline = False)
        embed.add_field(name = 'Post-6',
                        value = 'Careful of his magic outplay button (R). It will execute you at low HP. You can prevent Veigar from casting R by using your R. Usually, just look to roam. Edge of Night is also a good buy into his E.',
                        inline = False)
        await ctx.send(embed = embed)
        
    @commands.command(name = 'Velkoz', aliases = ['vel','vel\''])
    async def velkoz(self,ctx):
        embed = discord.Embed(title = 'Vel\'Koz', description = '**Intermediate**', color = discord.Color.blue())
        embed.add_field(name = 'Pre-6', 
                        value = 'Get good at dodging his Q\'s. Use minions as shields or dodge forward since most Velkoz\'s try to predict you backtracking to dodge their Q\'s.',
                        inline = False)
        embed.add_field(name = 'Post-6',
                        value = 'Look to roam. You can use walls to engage onto Velkoz from behind or from the side with E and rQ. Just be sure to dodge his knockup, as it is his main form of CC against you. Also, note that his level 6 combo can\
 one-shot you. Just prioritize dodging his knockup.',
                        inline = False)
        await ctx.send(embed = embed)
        
    @commands.command(name = 'Viego')
    async def viego(self,ctx):
        embed = discord.Embed(title = 'Viego', description = '**Intermediate**', color = discord.Color.blue())
        embed.add_field(name = 'Pre-6', 
                        value = 'Use minions to block his stun and back off if he uses his camouflage since he can get very close while invisible to you. His Q also has a decent range\
 so do not accidentally give him free trades. If he tries to go for melee trades, AA > mQ > AA. His dueling is very good, so make sure you\'re in a position to get passive procced if you\'re fighting.\
 Note that his AA range is long at 175 range.',
                        inline = False)
        embed.add_field(name = 'Post-6',
                        value = 'Look to roam. Your waveclear is much better than his. If you\'re fighting him, be careful of his R. It will make him immune to damage and stop you from getting stacks on him.\
 Bramble (bruiser) or executioner\'s (lethality) is recommended for his sustain.',
                        inline = False)
        await ctx.send(embed = embed)
        
    @commands.command(name = 'Viktor', aliases = ['vik'])
    async def viktor(self,ctx):
        embed = discord.Embed(title = 'Viktor', description = '**Intermediate**', color = discord.Color.blue())
        embed.add_field(name = 'Pre-6', 
                        value = 'Avoid his empowered Q and auto. If you get hit by Q, back off. Early on, he plays like any other poke mage. Just farm and poke with W as best as you can.\
 Erratic movements will help dodge his E, note that he will at some point upgrade it so it will explode. If he drops his W, back off and wait for it to dissipate.',
                        inline = False)
        embed.add_field(name = 'Post-6',
                        value = 'His burst is actually very strong. Do not stand in his R. If he uses his W, you can use your R to wait it out and reset your CD\'s before fighting again. Look to roam post-6 since he will\
 focus on CSing and scaling.',
                        inline = False)
        await ctx.send(embed = embed)
        
    @commands.command(name = 'Vladimir', aliases = ['vlad'])
    async def vladimir(self,ctx):
        embed = discord.Embed(title = 'Vladimir', description = '**Easy**', color = discord.Color.blue())
        embed.add_field(name = 'Pre-6', 
                        value = 'His Q CD is shown by the white bar, so pressure him whenever it\'s on CD (rQ, try to get 2W on him, etc). Usually, this is a farm lane. He has no real kill pressure on you. Just make sure you don\'t give him free Q\'s, especially\
 his empowered ones. Early executioner\'s can help with cutting down his sustain. You can push him into turret and make it hard for him to CS, since his abilities have long CD\'s. You can also rQ onto him, hold W and force him to use W before rQing back on him again.',
                        inline = False)
        embed.add_field(name = 'Post-6',
                        value = 'Do not try to flower him. He has a pool and will negate your burst. Since his waveclear is poor, look to roam instead.',
                        inline = False)
        await ctx.send(embed = embed)
        
    @commands.command(name = 'Xerath', aliases = ['xer'])
    async def xerath(self,ctx):
        embed = discord.Embed(title = 'Xerath', description = '**Easy**', color = discord.Color.blue())
        embed.add_field(name = 'Pre-6', 
                        value = 'Force him to choose between poking you with Q or farming by standing to the side of the wave. If you plan to all-in him, ensure you dodge his stun. You can dodge his Q easier if you walk in one direction and then switch at the last second.\
 You can also shove him into turret and make it hard for him to CS, forcing him to use abilities and waste mana.',
                        inline = False)
        embed.add_field(name = 'Post-6',
                        value = 'You can easily kill him post-6 if you dodge his stun. Use R to dodge it and don\'t run straight at him. Generally, just look to roam since he cannot follow. If he does, you can kill him from FOG.',
                        inline = False)
        await ctx.send(embed = embed)
    
    @commands.command(name = 'Yasuo', aliases = ['yas','windshitter'])
    async def yasuo(self,ctx):
        embed = discord.Embed(title = 'Yasuo', description = '**Intermediate**', color = discord.Color.blue())
        embed.add_field(name = 'Pre-6', 
                        value = 'Before trading, you want to auto or W him to get rid of his passive shield first. Do not take extended trades with him lvl 1 and instead focus on getting level 2.\
 When he E\'s by for trades, AA > mQ > AA and try to match his autos. Lvl 3+, try not to fight him if his windwall is up. You can bait windwall\
 by walking up and pretending to W. If he has Q3 up or you missed W2, respect his engage and back away from the wave and him.',
                        inline = False)
        embed.add_field(name = 'Post-6',
                        value = 'Be careful not to ult into his windwall. You can use your ult to deny his R by ulting just before his knockup or any knockup hits.',
                        inline = False)
        await ctx.send(embed = embed)
        
    @commands.command(name = 'Yone')
    async def yone(self,ctx):
        embed = discord.Embed(title = 'Yone', description = '**Intermediate**', color = discord.Color.blue())
        embed.add_field(name = 'Pre-6', 
                        value = 'Back off if his Q3 is up, though you could also position to W him if he goes for Q3, giving 2 easy stacks. Afterwards, you can rQ him for passive. You can also W1 + W2 > rQ if his Q3 isn\'t up. If he uses E, AA > mQ > AA\
 and then disengage before he can keep stacking damage. Note that you can also force him to E in unfavorable spots, such as rQing on him when he\'s under your turret and bursting him.',
                        inline = False)
        embed.add_field(name = 'Post-6',
                        value = 'Dodge his R with flash or with your own R. If you have Prowler\'s, you can easily use an empowered flower combo + ignite and one-shot him unless he has shieldbow or cloth armor. Usually, just look to roam instead.',
                        inline = False)
        await ctx.send(embed = embed)
        
    @commands.command(name = 'Zed')
    async def zed(self,ctx):
        embed = discord.Embed(title = 'Zed', description = '**Intermediate**', color = discord.Color.blue())
        embed.add_field(name = 'Pre-6', 
                        value = 'Stand behind minions for his Q. This is because his Q does more damage if you\'re the first target it hits. Early on, you can pressure him and get level 2 prio. However, he hits his powerspike at level 3.\
 Note that his W is on ~20 second CD, so if it\'s on CD, you can pressure him. Do not walk into his W range if you\'re on CD, as he will get a free trade on you. Generally, you can dodge his Q\'s by walking in the opposite direction as soon as he throws down his W.\
 He has stronger laning while you have stronger roams.',
                        inline = False)
        embed.add_field(name = 'Post-6',
                        value = 'Whoever hits 6 first has the advantage. If he hits 6 first, back off and wait for yours. If he R\'s you first, do not R until he appears. After that, you can use your R movement speed to dodge his Q\'s and wait out his R.\
 Note that after he R\'s, he will appear behind you. If he uses W, you can try to burst him or if you can catch him from FOG. If fast enough, you can proc passive before he R\'s, or simply do it after he comes out of R. Generally, this is a roam heavy matchup\
 and you will be competing for better roams.',
                        inline = False)
        await ctx.send(embed = embed)
    
    @commands.command(name = 'Ziggs')
    async def ziggs(self,ctx):
        embed = discord.Embed(title = 'Ziggs', description = '**Easy**', color = discord.Color.blue())
        embed.add_field(name = 'Pre-6', 
                        value = 'Dodge his Q poke and stay healthy in lane. If you can rQ on him, you can and force him to W away. Again, stand away from your minions and force him to choose between poking you or CSing. His W is his\
 only disengage.',
                        inline = False)
        embed.add_field(name = 'Post-6',
                        value = 'Look to roam post-6. He will not be able to follow you and is very squishy. A simple flower combo should do before he can W away. Make sure you shove properly, Ziggs is very good at destroying turrets and getting plates.   ',
                        inline = False)
        await ctx.send(embed = embed)
        
    @commands.command(name = 'Zilean', aliases = ['zil'])
    async def zilean(self,ctx):
        embed = discord.Embed(title = 'Zilean', description = '**Intermediate**', color = discord.Color.blue())
        embed.add_field(name = 'Pre-6', 
                        value = 'Dodge his time bombs and stand away from your minions to avoid letting him damage them too. He will be very good at setting up ganks but has no real kill pressure on you. If you can rQ on him and slow him with W, that is ideal.\
 He has a very hard time last hitting, so shove him to turret and force him to use abilities to CS. Note that his E is a very strong slow and will set up his Q\'s.',
                        inline = False)
        embed.add_field(name = 'Post-6',
                        value = 'Look to roam. You cannot burst him since he has chronoshift. Instead, focus on snowballing your team. In fights, just like how you would deal with Lulu R, make him guess who you\'re going to full target. You can rQ > AA > W > R and wait for your CD\'s\
 before full comboing someone else. Either way, try not to waste your full combo on his R and do as much damage without it.',
                        inline = False)
        await ctx.send(embed = embed)
        
    @commands.command(name = 'Zoe')
    async def zoe(self,ctx):
        embed = discord.Embed(title = 'Zoe', description = '**Intermediate**', color = discord.Color.blue())
        embed.add_field(name = 'Pre-6', 
                        value = 'Stand behind your minions in order to not get hit by her E and predict where her Q is going to land when she\'s channeling it. Do not get shoved into turret or you will open yourself up to an easy E. If you do get hit, look for a wall\
 to jump over or minions to get behind. Note that after each ability she uses, she will have an empowered auto. So stay at a good distance and avoid getting poked out. Do not rQ on her unless she uses E or she just used Q. This is because even if she hits E, she won\'t be able\
 to get a long range Q on you.',
                        inline = False)
        embed.add_field(name = 'Post-6',
                        value = 'Look to roam. You can kill her if you can dodge her E with flash or R. Just do not run straight at her. If you rQ on her, you can use flash to immediately dodge her E since it has a delay.\
 If you can flower her and get passive procced before you sleep, that is also an option.',
                        inline = False)
        await ctx.send(embed = embed)
    
def setup(client):
    client.add_cog(Matchups(client))

