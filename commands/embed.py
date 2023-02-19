import nextcord
from nextcord.ext import commands
from nextcord import Interaction, SlashOption
import re

class embed(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    testing_id = "some random server id"

    @nextcord.slash_command(guild_ids = [testing_id], description = "Build an embed")
    async def embed(
        self, interaction : Interaction, 
        title: str = SlashOption(description = "Provide a title", required = True),
        description: str = SlashOption(description = "Provide a description", required = True)
    ):

        embed = nextcord.Embed(
            title = f"{title}",
            description = f"{description}",
            color = nextcord.Color.random()
        )

        await interaction.send(embed = embed)

def setup(bot):
    bot.add_cog(embed(bot))
