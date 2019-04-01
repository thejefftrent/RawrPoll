import auth
import discord
from discord.ext import commands


#client = discord.Client();
bot = commands.Bot(command_prefix='+');

#@client.event
@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("with the API"))

#@client.event
@bot.event
async def on_message(message):
    if not message.author.bot:
        await bot.process_commands(message)

@bot.command()
async def test(ctx):
    await ctx.send("Hello!")


bot.run(auth.discordToken)
