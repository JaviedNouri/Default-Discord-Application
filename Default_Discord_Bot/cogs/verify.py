# Importing Module
import discord
import datetime

from discord import slash_command
from discord.ext import commands
from discord.utils import get
from datetime import datetime



class verifyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Verification Help
    @slash_command(description="Verify Help")
    async def verify_help(self, ctx):
        latency = round(self.bot.latency * 1000)
        embed=discord.Embed(title=f"Verification Help For The Server", description=f"""
        ```Verification Help Listed Below.```
        Verify Yourself By Pressing The ``✅`` On The Highlighted Message Above:

        (If Needed): Link To Message: 
        """, color=0x5900ff)
        embed.set_image(url="")
        embed.set_footer(text=f"- TEST Server Verification - Ping: {latency}ms")

        await ctx.respond(embed=embed)


    # Verification Reaction Event
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        latency = round(self.bot.latency * 1000)
        messageID = # Input message ID
        if messageID == payload.message_id:
            member = payload.member
            guild = member.guild

            emoji = payload.emoji.name
            if emoji == '✅':
                mrole = discord.utils.get(guild.roles, id= ) # id= Verified Role ID
                mrole2 = discord.utils.get(guild.roles, id= ) # id= Unverified Role ID
                await member.add_roles(mrole)
                await member.remove_roles(mrole2)

            time = datetime.now().strftime("%H:%M:%S %p, %d/%m/%Y")
            channel = await self.bot.fetch_channel() # Input Channel1 ID
            channel2 = await self.bot.fetch_channel() # Input Channel2 ID || Must remove note # from await channel2.send
            embed=discord.Embed(title=f"{member} Has Verified", description=f"{member.mention} Has Successfully Verified", color=0x5900ff)
            embed.set_image(url="https://cdn.discordapp.com/attachments/969784491864391721/1008451324288979054/rgb.gif")
            embed.set_footer(text=f"- TEST Server - Ping: {latency}ms • {time}")

            await channel.send(embed=embed)
            #await channel2.send(f"{member.mention} Please ask an **Owner** or **Admin** for **Secondary Verification** help.")
            


def setup(bot):
    bot.add_cog(verifyCog(bot))
