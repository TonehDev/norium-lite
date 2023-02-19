import nextcord
from nextcord.ext import commands, application_checks
import os
from nextcord.ui import Button
from nextcord import Interaction, SlashOption, ChannelType
from nextcord.abc import GuildChannel
import time
import datetime

intents = nextcord.Intents.default()
intents.members = True
bot = commands.Bot(case_insensitive = True, intents = intents)
bot.remove_command("help")
test = "some random server id" ### remove this only if you want to add global commands, however it is recommended that you limit the usage of slash commands to only one server for the purpose of testing

### EVENTS

@bot.event
async def on_ready():
    global startTime
    startTime = time.time()
    await bot.change_presence(activity = nextcord.Game(name = f"in {len(bot.guilds)} servers | /help"))
    print("Norium is ready")

### COMMANDS

@bot.slash_command(guild_ids = [test], description = "A quick overview of all commands")
async def help(
        interaction : Interaction
    ):

    support = Button(
        label = "Your support server",
        url = "https://discord.gg/idklol"
    )

    website = Button(
        label = "Your website", 
        url = "https://google.com/"
    )

    view = HelpDropView()
    view.add_item(support)
    view.add_item(website)

    embed = nextcord.Embed(
        title = "Help menu", 
        color = nextcord.Color.blurple()
    )

    embed.add_field(
        name = "Navigating", value="Choose something from the dropdown below."
    )

    await interaction.send(embed=embed, view=view)



class HelpDrop(nextcord.ui.Select):
    def __init__(self):
        selectOptions = [
            nextcord.SelectOption(
                label = "Fun", 
                description = "Displays all fun features", 
                emoji = "🎮"
            ),
            nextcord.SelectOption(
                label = "Utility", 
                description = "Displays all utility features", 
                emoji = "🔨"
            ),
            nextcord.SelectOption(
                label = "Home",
                description = "Go back to the original page",
                emoji = "🏠"
            )
        ]

        super().__init__(
            placeholder = 'Select a category',
            min_values = 1, max_values = 1, options = selectOptions
        )

    async def callback(
        self, interaction : Interaction
    ):

        if self.values[0] == 'Utility':
            embed = nextcord.Embed(
                title = "Utility Plugin",
                description = "``<> Required\n[] Optional``",
                color = nextcord.Color.blurple()
            )
            embed.add_field(
                name = "``/help``",
                value = "A quick overview of all commands"
            )
            embed.add_field(
                name = "``/embed <title> <description>``",
                value = "Build an embed"
            )
            embed.add_field(
                name = "``/profile @[member]``",
                value = "Sends your or another user's profile")
            embed.add_field(
                name = "``/avatar @[member]``",
                value = "Returns your profile picture"
            )
            await interaction.edit(
                embed = embed
            )

        if self.values[0] == 'Fun':
                embed = nextcord.Embed(
                    title = "Fun Plugin",
                    description="``<> Required``\n``[] Optional``",
                    color = nextcord.Color.blurple()
                )
                embed.add_field(
                    name = "``/bunger``", 
                    value = "Bunger"
                )
                embed.add_field(
                    name = "``/ask <question>``",
                    value = "Ask the magic 8ball a question"
                )
                embed.add_field(
                    name = "``/gayrate @[member]``",
                    value = "Accurately measures gay rate"
                )
                embed.add_field(
                    name = "``/eggcat``", 
                    value = "Oh the misery"
                )
                await interaction.edit(
                    embed = embed
                )

        if self.values[0] == 'Home':
            support = Button(
                label = "Your support server",
                url = "https://discord.gg/2xzfZtAKMf"
            )

            website = Button(
                label = "Your website", 
                url = "https://noriumbot.com/"
            )

            view = HelpDropView()
            view.add_item(support)
            view.add_item(website)

            embed = nextcord.Embed(
                title = "Help menu", 
                color = nextcord.Color.blurple()
            )

            embed.add_field(
                name = "Navigating",
                value = "Choose something from the dropdown below."
            )

            await interaction.edit(
                embed = embed, 
                view = view
            )    
    

class HelpDropView(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(HelpDrop())

@bot.slash_command(guild_ids = [test], description = "[OWNER ONLY] Sets the status") # restarting will reset the status to its origin
@application_checks.is_owner()
async def setstatus(
    interaction : Interaction, 
    playing: str = SlashOption(description = "Set a status")
): # playing has to be a string

    embed = nextcord.Embed(
        title = "Status is now set (Playing)",
        description = f"Status is now set to ```PLAYING {playing}```",
        color = nextcord.Color.blurple()
    )

    await interaction.send(embed = embed) # sends the embed

    await bot.change_presence(activity = nextcord.Game(name = f"{playing}")) # changes the status

for filename in os.listdir('./commands'):
    if filename.endswith('.py'):
        bot.load_extension(f'commands.{filename[:-3]}')

bot.run("insert your token in here")