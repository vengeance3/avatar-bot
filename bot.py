import discord

client = discord.Client()


@client.event
async def on_ready():
    print('started')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('>avatar'):
        if len(message.mentions) > 0:
            images = ''
            for user in message.mentions:
                images += str(user.avatar_url) + str('\n')
            await message.channel.send(images)
        else:
            await message.channel.send(message.author.avatar_url)


client.run('token')
