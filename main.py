# import discord package
import discord
from discord.ext import commands

# client (the monkey bot)
client = discord.Client()
bot = commands.Bot(command_prefix='$')

@client.event
async def on_ready():
    # DO STUFF
    # 845804101988122657

    general_channel = client.get_channel(845804101988122657)
    await general_channel.send("monke brain online")

@client.event
async def on_message(message):
    if message.content == 'monke version':
        general_channel = client.get_channel(845804101988122657)

        versionEmbed = discord.Embed(title="Current Version", description="Version 1.0.0", color=0x1d5819)
        versionEmbed.add_field(name="Next version:", value="1.0.1", inline=False)
        versionEmbed.add_field(name="Date created:", value="5/22/2021", inline=False)
        versionEmbed.set_footer(text="Brought to you by bananas", icon_url="https://www.kindpng.com/picc/m/47-475412_gorilla-png-transparent-png.png")
        await general_channel.send(embed=versionEmbed)

    if message.content == 'gorilla spin':
        general_channel = client.get_channel(845804101988122657)
        await general_channel.send("OOO OOO AAA AAA")

    if message.content == 'monkey fact':
        general_channel = client.get_channel(845804101988122657)

        monkeyFact = discord.Embed(title="Monkey Fact #{random#here}", color=0x1d5819)
        monkeyFact.add_field(name="Fact:", value="Fact here")
        monkeyFact.set_footer(text="Powered by {data set here}")

        await general_channel.send(embed=monkeyFact)

@client.event
async def on_disconnect():
    general_channel = client.get_channel(845804101988122657)
    await general_channel.send("monke brain offline")

# Run the client on the server
client.run('-----client id here---------')