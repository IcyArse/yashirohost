import discord
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



client.run(TOKEN)

