import discord
import config
import image_module

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!hello_world"):
        msg = "H..Hello world, my name is Pandora."
        await client.send_message(message.channel, msg)

    if message.content.startswith("!tags"):
        tags = message.content.replace("!tags ", "")
        url = await image_module.get_random_img(tags)
        await client.send_message(message.channel, url)

@client.event
async def on_ready():
    print("Logged in as:")
    print(client.user.name)
    print(client.user.id)
    print("------")
    print("Setting status as:")
    print("Playing " + config.status)
    await client.change_presence(game=discord.Game(name=config.status))
    print("------")
    print("Joined servers:")
    for server in client.servers:
        print(server.name + " (" + server.id + ")")

client.run(config.token)