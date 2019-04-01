import auth
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='+');


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("Dungeons and Dragons"))

@bot.event
async def on_message(message):
    if not message.author.bot:
        await bot.process_commands(message)

@bot.command()
async def test(ctx):
    await ctx.send("Hello!")

@bot.command()
async def ping(ctx):
    await ctx.send("PONG!" + bot.latency + "ms")

bot.run(auth.discordToken)
