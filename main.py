import discord
import os
import requests
import random
import json
from replit import db

client = discord.Client()

creatures = [
	"Dragon",
	"Ogre",
	"Hydra",
	"Snake",
	"Tiki monster",
	"Yeti"
]

weapons = list([
	"sword",
	"shield"
])

def add_currency(message):
  print(str(message.author.name))

  if(str(message.author.name) in db.keys()):
    value = db[str(message.author.name)]
    print(db[message.author.name])
    db[str(message.author.name)] = str(int(value) + 10)
    print(12345)
  else:
    db[str(message.author.name)] = str(message.author.name)
    db[message.author.name] = str(10)
    print(54321)

  print(db[str(message.author.name)])

def check_currency(message):
	return ("You have " + db[str(message.author.name)] + " currency!")

def get_meme():
  response = requests.get('https://meme-api.herokuapp.com/gimme/cleanmemes')
  json_data = json.loads(response.text)
  return(json_data['url'])

@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
	msg = message.content
	cur = '$cur'
	add_currency(message)

	if message.author == client.user:
		return

	if msg.startswith(cur) and msg.endswith('gain'):
		await message.channel.send('You gained 10 currency!')

	if msg.startswith(cur) and msg.endswith('meme'):
		await message.channel.send(get_meme())

	if msg.startswith(cur) and msg.endswith('fight monster'):
		await message.channel.send(random.choice(creatures))

	if msg.startswith(cur) and msg.endswith('shop'):
		await message.channel.send(weapons)

	if msg.startswith(cur) and msg.endswith('inventory'):
		await message.channel.send(check_currency(message))

	if msg.startswith(cur) and msg.endswith('help'):
		await message.channel.send('.cur gain: gain currency\n.cur meme: post a meme\n.cur fight monster: still working on this\n.cur shop: shows weapons\n.cur inventory: shows your currency')
		
client.run(os.getenv('TOKEN'))