import auth
import discord

client = discord.Client();

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author != client.user && message.content.startswith('+'):
        if message.content.startswith('+hello'):
            await message.channel.send('Hello! {0.name}'.format(message.author))
        else:
            command = message.content.split(" ")[0][1:]
            await message.channel.send("Sorry, " + command + " is not a valid command")

    else:
        return


client.run(auth.discordToken)
