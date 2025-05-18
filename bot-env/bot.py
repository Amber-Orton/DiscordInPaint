import discord
import config
import storage

def create_bot():
    # retreive information from the config file
    global BOT_TOKEN
    global DB_LOCATION
    config.init()
    BOT_TOKEN = config.BOT_TOKEN
    DB_LOCATION = config.DB_LOCATION

    # setup discord bot intents
    intents = discord.Intents.default()
    intents.message_content = True
    intents.messages = True

    # create the bot client
    client = InPaintClient(intents=intents)
    client.run(BOT_TOKEN)
    return client


class InPaintClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user}')


    #when reciving a message
    async def on_message(self, message):
        if message.author == self.user:
            return

        print(f'Message from {message.author}: {message.content}')

        channel = message.channel
        async for msg in channel.history(limit=10):
            print(f'History - {msg.author}: {msg.content}')
        
        await channel.send(f'Hello {message.author.name}, you said: {message.content}')