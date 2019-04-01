import auth
import discord
from discord.ext import commands

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
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("Dungeons and Dragons"))

@bot.event
async def on_message(message):
    if not message.author.bot:
        await bot.process_commands(message)



############
# COMMANDS #
############

@bot.command()
async def test(ctx):
    await ctx.send("Hello!")

@bot.command()
async def ping(ctx):
    await ctx.send("PONG! " + str(bot.latency*1000)[:6] + "ms")

@bot.command()
async def poll(ctx, arg):
    polls.append(await ctx.send(arg))
    print(polls[len(polls)-1].id)

@bot.command()
async def add(ctx):
    await polls[0].add_reaction(get(bot.get_all_emojis(), name="crit"))
    pass

@bot.command()
async def end(ctx):
    pass
###########################
### LETS RUN THIS THING ###
###########################
bot.run(auth.discordToken)
