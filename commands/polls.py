import nextcord
from nextcord.ext import commands
from nextcord import Interaction, SlashOption

class Poll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 

    testing_id = "some random server id"

    @nextcord.slash_command(guild_ids = [testing_id], description = "Send a voting message")
    async def poll(
        self, interaction : Interaction, 
        choice1 = SlashOption(description = "First choice", required = True), 
        choice2 = SlashOption(description = "Second choice", required = True),
        *, 
        note = SlashOption(description = "A note you'd like to leave", required = False),
         topic: str
    ):

        if choice1 and choice2:

            embed = nextcord.Embed(
                title = topic,
                description = f":one: {choice1}\n:two: {choice2}",
                color = nextcord.Color.random()
            )

            embed.add_field(
                name = "Notes",
                value = f"{note}"
            )

            embed.set_footer(text = f"Asked by {interaction.user.name}#{interaction.user.discriminator}")

            await interaction.response.send_message(
                embed = embed
            )

            msg = await interaction.original_message()

            await msg.add_reaction("1️⃣")
            await msg.add_reaction("2️⃣")

def setup(bot):
    bot.add_cog(Poll(bot))