import os
import random
import discord

token = os.getenv("DISCORD_TOKEN")
#my_guild = os.getenv("DISCORD_GUILD")

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    for guild in client.guilds:
        print(
            f"{client.user} is connected to the following guild:\n"
            f"{guild.name}(id: {guild.id})"
        )
        #if guild.name == my_guild:
         #   break


client.run(token)