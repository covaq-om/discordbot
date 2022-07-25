
from audioop import error
from urllib import response
from discord.ext import commands
import discord.embeds
from interactions import Embed, User
import requests
from dislash import SlashClient
import requests
import time
import interactions
import discord.utils 
import random
import json
import os
import asyncio
from discord.ext.commands import has_permissions, MissingPermissions
import fortnite_api
import discord.errors
import discord.voice_client
import discord.ext.commands
from webserver import keep_alive
import discord.ext.tasks
import discord.ext.commands.errors
import discord.ext.commands.context
import discord.ext.commands.core


bot = commands.Bot(command_prefix="/")
slash = SlashClient(bot)
bot.remove_command('help')


api = fortnite_api.FortniteAPI()

@slash.command(
    
    name="access",
    description="It Gives You Access To The Bot.",
    scope=1000858153614843964
)
@commands.has_permissions(send_messages=True)
async def access(ctx, amount=1):
    if ctx.channel.id == 1000858153614843964:
        member = ctx.author
        role = discord.utils.get(ctx.guild.roles, name="access")
        await member.add_roles(role)
        embed = discord.Embed(title=f'You Now Have Access To Use The Bot.', description=f'Welcome {ctx.author.name}#{ctx.author.discriminator} || Type /commands', color=discord.Color.blue())
        embed.set_footer(text=f'Requested by:  {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    else:
        embed = discord.Embed(title='Error', description='This command can only be ran in <#1000858153614843964>', color=discord.Colour.blue())
        await ctx.send(embed=embed)
        time.sleep(2.3)
        await ctx.message.delete()

    if role in member.roles:
        await ctx.channel.purge(limit=amount)
        embed = discord.Embed(title='You Already Have The Access Role..', description=f'', color=discord.Color.blue())
        await ctx.send(embed=embed)

@bot.command()
@commands.has_role("access")
async def check(ctx, *, user="", amount=1, ):
        if user == "":
            embed = discord.Embed(title='Error', description='Please Retry..', color=discord.Color.blue())
            embed.add_field(name='Error', value='Please enter a valid username', inline=True)
            embed.set_footer(text=f'Requested by:  {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
            await ctx.channel.purge(limit=amount)
            await ctx.send(embed=embed)
            return
        else:
            url = f"""https://fortnite-api.com/v2/stats/br/v2?name={user}"""
            headers = {'Authorization': 'f9cf44f0-86ad-4933-8ca9-3a44ada5a821'}
            
            resp = requests.get(url, headers=headers)
            if resp.status_code == 200:
                resp = resp.json()
                account_id = resp['data']['account']['id']
                username = resp['data']['account']['name']   
                level = resp['data']['battlePass']['level']
                overallWins = resp['data']['stats']['all']['overall']['wins']
                overalldeaths = resp['data']['stats']['all']['overall']['deaths']
                overallKills = resp['data']['stats']['all']['overall']['kills']
                overallmatches = resp['data']['stats']['all']['overall']['matches']
                overallkd = round(resp['data']['stats']['all']['overall']['kd'], 2)
                embed = discord.Embed(title='Results on What You Searched. ', description='', color=discord.Color.blue())
                embed.set_author(name='Cypher Bot V2 - qc#1440',
                icon_url='https://cdn.discordapp.com/avatars/962432913767551026/a_736ec547e5dd85e2a32700c7a8d055f0.gif?size=128')
                embed.set_thumbnail(url='https://fortnite-api.com/images/cosmetics/br/cid_175_athena_commando_m_celestial/icon.png')
                embed.add_field(name='Username', value=username, inline=True)
                embed.add_field(name='Account ID', value=account_id, inline=False)
                embed.add_field(name=f'Overall Stats of {username}', value=f'Some of These Stats Will be off by some numbers..', inline=False)
                embed.add_field(name='Level', value=level, inline=True)
                embed.add_field(name='Wins', value=overallWins, inline=True)
                embed.add_field(name='Kd', value=overallkd, inline=True)
                embed.add_field(name='Kills', value=overallKills, inline=True)
                embed.add_field(name='Deaths', value=overalldeaths, inline=True)
                embed.add_field(name='Matches', value=overallmatches, inline=True)
                embed.set_image(url='https://share.creavite.co/4wgJVo0MbAxXVYdv.gif')
                await ctx.channel.purge(limit=1) 
                await ctx.send(embed=embed)
            else:
                if resp.status_code == 403:
                    embed = discord.Embed(title=f"**{user}**   Has Their Account Profile on Private.", description='', color=discord.Color.red())
                    embed.set_footer(text=f'Requested by:  {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)   
                    await ctx.channel.purge(limit=1)   
                    await ctx.send(embed=embed)
            
                elif resp.status_code == 404:
                    embed = discord.Embed(title=f"**{user}**   Does Not Exist.", description='', color=discord.Color.red())
                    embed.set_footer(text=f'Requested by:  {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)   
                    await ctx.channel.purge(limit=1)
                    await ctx.send(embed=embed)
                    

@slash.command(
    name="news",
    description="hows The Fortnite news.",
)
async def news(ctx):
		r = requests.get('https://fortnite-api.com/v2/news')
		data = r.json()
		image = data['data']['br']['image']
		embed = discord.embeds.Embed(title="Fortnite News", description="", color=discord.Colour.blue())
		embed.set_image(url=image)
		await ctx.send(embed=embed)

@slash.command(
    name="download",
    description="Gives You The Link To Download Cypher V1 *Program* and other Stuff that was made by Cypher.",
)
async def commands(ctx):
    if ctx.channel.id == 983352704015413318:
        embed = discord.Embed(title='**Cypher Program V1**   ~   **Download**', description='', color=discord.Color.blue())
        embed.add_field(name='**Cypher V1**', value='https://cdn.discordapp.com/attachments/982288524717989909/997649985086701598/Cypher_Checker.exe', inline=True)
        embed.add_field(name='Q: Why is it detecting it as a virus?', value='A: Well it was a python file converted to exe so it will mark it as a virus.', inline=False)
        embed.set_image(url='https://share.creavite.co/4wgJVo0MbAxXVYdv.gif')
        embed.set_footer(text=f'Requested by:  {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title='Error', description='This command can only be ran in <#983352704015413318>', color=discord.Colour.blue())
        await ctx.send(embed=embed)
        time.sleep(2.3)
        await ctx.message.delete()

@slash.command(
    name="commands",
    description="Shows You Commands of The Bot",
)
async def commands(ctx):
    if ctx.channel.id == 983352704015413318:
        embed = discord.Embed(title='**Cypher Bot V2**   ~   **Commands**', description='', color=discord.Color.blue())
        embed.add_field(name='/commands', value='Shows This Message.', inline=True)
        embed.add_field(name='/news', value='Shows The Fortnite news.', inline=True)
        embed.add_field(name='/access', value=f'Go To  <#1000858153614843964>  To Get Access To The Bot.', inline=False)
        embed.add_field(name='/check', value='Checks The users Stats.', inline=True)
        embed.add_field(name='/invite', value='Gives You The Invite For The Bot.', inline=True)
        embed.add_field(name='/download', value='Gives You The Link To Download Cypher V1 *Program* and other Stuff that was made by Cypher.', inline=False)
        embed.set_image(url='https://share.creavite.co/4wgJVo0MbAxXVYdv.gif')
        embed.set_footer(text=f'Requested by:  {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title='Error', description='This command can only be ran in <#983352704015413318>', color=discord.Colour.blue())
        await ctx.send(embed=embed)
        time.sleep(2.3)
        await ctx.message.delete()

@slash.command(
    
    name="invite",
    description="Has The Discord Bot invite Link",
)
async def invite(ctx, amount=1):
    if ctx.channel.id == 983352704015413318:
            embed = discord.Embed(title="Invite The Bot To Your Server.", description="There Will be a Link Below Just Copy and Paste That into Your Broswer and Make Sure Your Logged into Your Discord Account Then Add it to Your Server", color=discord.Color.blue())
            embed.add_field(name="The Link To Add The Bot", value='Currently No Link Right Know...', inline=False)
            embed.add_field(name="Why?", value="Why? do you need this bot? well you can use the bot for multiple reasons pulling a account or you could use it kinda like wick but less as good as the bot but the bot is good for pulling fortnite accounts.",inline=False)
            embed.add_field(name="Need Help?", value='Cantact qc#1440 if you need help.',inline=False)
            embed.set_image(url='https://share.creavite.co/4wgJVo0MbAxXVYdv.gif')
            embed.set_footer(text=f'Requested by:  {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
            await ctx.channel.purge(limit=amount)
            await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title='Error', description='This command can only be ran in <#983352704015413318>', color=discord.Colour.blue())
        await ctx.send(embed=embed)
        time.sleep(2.3)
        await ctx.message.delete()
@slash.command(
    
    name="clear",
    description="Clears The Messages..",
)
async def clear(ctx, amount=1000):
    await ctx.send("Clearing The Channel")
    time.sleep(1.3)
    await ctx.channel.purge(limit=amount)
 
keep_alive()
token = os.environ.get("DISCORD_TOKEN")
bot.run(token)


bot.run("MTAwMDY0MTI0ODU1NTcwODQzNw.G-8TSA.tm5bJN9JZ5q81FofdBiUU49P16z9L3gBVwPh2I")