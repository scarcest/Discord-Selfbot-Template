v = 1.0

import discord, requests, json, subprocess, os, time, sys
from discord.ext import(
	commands,
	tasks
)
from colorama import Fore

with open("config.json") as f:
	config = json.load(f)

token = config.get("token")
prefix = config.get("prefix")

knife = discord.Client()
knife = commands.Bot(
	self_bot=True,
	command_prefix=prefix
)
knife.remove_command("help")

def clear():
	os.system("clear")

def initial():
	clear()
	if token == "token-here":
		print(Fore.RED+"[error]"+Fore.WHITE+" you didn't put your token in the config file")
		sys.exit()
	else:
		knife.run(token, bot=False, reconnect=True)


def banner():
	clear()
	r = Fore.RED
	w = Fore.WHITE
	g = Fore.GREEN
	print(f''' 
									{r}Knife{w} Selfbot v{v} {r}|{w} Logged in as: {knife.user.name}{r}#{w}{knife.user.discriminator}{r} |{w} ID:{w} {knife.user.id}{w}
									Prefix: {r}{prefix}

		''')



@knife.event
async def on_connect():
	banner()

@knife.command()
async def help(ctx):
	await ctx.message.delete()
	em = discord.Embed(title=f"Knife v{v}", color=0x000000, timestamp=ctx.message.created_at, description=f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n>`{prefix}help - displays this msg`\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
	em.set_footer(text=f"Knife v{v}")
	em.set_image(url="https://cdn.discordapp.com/attachments/785521893766856755/797306975221579785/350kb.gif")
	await ctx.send(embed=em)

initial()