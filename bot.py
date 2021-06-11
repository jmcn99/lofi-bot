import discord
from discord.ext.commands import Bot

import platform
import os
import sys
from dotenv import load_dotenv

import yaml

intents = discord.Intents.default()

load_dotenv()
TOKEN = os.getenv("TOKEN")

bot = Bot(command_prefix=".", intents = intents)

#loading playlists
if not os.path.isfile("playlists.yaml"):
    sys.exit("'playlists.yaml' not found! Please add it and try again.")
else:
    with open("playlists.yaml") as file:
        playlists = yaml.load(file, Loader=yaml.FullLoader)



@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")
    print(f"Discord.py API version: {discord.__version__}")
    print(f"Python version: {platform.python_version()}")
    print(f"Running on: {platform.system()} {platform.release()} ({os.name})")
    print("-------------------")

bot.remove_command("help")

if __name__ == "__main__":
    for file in os.listdir("./cogs"):
        if file.endswith(".py"):
            extension = file[:-3]
            try:
                bot.load_extension(f"cogs.{extension}")
                print(f"Loaded extension '{extension}'")
            except Exception as e:
                exception = f"{type(e).__name__}: {e}"
                print(f"Failed to load extension {extension}\n{exception}")

bot.run(TOKEN)