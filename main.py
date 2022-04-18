import os
import random
import discord 
from discord.ext import commands
import discord.ext.commands 

client = commands.Bot(command_prefix = '%') # % in front of the command, like %image or %help. We call this the prefix.

# Commands 
def user_is_idotmaster1(ctx):
    return ctx.message.author.id == "your id here" # Currently useless, put your User ID here

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game(f'XXXX')) # This is the status, like "Playing with XXXX"
    print('Hello World! I am ready to serve you!')

@client.command ()
async def whoami(ctx):
   await ctx.send(f'Heil {ctx.message.author.mention}, Thanks for using me!')

@client.command ()
async def ping(ctx):
    await ctx.send(f'the balls ping: **{round(client.latency * 1000)}ms**')

@client.command(pass_context=True)
async def say(ctx, *, message: str):
    if not ("@" in message):
        await ctx.send(message)
    else:
        await ctx.send("stop trying to ping everyone <:trollcrazy:962783074544934962>") # This is an emoji from the bunkercoin discord. To make this work you need to include the ID. To get the full string do \:emojiname: and it will give you <:emojihere:XXXXXXXXXXXXXXXXXX>

@client.command()
async def github(ctx, *, message: str):
    await ctx.send("https://github.com/IdotMaster1/idotbot")

@client.command()
async def image(ctx):
    path = random.choice(os.listdir('holyarchive/'))  # If you are self-hosting, make a folder called holyarchive and stuff you want it to send IT HAS TO BE A VIDEO OR IMAGE
    await ctx.send(file=discord.File("holyarchive/"+path))

# Help command
@client.command ()
async def commands(ctx):
    embed = discord.Embed(
        colour = discord.Colour.blue()
    )
    embed.set_author(name='List of commands')
    
    embed.add_field(name='%whoami', value='Tells you your name, useless to the max', inline=False)
    embed.add_field(name='%ping', value="Give you the ping of the bot", inline=False)
    embed.add_field(name='%say', value="say!!", inline=False)
    embed.add_field(name='%github', value="Print the github page", inline=False)
    embed.add_field(name='%image', value="Best command, Gives you a random meme from my Holy Archive", inline=False)
    embed.set_footer(text="Here to serve you!")
    await ctx.send(embed=embed)

client.run('TOKEN HERE')