import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('$ping'):
        await message.channel.send('Pong!')

    

client.run('Nzg5NTI4MzQzMTEyMTg3OTI0.X9zXkQ.Wg2Th7FsOZ70h6HvuHtNt5BEWxA')