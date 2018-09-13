import discord
from discord.ext import commands
import random
import os

cmdPrefix = '-'
bot = commands.Bot(command_prefix=cmdPrefix)

botTitle = "Comfy Bot"
botDescription = "Get comfy, have some coffee. Don't be straight"

#definitely find a better way to do this
sefID = '105043765512679424'
bettyID = '105032168501198848'

print ('TESTING PLEASE WITNESS ME')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('## ----------------- ##')

### Messy code to mess with yousef ###

@bot.event
async def on_message(message):
    print (message)
    print (message.author)
    print (message.author.id)
    print (message.author.name)
    print (message.author.nick)
    print (str(message.author))
    if message.author == message.author:
        print ('If Test success')

    if message.author.id == sefID:
        print ('yousef check success')

    """
    if "not" in message.author:
       await bot.send_message(message.channel, 'yes')
       message.author
    """

######################################

@bot.command()
async def test(ctx):
    print ('test command called')
    #await ctx.send('<@' + bettyID + '>' + " https://www.youtube.com/watch?v=4Ds-oqOjUog")
    await ctx.send("Test Logging. Check application log")

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
async def boosef(ctx):
    await ctx.send('<@' + sefID + '>' + " https://www.youtube.com/watch?v=4Ds-oqOjUog")

@bot.command()
async def diesel(ctx):
    await ctx.send('https://s1.webmshare.com/jRdK6.webm')

@bot.command()
async def dieselfarts(ctx):
    await ctx.send('https://video.twimg.com/ext_tw_video/1031498604740005889/pu/vid/638x360/MU2urw3oGOKZc8rE.mp4?tag=5')

@bot.command()
async def flip(ctx):
    result = 'ERROR'
    flip = random.randint(0, 1)
    if (flip == 0):
        result = "Heads"
    elif (flip == 1):
        result = "Tails"

    await ctx.send(result)

@bot.command()
async def info(ctx):
    embed = discord.Embed(title="Comfy Bot", description=botDescription, color=0xeee657)
    
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
    print ('Sending Help')
    embed = discord.Embed(title=botTitle, description="Get Comfy. List of commands are:", color=0xeee657)

    embed.add_field(name=(cmdPrefix + "greet"), value="Gives a nice greet message", inline=False)
    embed.add_field(name=(cmdPrefix + "cat"), value="Its a cat", inline=False)
    embed.add_field(name=(cmdPrefix + "boo"), value="Almost scares you", inline=False)
    embed.add_field(name=(cmdPrefix + "boosef"), value="Almost scares him", inline=False)
    embed.add_field(name=(cmdPrefix + "diesel"), value="He enters", inline=False)
    embed.add_field(name=(cmdPrefix + "dieselfarts"), value="Don't use this one", inline=False)
    embed.add_field(name=(cmdPrefix + "flip"), value="Heads or tails?", inline=False)
    embed.add_field(name=(cmdPrefix + "info"), value="Gives a little info about the bot", inline=False)
    embed.add_field(name=(cmdPrefix + "help"), value="Gives this message", inline=False)

    await ctx.send(embed=embed)

#from boto.s3.connection import S3Connection
#s3 = str(S3Connection(os.environ['bootyToken']))
#print (s3)
#print ('TESTING PLEASE WITNESS ME2')

discoToken = os.environ.get('bootyToken')

bot.run(discoToken)