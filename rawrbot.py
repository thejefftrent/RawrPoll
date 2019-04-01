import auth
import discord
from discord.ext import commands


client = discord.Client();
bot = commands.Bot(command_prefix='+');

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(status=discord.Status.online, activity=discord.Game("with the API"))

@client.event
async def on_message(message):
     await bot.process_commands(message)

@bot.command()
async def hello(ctx):
    await ctx.send("Hello!")


client.run(auth.discordToken)
