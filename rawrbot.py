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
    embed=discord.Embed(title=arg, color=0xff8040)
    embed.set_author(name="Poll started by " + ctx.message.author.display_name, icon_url=ctx.message.author.avatar_url)
    embed.set_footer(text="Use (+add 'option' emoji) to add another option and then react to vote.")
    polls.append(await ctx.send(embed=embed))
    print(polls[len(polls)-1].id)

@bot.command()
async def add(ctx, arg1, arg2, id = 0):
    print(arg1 + " " + arg2)
    emoji = get(bot.emojis, name=arg2)
    print(emoji)
    embed = polls[id].embeds[0]
    embed.add_field(name=emoji, value=arg1, inline=False)
    await polls[id].add_reaction(emoji)
    await polls[id].edit(embed=embed)

@bot.command()
async def end(ctx):
    pass
###########################
### LETS RUN THIS THING ###
###########################
bot.run(auth.discordToken)
