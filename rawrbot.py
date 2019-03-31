import auth
import discord

client = discord.Client();

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author != client.user:
        if message.content.startswith('+hello'):
            await message.channel.send('Hello!')
    else:
        return
client.run(auth.discordToken)
