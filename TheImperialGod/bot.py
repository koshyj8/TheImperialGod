"""
MIT LICENCE 2020 - 2021
All the code and the full bot is nothing but TheImperialGod
All the code is made by NightZan999, check him out at https://github.com/NightZan999
The deposit and withdraw command have been added on to by Makiyu-py, he used it in a fork
The repository the code has been taken from is at https://github.com/NightZan999/TheImperialGod

Be sure to have this in your project at the beginning!
"""
import discord #discord object
import discord.ext #external
from discord.ext import commands #commands from external
from discord.ext.commands import CheckFailure #failure
import random #random
import json
import asyncio

def load_cogs(): #loading all our cogs
    extensions = [
        "cogs.giveaways",
        "cogs.info",
        "cogs.math",
        "cogs.misc",
        "cogs.economy",
        "cogs.help",
        "cogs.fun.animals",
        "cogs.fun.imageManipulation",
        "cogs.fun.utils",
        "cogs.moderation.admin",
        "cogs.moderation.mod",
        "cogs.moderation.owner",
    ]
    for extension in extensions:
        client.load_extension(extension)

with open("config.json", "r") as f:
    config = json.load(f)

#consts
BOT_TOKEN = config["token"]
CLIENT_ID = config["clientId"]
CLIENT_SECRET = config["clientSecret"]
PUBLIC_KEY = config["publicKey"]
BOT_PREFIX = config["prefix"]
INVITE_LINK = "https://discordapp.com/oauth2/authorize?&client_id=768695035092271124&scope=bot&permissions=21474836398"

client = commands.Bot(command_prefix = BOT_PREFIX, case_insensitive = True) #making a client object

#when the bot gets ready
@client.event
async def on_ready():
    print("Ready!")
    print("Username: ", client.user.name)
    print("User ID: ", client.user.id)
    print("----------------------------")

async def ch_pr(): #changing the bots status every 5 secs!!!
    await client.wait_until_ready()
    
    while not client.is_closed():
        statuses = [
            f"The Protection of {len(client.guilds)} servers",
            "Making money!",
            "Hosting Giveaways",
            "imp gstart",
            "Kicking people!",
            "Using utils!",
            f"Serving {len(client.users)} users",
            "Calculating inflation!",
            "Changing statuses!"            
        ]
        status = random.choice(statuses)

        await client.change_presence(activity = discord.Streaming(name = status, url = "https://twitch.tv/pewdiepie"))
        await asyncio.sleep(15)

    if client.is_closed():
        print("Offline again, f in the chat for the discord devs!")


@client.event
async def on_guild_join(guild):
    sguild = client.get_guild(config["IDs"]["serverLogId"])
    embed = discord.Embed(title = "I joined a new server!", color = discord.Color.red())

    embed.add_field(name = "Owner:", value = f"`{guild.owner}`")
    embed.add_field(name = "New Servercount:", value = f"`{len(client.guilds)}`")
    embed.add_field(name = "New Usercount:", value = f"`{len(client.users)}`")
    embed.add_field(name = "Name:", value = f"{str(guild.name)}")

    for channel in sguild.channels:
        if channel.id == 781366606202798080:
            await channel.send(embed = embed)
            break
            
@client.event
async def on_guild_remove(guild):
    sguild = client.get_guild(config["IDs"]["serverLogId"])   
    embed = discord.Embed(title = "I left a server!", color = discord.Color.red())

    embed.add_field(name = "Owner:", value = f"`{guild.owner}`")
    embed.add_field(name = "New Servercount:", value = f"`{len(client.guilds)}`")
    embed.add_field(name = "New Usercount:", value = f"`{len(client.users)}`")
    embed.add_field(name = "Name:", value = f"{str(guild.name)}")

    for channel in sguild.channels:
        if channel.id == 781366606202798080:
            await channel.send(embed = embed)
            break

@client.event
async def on_message(msg):
    with open("data/automod.json", "r") as f:
        guilds = json.load(f)

    ctx = await client.get_context(msg)

    try:
        if guilds[str(ctx.guild.id)]["automod"] == "true":
            for word in filtered_words:
                if word in msg.content.lower():
                    await msg.delete()
    except:
        pass

    try:
        if msg.mentions[0] == client.user:
            await msg.channel.send(f"My prefix for this server is `imp`\nCheck out `imp help` for more information")
        elif self.client.user in msg.mentions:
            for i in range(0, len(msg.mentions)):
                if msg.mentions[i] == client.user:
                    await msg.channel.send(f"My prefix for this server is `imp`\nCheck out `imp help` for more information")
                    break
        else:
            pass
    except:
        pass


    await client.process_commands(msg)

@client.command()
async def load(ctx, extension):
    if ZAN_ID != ctx.author.id:
        await ctx.send("Only for bot devs")
        return
    client.load_extension(f"cogs.{extension}")
    await ctx.send("loaded the cog...")

@client.command()
async def unload(ctx, extension):
    if ZAN_ID != ctx.author.id:
        await ctx.send("Only for bot devs")
        return
    client.unload_extension(f"cogs.{extension}")
    await ctx.send('unloaded the cog...')

@client.command(case_insensitive=True)
async def treat(ctx, member:discord.Member):
    if member == ctx.author:
        await ctx.send("You can't treat youself!")
        return
    embed=discord.Embed(
        description=f'You offered {member.name} a treat! {member.mention} react to the emoji below to accept!',
        color=0x006400
    )
    timeout=int(15.0)
    message = await ctx.channel.send(embed=embed)

    await message.add_reaction('🍫')
    
    def check(reaction, user):
        return user == member and str(reaction.emoji) == '🍫'
        
    try:
        reaction, user = await client.wait_for('reaction_add', timeout=timeout, check=check)
        
    except asyncio.TimeoutError:
        msg=(f"{member.mention} didn't accept the treat in time!!")
        await ctx.channel.send(msg)

    else:
        await ctx.channel.send(f"{member.mention} You have accepted {ctx.author.name}'s offer!")
'''
Some fun data about this code:
1 Line of Code = 26/09/2020
50 Lines of Code = 27/09/2020
100 Lines of Code = 29/09/2020
250 Lines of Code = 30/09/2020
500 Lines of Code = 07/10/2020
1000 Lines of Code = 19/10/2020
1500 Lines of Code = 05/11/2020
2000 Lines of Code = 11/11/2020
5000 Lines of Code =
'''
load_cogs() 
client.loop.create_task(ch_pr())
client.run(BOT_TOKEN)