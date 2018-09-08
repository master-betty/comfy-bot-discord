import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='-')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def greet(ctx):
    await ctx.send(":smiley: :wave: Hello, there!")

@bot.command()
async def cat(ctx):
    await ctx.send("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")

@bot.command()
async def boo(ctx):
    await ctx.send("https://www.youtube.com/watch?v=4Ds-oqOjUog")

@bot.command()
async def info(ctx):
    embed = discord.Embed(title="Comfy Bot", description="Dont be straight", color=0xeee657)
    
    # give info about you here
    embed.add_field(name="Author", value="master-betty")
    
    # Shows the number of servers the bot is member of.
    embed.add_field(name="Server count", value=f"{len(bot.guilds)}")

    # give users a link to invite thsi bot to their server
    #embed.add_field(name="Invite", value="[Invite link](<insert your OAuth invitation link here>)")

    await ctx.send(embed=embed)

bot.remove_command('help')

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="nice bot", description="A Very Nice bot. List of commands are:", color=0xeee657)

    embed.add_field(name="-", value="Prefix to call bot", inline=False)
    embed.add_field(name="cat", value="Its a cat", inline=False)
    embed.add_field(name="boo", value="Almost scares you", inline=False)
    embed.add_field(name="greet", value="Gives a nice greet message", inline=False)
    embed.add_field(name="info", value="Gives a little info about the bot", inline=False)
    embed.add_field(name="help", value="Gives this message", inline=False)

    await ctx.send(embed=embed)

bot.run('NDg3NzA4OTI1NzgxNzM3NDcy.DnTdTg.H3RhfajJpVw-nhzrpCplOSoXoxY')