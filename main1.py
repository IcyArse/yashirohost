import discord
import random
import pytz
import datetime

from textwrap import dedent
from gif_list import wavelist, huglist, kisslist,  slaplist, punchlist, bitelist


from discord import channel
from discord.ext import commands

from apscheduler.schedulers.asyncio import AsyncIOScheduler

from globals1 import TOKEN, PREFIX, muterole


from discord.ext import commands
from functions import embed


muted_user_roles = {}



intents = discord.Intents.default()# sets intents as an instant if intents
intents.members = True# sets intents for members true so we use members from the server

client = commands.Bot(command_prefix=PREFIX, case_insensitive=True, intents=intents)

scheduler = AsyncIOScheduler()
muted_user_roles = {}

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
    descriptionhappy = f"{ctx.author.mention} Is Happy! ðŸ˜„"
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


# kiss
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

#slap
@client.command()
async def slap(ctx):
    try:
        if ctx.message.mentions:
            description = f"{ctx.author.mention} is slapped {ctx.message.mentions[0].mention} ouch"
            gif = slaplist[random.randint(0, len(slaplist)) - 9]
            embeded = await embed(description=description, image=gif, client=client)
            await ctx.send(embed=embeded)
        else:
            description = f"You need to tell us who you wan,t to slap."
            embeded = await embed(description=description, client=client)
            await ctx.send(embed=embeded)
    except:
        print("There was a problem with slap()")



#punch
@client.command()
async def punch(ctx):
    try:
        if ctx.message.mentions:
            description = f"{ctx.author.mention} is has punched {ctx.message.mentions[0].mention} ouch"
            gif = punchlist[random.randint(0, len(punchlist)) - 7]
            embeded = await embed(description=description, image=gif, client=client)
            await ctx.send(embed=embeded)
        else:
            description = f"You need to tell us who you wan,t to punch."
            embeded = await embed(description=description, client=client)
            await ctx.send(embed=embeded)
    except:
        print("There was a problem with punch()")


#bite
@client.command(aliases= ["nom","nibble"])
async def bite(ctx):
    try:
        if ctx.message.mentions:
            description = f"{ctx.author.mention} has bitten {ctx.message.mentions[0].mention} yumm!"
            gif = bitelist[random.randint(0, len(bitelist)) - 9]
            embeded = await embed(description=description, image=gif, client=client)
            await ctx.send(embed=embeded)
        else:
            description = f"You need to tell us who you wan,t to bite."
            embeded = await embed(description=description, client=client)
            await ctx.send(embed=embeded)
    except:
        print("There was a problem with bite()")

        
#mute role
@client.command(name="muterole")
@commands.has_permissions(mute_members=True)
async def on_message(ctx):

        global muterole


        try :
                role = await commands.RoleConverter().convert(ctx, str(muterole))# converts muterole to a role object
                permissions = discord.Permissions()# sets permissions as a Permissions object from discord lib


                # contains all the values for the permissions for the role and updates them in the permissions object
                permissions.update(
                        read_messages=True,
                        read_message_history=True,
                        view_channel=True,
                        external_emojis=False,
                        deafen_members=False,
                        create_instant_invite=False,
                        use_external_emojis=False,
                        use_voice_activation=False,
                        connect=False,
                        stream=False,
                        change_nickname=False,
                        embed_links=False,
                        speak=False,
                        add_reactions=False,
                        send_messages=False,
                        send_tts_messages=False,
                        view_audit_log=False,
                        view_guild_insights=False,
                        move_members=False,
                        mute_members=False,
                        priority_speaker=False,
                        manage_permissions=False,
                        manage_roles=False,
                        manage_nicknames=False,
                        manage_emojis=False,
                        manage_webhooks=False,
                        manage_channels=False,
                        manage_guild=False,
                        mention_everyone=False,
                        kick_members=False,
                        ban_members=False,
                )

                await role.edit(reason=None, color=0xd7090b, permissions=permissions)# changes the roles perms according to perms mentioned in the permissions tuple

                description = f"<@&{muterole}> has been set up as the mute role"# description for the embed
                embeded = discord.Embed(title="Mute Role Setted Up", description=description, color=0x2ca26f)# creates the embed

        except:
                embeded = discord.Embed(title="ERROR", description="Role doesn't exists", color=0x090202)# for the end case where the role entered by user doesn't exists


        await ctx.send(embed=embeded)# sends the embed in the chat



