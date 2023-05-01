import discord
import requests
import logging
import json

logging.basicConfig(level=logging.INFO)

with open('config.json', 'r') as file:
    config = json.load(file)


def random_quote():
    # make GET request to the API
    response = requests.get('https://www.archerapi.com/api/quotes/random', data={'key': 'value'})
    # extract 'quote' from the response 
    data = response.json()
    quote = data.get('quote')
    return quote

# Define the list of trigger words
trigger_words = ['hello', 'hi', 'hey']

# Define the Discord client
intents = discord.Intents.default()  # Enable the default intents
intents.messages = True
intents.message_content = True

client = discord.Client(intents=intents)

# Event handler for when the bot is ready
@client.event
async def on_ready():
    print('Bot is ready.')

# Event handler for when a message is received
@client.event
async def on_message(message):
    # Ignore messages sent by the bot itself
    if message.author == client.user:
        return

    # Check if any of the trigger words are in the message content
    for word in trigger_words:
        if word in message.content.lower().split():
            # Send a reply message
            await message.channel.send(random_quote())
            return

# Run the bot
client.run(config['bot_token'])