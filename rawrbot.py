import auth
import discord
from discord.ext import commands
from discord.utils import get

############
# INITIATE #
############
bot = commands.Bot(command_prefix='+');

polls = list()

##########
# EVENTS #
##########
@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("circle game 👌"))

@bot.event
async def on_message(message):
    if not message.author.bot:
        await bot.process_commands(message)

@bot.event
async def on_reaction_add(reaction, user):
    if reaction.message.author.bot:
        print("Someone reacted to a bot")
        for poll in polls:
            if poll.id == reaction.message.id:
                print("Someone reacted with one of my polls!")
                #TODO check to see the pass limit is met

############
# COMMANDS #
############

# @bot.command()
# async def test(ctx):
#     await ctx.send("Hello!")

@bot.command()
async def ping(ctx):
    await ctx.send("PONG! " + str(bot.latency*1000)[:6] + "ms")
    await ctx.message.delete()

@bot.command()
async def poll(ctx, arg = "untitled"):
    embed=discord.Embed(title=arg, color=0xff8040)
    embed.set_author(name="Poll started by " + ctx.message.author.display_name, icon_url=ctx.message.author.avatar_url)
    embed.set_footer(text="Use (+add 'option' emoji "+ str(len(polls)) +") to add another option and then react to vote.")
    polls.append(await ctx.send(embed=embed))
    await ctx.message.delete()
    #print(polls[len(polls)-1].id)


#TODO Check to see if emoji already exists
@bot.command()
async def add(ctx, arg1, arg2, id = 0):
    # Some sanitization
    print(arg2)
    e = arg2
    if arg2[0] == ':' and arg2[-1] == ':':
        e = arg2[1:-1]
    if arg2[0] == '<' and arg2[-1] == '>':
        e = arg2.split(':')[1]
    ec = ":" + e + ":"

    emoji = get(bot.emojis, name=e)
    if emoji == None:
        emoji = e
    print(emoji)
    embed = polls[id].embeds[0]
    embed.add_field(name=ctx.message.author.display_name + " is suggesting:", value=str(emoji) + "—" + arg1, inline=False)
    try:
        await polls[id].add_reaction(emoji)
    except discord.NotFound:
        await ctx.send("An error occured. Likely the emoji does not exist or I don't have access to it.")
        return
    except discord.HTTPException:
        await ctx.send("An error occured when I tried adding a reaction. The emoji should NOT be in plain text")
        return
    await polls[id].edit(embed=embed)
    await ctx.message.delete()

@bot.command()
async def end(ctx, id=0):
    if id < len(polls):
        print("removing " + str(polls[id]))
        polls.remove(polls[id])
    else:
        await ctx.send("No polls exist or the poll id is too large.")
    await ctx.message.delete()
    #Check to see which has the most reactions

    # winner = polls[id].reactions[0]
    # winners = list()
    # for reaction in polls[id].reactions:
    #     if reaction.count > winner.reaction.count:
    #         winner = reaction
    # for reaction in polls[id].reactions:
    #     if reaction.count >= winner.count:
    #         winners.append(reaction)
    # if len(winners) > 0:
    #     pass
    # else:
    #     await ctx.send(str(reaction.emoji) + " is the winner!")
    # polls.remove(polls[id])

@bot.command(name="list")
async def _list(ctx):
    s = "There are " + str(len(polls)) + " polls right now\n"
    i = 0
    for poll in polls:
        print(str(poll.embeds[0].title))
        s += str(i) + "—" + str(poll.embeds[0].title) + "\n"
        s += poll.jump_url + "\n"
        i += 1
    await ctx.send(s)

#TODO extend the duration of the poll
@bot.command()
async def extend(ctx, id=0):
    pass

#TODO set a limit for the amount of votes needed for an option to pass
@bot.command(name="pass")
async def _pass(ctx, id=0):
    pass
###########################
### LETS RUN THIS THING ###
###########################
bot.run(auth.discordToken)
