import discord
import random
from gif_list import wavelist, huglist
from globals1 import TOKEN, PREFIX
from discord.ext import commands
from functions import embed




intents = discord.Intents().all()
client = commands.Bot(command_prefix=PREFIX,case_insensitive=True  )

#welcome_message

# welcome
@client.event
async def on_member_join(member):
    print(f"{member.name} has joined Welcome! 😊 ")
    channel = discord.utils.get(member.guild.text_channels, name="welcome and goodbyes")
    await channel.send(f"{member.mention} has joined! 😊")



#modeeration


# kick
@client.command()
@commands.has_permissions(manage_messages=True)
async def kick(ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f"{member.mention} has been kicked")



# ban
@client.command()
@commands.has_permissions(manage_messages=True)
async def ban(ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f"{member.mention} has been banned")





#purge
@client.command(aliases=["r", "purge","delete"])
@commands.has_permissions(manage_messages=True)
async def remove(ctx, amount : int):
        await ctx.channel.purge(limit=amount)
        await ctx.send(f'Purged {amount} messages')


# ping
@client.command()
async def ping(ctx):
    title = "Pong!"
    latency = int(round(client.latency * 1000, 0))
    description = f"takes me this long to eat a cookie! {latency}ms."
    embeded = await embed(title=title, description=description, client=client)
    await ctx.send(embed=embeded)



@client.event
async def on_ready():
    print('SUCCESSFULLY LOGGED IN AS', client.user.name.upper())

    await client.get_channel(824596004242194485).send(f"{client.user.mention} Im AWAKE!!")


#gifs

#wave
@client.command(aliases=["hi","hello","hey"])
async def wave(ctx):
    description = f"{ctx.author.mention} is Waving"
    gif = wavelist[random.randint(0, len(wavelist)) - 9]
    embeded = await embed(description=description, image=gif, client=client)
    await ctx.send(embed=embeded)

# pat
@client.command()
async def hug(ctx):
    try:
        if ctx.message.mentions:
            description = f"{ctx.author.mention} has hugged {ctx.message.mentions[0].mention}! Cute!"
            gif = huglist[random.randint(0, len(huglist)) - 3]
            embeded = await embed(description=description, image=gif, client=client)
            await ctx.send(embed=embeded)
        else:
            description = f"You need to tell me who you want to hug."
            embeded = await embed(description=description, client=client)
            await ctx.send(embed=embeded)
    except:
        print("There was a problem with the hug command")


client.run(TOKEN)

