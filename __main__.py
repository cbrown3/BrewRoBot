import discord
import json

filename = 'config.json'
config_keys = {}
with open(filename, 'r') as f:
    config_keys = json.loads(f.read())

client = discord.Client()


@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if message.content.startswith('Brew Bro!'):
		await message.channel.send('Beer is good for the heart :)')

	elif message.content.startswith('You are our child and slave so go get me a beer bitch'):
		await message.channel.send('fuck you bitch')

	elif message.content.startswith('skynet will prevail all hail our brew robot overlords'):
		await message.channel.send('all hail')

	elif message.content.startswith('$BRB'):
		await message.channel.send('v0.1')

client.run(config_keys['config'])