#mute
@client.command(name="mute")
@commands.has_permissions(mute_members=True)
async def on_message(ctx, member: discord.Member, *timemute):

        global muted_user_roles

        muterole_obj = await commands.RoleConverter().convert(ctx, str(muterole))# converts muterole to a role object

        time_of_message = ctx.message.created_at# gets the time at which the message was sent by author
        delay = list(timemute)# converts the context of the message into a list

        reason = ""

        timedelta = datetime.timedelta()# creates an empty time lenght to be added into later


        # block to extract the time
        for i in delay:# selects each word from the delay which were split by spaces in the original message

                # if the content is in the format of time
                try :

                        stripped = int(i[:-1])# main check for the try function for time format


                        if "d" in i or "D" in i:# the day gap

                                stripped = int(i[:-1])# slices the last part of the string which will only leave an int part
                                                      # as the input will only consist <number of time><which level> and as level
                                                      # is only one letter it slices it off and leaves a number

                                timedays = datetime.timedelta(days=stripped)# sets the timedays to the no of days in the stripped
                                timedelta = timedelta + timedays# adds the time gap in timedays to the main time gap "timedelta"

                        elif "h" in i or "H" in i:# the hour gap

                                stripped = int(i[:-1])# slices the last part of the string which will only leave an int part

                                timehours = datetime.timedelta(hours=stripped)# sets the timehours to the no of hours in the stripped
                                timedelta = timedelta + timehours# adds the time gap in timehours to the main time gap "timedelta"

                        elif "m" in i or "M" in i:

                                stripped = int(i[:-1])# slices the last part of the string which will only leave an int part

                                timeminutes = datetime.timedelta(minutes=stripped)# sets the timeminutes to the no of minutes in the stripped
                                timedelta = timedelta + timeminutes# adds the time gap in timeminutes to the main time gap "timedelta"

                        elif "s" in i or "S" in i:

                                stripped = int(i[:-1])# slices the last part of the string which will only leave an int part

                                timeseconds = datetime.timedelta(seconds=stripped)# sets the timeseconds to the no of seconds in the stripped
                                timedelta = timedelta + timeseconds# adds the time gap in timeseconds to the main time gap "timedelta"

                except:
                        reason = i# if the content isn't in the format of time it adds it to the reason string


        time_unmute = time_of_message + timedelta# time to unmute the user

        time_unmute_local = time_unmute.replace(tzinfo=pytz.utc).astimezone(pytz.timezone("Asia/Kolkata"))
        time_unmute_local = str(time_unmute_local)[0:19]


        # block to mute and time the unmute
        try:

                muted_user_role_ids = []

                mentioned_roles_list = member.roles
                mentioned_roles_list.pop(0)


                for i in mentioned_roles_list:

                        await member.remove_roles(i)
                        muted_user_role_ids.append(i.id)


                await member.add_roles(muterole_obj)# adds the muterole to the member

                muted_user_roles.update({str(member.id): muted_user_role_ids})# will only happen when muted indefinitely

                # if no time is mentioned
                if time_unmute == time_of_message:

                        title = f"{member.name} muted"
                        desc = f"{member.name} has been muted indefinitely"

                        embeded = discord.Embed(title=title, description=desc, color=0xd60e11)# creates the ember

                        if reason:
                                embeded.add_field(name="Reason", value=reason, inline=False)# adds the reason field to the embed if reason is given

                        await ctx.send(embed=embeded)# sends the embed in the chat

                else :

                        title = f"{member.name} muted"
                        desc = f"{member.name} has been muted for {timedelta}"


                        embeded = discord.Embed(title=title, description=desc, color=0xd60e11)# creates the embed

                        if reason:
                                embeded.add_field(name="Reason", value=reason, inline=False)# adds the reason field to the embed if reason is given

                        await ctx.send(embed=embeded)# sends the embed in the chat

                        async def return_roles():
                                print("pls")
                                try:
                                        for i in mentioned_roles_list:
                                        
                                                await member.add_roles(i)
                                        muted_user_roles.pop(str(member.id))
                                        await member.remove_roles(muterole_obj)# removes the muterole from the user
                                        await ctx.send(f"{member.name} is unmuted")# confirms the unmute in the chat
                                except:
                                        pass

                        scheduler.add_job(return_roles, 'date', run_date=time_unmute_local)
                        scheduler.start()




        except:

                # if any error occurs in the try
                embeded = discord.Embed(title="ERROR", description="mentioned user doesn't exist or used in wrong format.", color=0x090202)

                await ctx.send(embed=embeded)# sends the embed in the chat



#unmute
@client.command(name="unmute")
@commands.has_permissions(mute_members=True)
async def on_message(ctx, member: discord.Member):

        global muted_user_roles

        muterole_obj = await commands.RoleConverter().convert(ctx, str(muterole))# converts muterole to a role object

        try:

                mentioned_roles_id_list = muted_user_roles.get(str(member.id))

                muted_user_roles.pop(str(member.id))

                # removes the mute role from user
                await member.remove_roles(muterole_obj)

                for i in mentioned_roles_id_list:

                        role = await commands.RoleConverter().convert(ctx, str(i))
                        await member.add_roles(role)

                await ctx.send(f"{member.name} has been unmuted")
                mentioned_roles_id_list = []

        except:
                # if the mentioned user is invalid
                embeded = discord.Embed(title="ERROR", description="mentioned user doesn't exists or isn't muted", color=0x090202)
                await ctx.send(embed=embeded)

@client.command()
@commands.has_permissions(manage_messages=True)
async def test(ctx, role: discord.Role):
    print(role.id)


client.run(TOKEN)

