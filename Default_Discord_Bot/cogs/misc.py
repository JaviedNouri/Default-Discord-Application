import discord

from discord.ext import commands, tasks
from colorama import Fore, init
from discord import Option
from discord import (
    slash_command,
    client
)

class miscCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Misc Help
    @slash_command(description="Misc Commands")
    async def misc_help(self, ctx):
        latency = round(self.bot.latency * 1000)

        embed=discord.Embed(title=f"{ctx.author}, Misc Commands For This Server.", description=f"""\
            ```yaml
            \n /Purge: Provide a number of message to mass delete at once.

            \n /Role: Give a mentioned user any role of your choice.

            \n /UnRole: Remove a mentioned user's role of your choice.
                            
            \n /Ping: View the bots ping.
            ```
            """, color=0x5900ff)
        embed.set_footer(text=f"- Server Commands - Latency: {latency}ms.")
        embed.set_image(url="https://cdn.discordapp.com/attachments/969784491864391721/1008451324288979054/rgb.gif")

        await ctx.respond(embed=embed)


    # Error Handler
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        
        if isinstance(error, commands.MissingPermissions):
            await ctx.respond(f"{ctx.author.mention}, Missing Permission: {', '.join(error.missing_perms)} Permission.", delete_after=3)
        
        elif isinstance(error, commands.CommandOnCooldown):
            await ctx.respond(f"{ctx.author.mention}, Please wait ``{int(error.retry_after)} seconds`` before re-using this command.", delete_after=3)
        
        elif isinstance(error, commands.CommandInvokeError):
            await ctx.respond(f"{ctx.author.mention}, Exception in previous command.", delete_after=3)

        elif isinstance(error, commands.CommandNotFound):
            await ctx.respond(f"{ctx.author.mention}, Command not found.", delete_after=3)
            
        elif isinstance(error, commands.ArgumentParsingError):
            await ctx.respond(f"{ctx.author.mention}, Argumant Parsing Error", delete_after=3)

        # Sending Message
        await ctx.respond("Server Ping: ", client.latency * 1000)


    # Purge Command
    @slash_command(description="Purge Messages")
    @discord.default_permissions(
        manage_messages=True
    )
    async def purge(self, ctx, amount: Option(int, "Enter A Purge Amount", required=True)):
        await ctx.channel.purge(limit=int(amount))
        return await ctx.respond(f"{ctx.message.author.mention}, Successfully purged ``{amount}`` Messages.", delete_after=3)


    # User Set Role
    @slash_command(description="Set User Role")
    async def give_role(self, ctx, member: Option(discord.Member, "Select A User", required=True), *, role_name: Option(str or int, "Select A Role", required=True)):
        if member == None:
            await ctx.respond(f"{ctx.author.mention}, Please provide a ``member`` to give a role to.", delete_after=3)
            
        elif role_name == None:
            await ctx.respond(f"{ctx.author.mention}, Please provide a valid ``role ID and/or name`` to give the member.", delete_after=3)
            
        elif role_name == None:
            await ctx.respond(f"{ctx.author.mention}. Please provide a valid role and/or make sure the role name is in character and/or number format.", delete_after=3)

        else:
            guild = ctx.guild
            role = discord.utils.get(guild.roles, name=role_name)

            await member.add_roles(role)
            await ctx.respond(f"{ctx.author.mention}, Successfully added Role: **{role}** to Member: {member.mention}.", delete_after=5)


    # User Remove Role
    @slash_command(description="Remove A User Role")
    async def remove_role(self, ctx, member: Option(discord.Member, "Select A User"), *, role_name: Option(str, "Select A Role", required=True)):
        if member == None:
            await ctx.respond(f"{ctx.author.mention}, Please provide a ``member`` to remove a role from.", delete_after=3)

        elif role_name == None:
            await ctx.respond(f"{ctx.author.mention}, Please provide a valid ``role ID and/or name`` to remove from the member.", delete_after=3)

        elif role_name == None:
            await ctx.respond(f"{ctx.author.mention}. Please provide a valid role and/or make sure the role name is in character and/or number format.", delete_after=3)

        else:
            guild = ctx.guild
            role = discord.utils.get(guild.roles, name=role_name)

            await member.remove_roles(role)
            await ctx.respond(f"{ctx.author.mention}, Successfully removed Role: **{role}** from Member: {member.mention}.", delete_after=5)


    # Ping Command
    @slash_command(description="View The Bot's Ping")
    async def ping(self, ctx):
        # Ping
        ping = round(self.bot.latency * 1000)

        # Setting Embed
        embed = discord.Embed(title=f"{ctx.author}", description="View The Bot's Ping", color=0x5900ff)

        embed.add_field(name="**PING**", value=f"```yaml\n Ping: {ping}ms```", inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/969784491864391721/1008451324288979054/rgb.gif")
        embed.set_footer(text=f"- TEST Server Commands")

        # Sending Message
        await ctx.respond(embed=embed)


def setup(bot):
    bot.add_cog(miscCog(bot))