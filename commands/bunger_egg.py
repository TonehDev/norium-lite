import nextcord
from nextcord.ext import commands
from nextcord import Interaction

class Bunger(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    testing_id = "some random server id"

    @nextcord.slash_command(guild_ids = [testing_id], description = "Bunger")
    async def bunger(
        self, interaction : Interaction
    ):

        embed = nextcord.Embed(
            title = "Bunger :hamburger:", 
            description = "Bunger :hamburger:", 
            color = nextcord.Color.gold()
        )

        embed.set_image(
            url = "https://cdn.discordapp.com/attachments/943924201688027206/1055920899456512050/bunger.gif"
        )

        await interaction.send(embed = embed)

    @nextcord.slash_command(guild_ids = [testing_id], description = "Oh the misery")
    async def egg(
        self, interaction : Interaction
    ):

        embed = nextcord.Embed(
            title = "Oh the misery...", 
            description = "Egg cat :egg:", 
            color = nextcord.Color.light_grey()
        )

        embed.set_image(
            url = "https://cdn.discordapp.com/attachments/943924201688027206/1055921985219198986/oh-the-misery-eggcat.gif"
        )

        await interaction.send(embed = embed)
    
def setup(bot):
  bot.add_cog(Bunger(bot))