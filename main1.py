import discord
from textwrap import dedent
import random
from discord import channel

from globals1 import TOKEN, PREFIX

from discord.ext import commands
from functions import embed
from gif_list import wavelist, huglist, kisslist



intents = discord.Intents.default()# sets intents as an instant if intents
intents.members = True# sets intents for members true so we use members from the server

client = commands.Bot(command_prefix=PREFIX, case_insensitive=True, intents=intents)



#welcome_message

# welcome
@client.event
async def on_member_join(member):

    image_link = "https://media.discordapp.net/attachments/814539604472496168/823988886082420796/20210323_203731.gif"
    title = "welcome to __hanako__ <3"
    content = dedent(f"""
    <@!{member.id}>
    ,, <#807544089016401931>
    ,, <#824269867166203955>
    ,, <#807559580863299604>
    """)

    welcome_embed = await embed(title=title, description=content, thumbnail=image_link, colour=0x2f3136)

    await client.get_channel(824596004242194485).send(embed=welcome_embed)




# bye
@client.event
async def on_member_remove(member):
    print(f'{member.name} has left the server! 😭')
    channel = discord.utils.get(member.guild.text_channels, name="welcome and goodbyes")
    await channel.send(f"{member.mention} has left the server! 😭")



#modeeration


# kick
@client.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    if ctx.author in ctx.guild.get_role(825026101528756224).members:
        await member.kick(reason=reason)
        await ctx.send(f"{member.mention} has been kicked")
    else:
        await ctx.reply("You are not allowed to use that command")


# ban
@client.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    if ctx.author in ctx.guild.get_role(825026101528756224).members:
        await member.ban(reason=reason)
    else:
        await ctx.reply("You are not allowed to use that command ")


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

@client.command(aliases=["hey", "hi", "hello"])
async def wave(ctx):
    descriptionhappy = f"{ctx.author.mention} Is Happy! 😄"
    gif = wavelist[random.randint(0, len(wavelist)) - 11]
    embededhappy = await embed(description=descriptionhappy, image=gif, client=client)
    await ctx.send(embed=embededhappy)


# mad
@client.command(aliases= ["hold"])
async def hug(ctx):
    try:
        if ctx.message.mentions:
            descriptionmad = f"{ctx.author.mention} is hugging {ctx.message.mentions[0].mention}! awww how nice!"
            gif = huglist[random.randint(0, len(huglist)) - 10]
            embededmad = await embed(description=descriptionmad, image=gif, client=client)
            await ctx.send(embed=embededmad)
        else:
            descriptionmad = f"You need to tell us who you wan,t hug."
            embededmad = await embed(description=descriptionmad, client=client)
            await ctx.send(embed=embededmad)
    except:
        print("There was a problem with hug()")


# mad
@client.command()
async def kiss(ctx):
    try:
        if ctx.message.mentions:
            descriptionmad = f"{ctx.author.mention} is kissing {ctx.message.mentions[0].mention}! soo cute!!!"
            gif = kisslist[random.randint(0, len(kisslist)) - 9]
            embededmad = await embed(description=descriptionmad, image=gif, client=client)
            await ctx.send(embed=embededmad)
        else:
            descriptionmad = f"You need to tell us who you wan,t kiss."
            embededmad = await embed(description=descriptionmad, client=client)
            await ctx.send(embed=embededmad)
    except:
        print("There was a problem with kiss()")





client.run(TOKEN)