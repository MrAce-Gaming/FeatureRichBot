import discord
import config
from discord.ext import commands

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
async def ban(ctx, user:    discord.Member, reason=None):
    if user is None:
        await ctx.send("You can't ban no one")
    else:
        await ctx.guild.ban(user, reason=reason)
        await ctx.send(f"{user} was banned, Reason: {reason}")

@bot.command()
async def unban(ctx, user:  discord.User, reason=None):
    if user is None:
        await ctx.send("Are you trying to unban air?")
    else:
        await ctx.guild.unban(user, reason=reason)
        await ctx.send(f"{user} has been unbanned, Reason: {reason}")

@bot.command()
async def kick(ctx, user:   discord.Member, reason=None):
    if user is None:
        await ctx.send("You cant kick no one")
    else:
        await ctx.guild.kick(user, reason=reason)
        await ctx.send(f"{user} was kicked, Reason: {reason}")

@bot.command()
async def mute(ctx, user:   discord.Member, reason=None):
    if user is None:
        await ctx.send("Bro really be trying to mute air")
    else:
        await ctx.send("hmm")

bot.run(config.DISCORD_TOKEN)