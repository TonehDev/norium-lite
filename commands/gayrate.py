import nextcord
from nextcord.ext import commands
import random
from nextcord import Interaction, SlashOption

class GayRate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    testing_id = "some random server id"
    
    @nextcord.slash_command(guild_ids = [testing_id], description = "Accurately measures gay rate")
    async def gayrate(
        self, interaction : Interaction, 
        *, member : nextcord.Member = SlashOption(description = "Provide a member", required = False)
    ):

        if member is None:
            
            embed = nextcord.Embed(
                title = f"Gay Rate",
                description = f"{interaction.user.mention} is **{random.randint(1, 100)}%** gay!",
                color = nextcord.Color.random()
            )

            await interaction.send(embed = embed)
        
        elif member is not None:

            embed = nextcord.Embed(
                title = f"Gay Rate",
                description = f"{member.mention} is **{random.randint(1, 100)}%** gay!",
                color = nextcord.Color.random()
            )

            await interaction.send(embed = embed)

def setup(bot):
  bot.add_cog(GayRate(bot))