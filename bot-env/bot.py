import discord
import bot_token
import storage

# retreive bot token from the bot token file
global BOT_TOKEN
bot_token.init()
BOT_TOKEN = bot_token.BOT_TOKEN

# setup discord bot intents
intents = discord.Intents.default()
intents.message_content = True
intents.messages = True



class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user}')






    #TODO: work out how to interface with paint lol


    #when reciving a message
    async def on_message(self, message):
        if message.author == self.user:
            return

        print(f'Message from {message.author}: {message.content}')

        channel = message.channel
        async for msg in channel.history(limit=10):
            print(f'History - {msg.author}: {msg.content}')
        
        await channel.send(f'Hello {message.author.name}, you said: {message.content}')

client = MyClient(intents=intents)
client.run(BOT_TOKEN)