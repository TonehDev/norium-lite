import nextcord
from nextcord.ext import commands
from nextcord import Interaction
import random

class dadLocator(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 

    testing_id = "some random server id"

    @nextcord.slash_command(guild_ids = [testing_id], description = "Locate your dad")
    async def locatemydad(
        self, interaction : Interaction
    ):

        responses = [
            "Your dad does not exist.", "You don't have a father.", "Your dad is located in MIAMI, Florida", "Your father is in Ohio 💀", "Your dad is in the backrooms", "Your dad is on Mars", "Your father was sent to North Korea", "Your dad is at the local supermarket getting milk"
        ]

        embed = nextcord.Embed(
            title = "Trying to locate your dad...",
            color = nextcord.Color.random()
        )

        await interaction.send(embed=embed)

        embed = nextcord.Embed(
            title = "Your dad has been located!",
            color = nextcord.Color.og_blurple()
        )

        embed.add_field(
            name = "Location", 
            value = f"{random.choice(responses)}"
        )

        await interaction.edit(embed=embed)

def setup(bot):
    bot.add_cog(dadLocator(bot))