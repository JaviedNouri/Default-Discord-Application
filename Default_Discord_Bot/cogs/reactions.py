# Importing modules
import discord

from discord.ext import commands
from discord import slash_command

# -------------------------- #

class reactionsCog():
    def __init__(self, bot):
        self.bot = bot

    # Reaction Role Template
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        messageID = # <- Input message ID here
        if messageID == payload.message_id:
            member = payload.member
            guild = member.guild

            emoji = payload.emoji.name
            if emoji == '': # <- Input emoji or emoji ID here 'Emoji1'
                mrole = discord.utils.get(guild.roles, id= ) # <- Input given Role ID
                await member.add_role(mrole)


    # Add/Remove Reaction Role Template
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        messageID = # <- Input message ID here
        if messageID == payload.message_id:
            member = payload.member
            guild = member.guild

            emoji = payload.emoji.name
            if emoji == '': # <- Input emoji or emoji ID here 'emoji1'
                mrole = discord.utils.get(guild.roles, id= ) # <- Input removed Role ID
                mrole2= discord.utils.get(guild.roles, id= ) # <- Input given Role ID
                await member.remove_role(mrole)
                await member.add_role(mrole2)


        #Reminder to add reaction roles in future.#
        '''color roles
        channel locked roles
        notification roles'''