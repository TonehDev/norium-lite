import nextcord
from nextcord.ext import commands
from nextcord import Interaction, SlashOption 
import random

class Ask(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 

    testing_id = "some random server id"

    @nextcord.slash_command(guild_ids = [testing_id], description = "Ask the magic 8ball a question")
    async def ask(
        self, interaction : Interaction, *, 
        question: str = SlashOption(description = "Ask a question", required = True)
    ):

        responses = [
            "It is certain.", "It is decidedly so.", "Without a doubt.",
            "Yes - definitely.", "You may rely on it.", "As I see it, yes.",
            "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.",
            "Reply hazy, try again.", "Ask again later.",
            "Better not tell you now.", "Cannot predict now.",
            "Concentrate and ask again.", "Don't count on it.",
            "My reply is no.", "My sources say no.", "Outlook not so good.",
            "Very doubtful."
        ]

        embed = nextcord.Embed(
            title = "🎱 8ball says...",
            color = nextcord.Color.random()
        )

        embed.add_field(
            name = "Question", 
            value = f"{question}", 
            inline = "false"
        )

        embed.add_field(
            name = "Answer",
            value = f"{random.choice(responses)}",
            inline = "false"
        )

        embed.set_thumbnail(
            url = "https://cdn.discordapp.com/attachments/943924201688027206/1055761355887616070/1f3b1.png"
        )

        await interaction.send(embed=embed)

def setup(bot):
    bot.add_cog(Ask(bot))