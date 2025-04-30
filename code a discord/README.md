# Discord Bot

A simple Discord bot created with Python that can be hosted for free.

## Features

- `!hello` - Greets the user
- `!ping` - Shows bot latency
- `!info` - Displays bot information

## Setup Instructions

1. Create a new Discord application and bot at [Discord Developer Portal](https://discord.com/developers/applications)
2. Get your bot token from the Discord Developer Portal
3. Create a `.env` file in the root directory and add your bot token:
   ```
   DISCORD_TOKEN=your_bot_token_here
   ```
4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
5. Run the bot:
   ```
   python bot.py
   ```

## Hosting on Replit

1. Create a new Repl and import this repository
2. Add your Discord bot token to Replit's Secrets:
   - Click on "Tools" in the left sidebar
   - Select "Secrets"
   - Add a new secret with key `DISCORD_TOKEN` and your bot token as the value
3. Click "Run" to start the bot

## Commands

- `!hello` - The bot will greet you
- `!ping` - Check the bot's latency
- `!info` - Get information about the bot

## Requirements

- Python 3.8 or higher
- discord.py
- python-dotenv 