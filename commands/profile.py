import nextcord
from nextcord.ext import commands
from nextcord import Interaction, SlashOption

class Profile(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 

    testing_id = "some random server id"

    @nextcord.slash_command(guild_ids = [testing_id], description = "Sends your or another user's user profile")
    async def profile(
        self, interaction : Interaction, 
        member : nextcord.Member = SlashOption(description = "The member you want to view the profile of", required = False)
    ):

        if member is None:
            member = interaction.user 

        roles = [role for role in member.roles]

        embed = nextcord.Embed(
            title = f"{member.name}#{member.discriminator}'s Profile",
            color = member.color
        )

        embed.set_thumbnail(
            url = member.avatar.url
        )

        embed.add_field(
            name = "ID", 
            value = member.id
        )

        embed.add_field(
            name = "Nickname", 
            value = member.display_name
        )

        embed.add_field(
            name = "Created at", 
            value = member.created_at.strftime("%a, %#d, %B %Y, %I:%M %p UTC")
        )

        embed.add_field(
            name = "Joined at", 
            value = member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC")
        )

        embed.add_field(
            name = f"Roles ({len(roles)})", 
            value = " ".join([role.mention for role in roles])
        )

        embed.add_field(
            name = "Highest priority", 
            value = member.top_role.mention
        )

        embed.add_field(
            name = "Is Bot", 
            value = member.bot
        )

        embed.add_field(
            name = "Avatar URL", 
            value = f"[Click here]({member.avatar.url})"
        )

        await interaction.response.send_message(
            embed = embed
        )

    @nextcord.slash_command(guild_ids = [testing_id], description = "Returns your profile picture")
    async def avatar(
        self, interaction : Interaction, 
        member : nextcord.Member = SlashOption(description = "A member you want to view the avatar of", required = False)
    ):

        if member is None:
            member = interaction.user

        embed = nextcord.Embed(
            title = f"Avatar for {member.name}#{member.discriminator}", 
            description = f"[Avatar URL]({member.avatar.url})", 
            color = nextcord.Color.blurple()
        )

        embed.set_image(
            url = member.avatar.url
        )

        await interaction.response.send_message(
            embed = embed
        )

def setup(bot):
    bot.add_cog(Profile(bot))