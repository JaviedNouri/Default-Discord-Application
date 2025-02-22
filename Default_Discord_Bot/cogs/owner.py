# Importing modules
import discord
import os
import random
import traceback
import asyncio

from random import randint
from discord.ext import commands
from discord import slash_command



# Variables
bot = discord.Bot()
client = commands.Bot(command_prefix="?")
admins = [] # <- Input Admin member IDs


# -------------------------------#

class ownerCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
   
# Loads Cog #

    @slash_command()
    async def load(self, ctx, *, module: str):
        if ctx.author.id == (admins):
            """Loads a module."""
            try:
                self.bot.load_extension(f'cogs.{module}')
            except Exception as error:
                exc = traceback.format_exc(limit=500)
                e = discord.Embed(
                    title=error.__class__.__name__, 
                    description=exc,
                    color=discord.Color(randint(0x0, 0xFFFFFF))
                )
            else:
                e = discord.Embed(
                    title='Success',
                    description=f'Loaded {module}',
                    color=discord.Color(randint(0x0, 0xFFFFFF))
                )

            await ctx.send(embed=e)
        else:
            pass


# Unload Cog #

    @slash_command()
    async def unload(self, ctx, *, module: str):
        if ctx.author.id == (admins):
            """Unloads a module."""
            try:
                self.bot.unload_extension(f'cogs.{module}')
            except Exception as error:
                exc = traceback.format_exc(limit=500)
                e = discord.Embed(
                    title=error.__class__.__name__, 
                    description=exc,
                    color=discord.Color(randint(0x0, 0xFFFFFF))
                )
            else:
                e = discord.Embed(
                    title='Success',
                    description=f'Unloaded {module}',
                    color=discord.Color(randint(0x0, 0xFFFFFF))
                )

            await ctx.send(embed=e)
        else:
            pass


# Reload Cog #

    @slash_command()
    async def reload(self, ctx, *, module: str):
        if ctx.author.id == (admins):
            """Reloads a module."""
            try:
                self.bot.reload_extension(f'cogs.{module}')
            except commands.ExtensionNotLoaded:
                e = discord.Embed(
                    title='Error', 
                    description=f'{module} is not loaded.',
                    color=discord.Color(randint(0x0, 0xFFFFFF))
                )
            except Exception as error:
                exc = traceback.format_exc(limit=500)
                e = discord.Embed(
                    title=error.__class__.__name__, 
                    description=exc,
                    color=discord.Color(randint(0x0, 0xFFFFFF))
                )
            else:
                e = discord.Embed(
                    title='Success',
                    description=f'Reloaded {module}',
                    color=discord.Color(randint(0x0, 0xFFFFFF))
                )

            await ctx.send(embed=e)
        else:
            pass


# Announcements #

    @slash_command()
    async def pannouncement(self, ctx, ID : int, *args):
        if ctx.author.id == (admins):
            msg = ' '.join(args)
            colour=random.randint(0, 16777215)
            embed = discord.Embed(title="Server Bot", color = colour)
            embed.add_field(name="Bot Announcement:", value = msg, inline=False)
            channel = self.bot.get_channel(ID)
            await channel.send(embed=embed)
            await asyncio.sleep(1)
            await ctx.message.delete()
            await channel.send("@everyone")
            #await ctx.send("Message sent!")


# Clear Command Line #

    @slash_command()
    async def clear(self, ctx):
        if ctx.author.id == (admins):
            latency = round(self.bot.latency * 1000)
            os.system('clear')
            print(f'{ctx.author} Has successfully cleared and refreshed terminal!')
            embed=discord.Embed(title=f"{ctx.author} Has Cleared Terminal!", description=f"Terminal Has Successfully been cleared.", timestamp=ctx.message.created_at, color=random.randint(0, 16777215))
            embed.set_image(url="https://cdn.discordapp.com/attachments/1015397622367916122/1016912122992676935/rgb.gif")
            embed.set_footer(text=f"- TEST Server Bot - Ping: {latency}ms")
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(title=f"Error with {ctx.prefix}clear", description=f"You are not whitelisted/ the owner of the bot, so you can not use this command.", timestamp=ctx.message.created_at, color=random.randint(0, 16777215))
            embed.set_image(url="https://cdn.discordapp.com/attachments/1015397622367916122/1016912122992676935/rgb.gif")
            embed.set_footer(text=f"- TEST Server Bot  - Ping: {latency}ms")
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(ownerCog(bot))
