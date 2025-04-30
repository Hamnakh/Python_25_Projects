import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get the bot token from the environment
TOKEN = os.getenv('DISCORD_TOKEN')

# Check if token is found
if not TOKEN:
    raise ValueError("No token found. Please make sure you have a valid .env file with the DISCORD_TOKEN set.")

# Bot configuration
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    print('Bot is ready to use!')

@bot.command(name='hello')
async def hello(ctx):
    await ctx.send(f'Hello {ctx.author.name}! 👋')

@bot.command(name='ping')
async def ping(ctx):
    latency = round(bot.latency * 1000)
    await ctx.send(f'Pong! Latency: {latency}ms')

@bot.command(name='helpme')
async def helpme(ctx):
    await ctx.send("Here are the commands you can use: !hello, !ping, !info")

@bot.command(name='joke')
async def joke(ctx):
    await ctx.send("Why did the Python developer go broke? Because he used up all his cache. 😅")


@bot.command(name='info')
async def info(ctx):
    embed = discord.Embed(
        title="Bot Information",
        description="A simple Discord bot created with Python",
        color=discord.Color.blue()
    )
    embed.add_field(name="Bot Name", value=bot.user.name, inline=True)
    embed.add_field(name="Bot ID", value=bot.user.id, inline=True)
    embed.add_field(name="Server Count", value=len(bot.guilds), inline=True)
    await ctx.send(embed=embed)

# Run the bot
bot.run(TOKEN)
