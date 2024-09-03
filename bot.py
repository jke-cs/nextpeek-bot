import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True  # Enable members intent

bot = commands.Bot(command_prefix='!', intents=intents)

# Define the channel ID where the bot will send the initial message
channel_id = 1280518715506557003  # Replace this with the actual channel ID

# Define the roles and their corresponding reactions
roles = {
    '🇩🇪': 1280526518191390814,  # Germany - Replace with the actual role ID
    '🇦🇹': 1280526394262028390,  # Austria - Replace with the actual role ID
    '🇨🇭': 1280526674814832754,  # Switzerland - Replace with the actual role ID
    '🇸🇪': 1280526708239503411,  # Sweden - Replace with the actual role ID
    '🇩🇰': 1280527088511750144,  # Denmark - Replace with the actual role ID
    '🇧🇪': 1280526745400905728,  # Belgium - Replace with the actual role ID
    '🇧🇬': 1280526796038733875,  # Bulgaria - Replace with the actual role ID
    '🇨🇿': 1280527039971070134,  # Czech Republic - Replace with the actual role ID
    '🇫🇮': 1280527180476055603,  # Finland - Replace with the actual role ID
    '🇫🇷': 1280527261862330399,  # France - Replace with the actual role ID
    '🇭🇺': 1280527269999411342,  # Hungary - Replace with the actual role ID
    '🇮🇪': 1280527271014305906,  # Ireland - Replace with the actual role ID
    '🇳🇱': 1280527532529029171,  # Netherlands - Replace with the actual role ID
    '🇵🇱': 1280527558122930287,  # Poland - Replace with the actual role ID
    '🇵🇹': 1280527556239556719,  # Portugal - Replace with the actual role ID
    '🇷🇴': 1280527556759785562,  # Romania - Replace with the actual role ID
    '🇸🇰': 1280527557388669034,  # Slovakia - Replace with the actual role ID
    '🇸🇮': 1280527816613691402,  # Slovenia - Replace with the actual role ID
    '🇪🇸': 1280527817322270832,  # Spain - Replace with the actual role ID
    '🇬🇧': 1280527820296028181   # Great Britain - Replace with the actual role ID
}

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    channel = bot.get_channel(channel_id)
    if channel:
        await channel.send("@everyone")
        embed = discord.Embed(
            title="🌍 Where are you from?",
            description="React with the corresponding flag to select your country!\n\n"
                        + "\n".join([f"{emoji} - {role_mention}" 
                                      for emoji, role_id in roles.items()
                                      if (role := channel.guild.get_role(role_id))
                                      for role_mention in [f"<@&{role_id}>"]]), 
            color=discord.Color.blue()
        )
        message = await channel.send(embed=embed)
        for reaction in roles.keys():
            await message.add_reaction(reaction)
    else:
        print("Channel not found.")

@bot.event
async def on_reaction_add(reaction, user):
    if user.bot:
        return
    if reaction.message.channel.id == channel_id:
        role_id = roles.get(str(reaction.emoji))
        if role_id:
            role = reaction.message.guild.get_role(role_id)
            if role:
                await user.add_roles(role)
                await reaction.message.channel.send(f'{user.mention} has been assigned the {role.name} role!')
            else:
                print(f'Role with ID {role_id} not found.')
        else:
            print(f'No role associated with {str(reaction.emoji)}.')

bot.run('YOUR_BOT_TOKEN')  # https://discord.com/developers/applications/ Replace with your actual bot token
