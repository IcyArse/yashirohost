import discord
from globals1 import TOKEN, PREFIX
from discord.ext import commands
from functions import embed


intents = discord.Intents().all()
client = commands.Bot(command_prefix=PREFIX)

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

    await client.get_channel(823833801981165611).send(f"{client.user.mention} Im AWAKE!!")



client.run(TOKEN)

