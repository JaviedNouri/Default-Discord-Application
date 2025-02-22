import discord

from datetime import datetime
from discord.ext import commands

client = commands.Bot(command_prefix="?")

class eventsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    # Member Join Event
    @commands.Cog.listener()
    async def on_member_join(self, member):
        time = datetime.now().strftime("%H:%M:%S %p, %d/%m/%Y")
        latency = round(self.bot.latency * 1000)
        channel1 = self.bot.get_channel() # <- Input Welcome Channel ID here
        embed=discord.Embed(title=f"{member} Has Joined the Server.", description=f"Welcome {member.mention} to the Server!")
        embed.set_image() # <- Input image URL for Welcome Embed using url="image url"
        embed.set_footer(text=f"- TEST Server Bot - Ping: {latency}ms • {time}", icon_url="https://cdn.discordapp.com/attachments/1057165871874842685/1057167703858745354/blob.png")
        await channel1.send(embed=embed)


    # Member Leave Event
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        time = datetime.now().strftime("%H:%M:%S %p, %d/%m/%Y")
        latency = round(self.bot.latency * 1000)
        channel = self.bot.get_channel() # <- Input Goodbye Channel ID here
        embed=discord.Embed(title=f"{member} Has Left the Server.", description=f"User: {member.mention} Is not longer a server member.", color=0x5900ff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1057165871874842685/1057168167522271323/a_966e3814f2ea86b10d6769fec11f1910.png")
        embed.set_author(name=f"Discord User: {member} Has Left The Server.", icon_url=member.avatar_url)
        embed.set_footer(text=f"- Server Bot - Ping: {latency}ms • {time}", icon_url="https://cdn.discordapp.com/attachments/1057165871874842685/1057167703858745354/blob.png")
        embed.set_image(url="https://cdn.discordapp.com/attachments/1015397622367916122/1016912122992676935/rgb.gif")
        await channel.send(embed=embed)


def setup(bot):
    bot.add_cog(eventsCog(bot))
