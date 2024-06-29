import datetime
import discord
import config
from discord.ext import commands
from datetime import timedelta

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot is available, {bot.user}")
    await bot.tree.sync()

@bot.event
async def on_message(msg: discord.Message):
    message = msg.content
    if "kys" == message:
        await msg.reply("yeah bro go kill yourself da fuq")
    if "mrace" == message:
        await msg.reply("mrace more like mrass")
    if "scarry" == message:
        await msg.reply("bro got the most high end pc known to mankind")
    if "sam" == message:
        await msg.reply("let HIM COOK!")
    await bot.process_commands(msg)

@bot.tree.command()
async def welcome(interaction:    discord.Interaction):
    await interaction.response.send_message("Thanks!")

@bot.tree.command()
async def hello(interaction:    discord.Interaction):
    await interaction.response.send_message("Hello bro!")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

@bot.command()
async def ban(ctx, user:    discord.User, reason=None):
    if user is None:
        await ctx.send("You can't ban no one")
    else:
        await ctx.guild.ban(user, reason=reason)
        _ban_ = discord.Embed(title="BAN command initiation", description=(f"{user} was banned, Reason: {reason}"), color=0xFEE75C)
        await ctx.send(embed=_ban_)

@bot.command()
async def unban(ctx, user:  discord.User, reason=None):
    if user is None:
        await ctx.send("Are you trying to unban air?")
    else:
        await ctx.guild.unban(user, reason=reason)
        _unban_ = discord.Embed(title="UNBAN command initiation", description=(f"{user} was unbanned, Reason: {reason}"), color=0xFEE75C)
        await ctx.send(embed=_unban_)

@bot.command()
async def kick(ctx, user:   discord.Member, reason=None):
    if user is None:
        await ctx.send("You cant kick no one")
    else:
        await ctx.guild.kick(user, reason=reason)
        _kick_ = discord.Embed(title="KICK command initiation", description=(f"{user} was kicked, Reason: {reason}"), color=0xFEE75C)
        await ctx.send(embed=_kick_)

@bot.command()
async def timeout(ctx, user:   discord.Member, time: int, reason=None):
    if user is None:
        await ctx.send("Bro really be trying to timeout air")
    else:
        await user.timeout(datetime.timedelta(seconds=time), reason=reason)
        _timeout_ = discord.Embed(title="TIMEOUT command initiation", description=(f"{user} was timeouted for {time} seconds, Reason: {reason}"), color=0xFEE75C)
        await ctx.send(embed=_timeout_)

bot.run(config.DISCORD_TOKEN)