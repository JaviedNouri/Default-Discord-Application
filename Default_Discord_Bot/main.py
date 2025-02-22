# Importing Module
import discord
import asyncio
import os
import sys
import time

from colorama import Fore, init
from discord.ext import commands
from itertools import cycle
from datetime import datetime


# Loading Intents
intents = discord.Intents.all()
intents.members = True
intents.typing = True
intents.presences = True

client = commands.Bot(command_prefix = '?', case_insensitive=True, intents=intents)
client.remove_command('help')
status = cycle (['placeholder'])

# Loading Cogs
initial_extensions = ["cogs.events", "cogs.misc", "cogs.owner", "cogs.verify", "cogs.reactions"]
for extension in initial_extensions:
    try:
        client.load_extension(extension)
        print(Fore.GREEN + f"║ → Fully Loaded {extension} ← ║" + Fore.RESET)
    except Exception as e:
        print(Fore.RED + f"║ → Error: Failed to load extension {extension}. ← ║" + Fore.RESET, file=sys.stderr)
        print(e)

# Status Loop
async def status_task():
    while True:
        count = 0
        for g in client.guilds:
            count += g.member_count

        activity = discord.Game(name="Monitoring Server")

        await client.change_presence(status=discord.Status.online, activity=activity)

async def elapsed_time_task():
    start_time = time.time()
    while True:
        elapsed_time = time.time() - start_time
        minutes, seconds = divmod(elapsed_time, 60)
        print(Fore.LIGHTGREEN_EX, f'\b\b║ → Elapsed Runtime: {int(minutes)} Minutes, {int(seconds)} Seconds.\r', end='', flush=True)
        await asyncio.sleep(1)

async def main():
    task = asyncio.create_task(elapsed_time_task())

    await asyncio.gather(task)

# Bot Loaded 
@client.event
async def on_ready():
    client.loop.create_task(status_task())
    client.loop.create_task(main())
    os.system('clear') # If hosted on -WINDOWS OS- replace command 'clear' with 'cls'
    print(Fore.CYAN + f"║ → Bot is online, Logged in as {client.user} ← ║" + Fore.RESET)


# API KEYS

DISCORD_TOKEN = '' # <- 'Input Discord Token'

# ------------------------- #

# Running Bot
client.run(DISCORD_TOKEN) 