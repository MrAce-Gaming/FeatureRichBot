import discord
import config
import aiohttp
import time
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=">", intents=intents)
async def automodFilter(guild):
    try:
        trigger = discord.AutoModTrigger(
            type=discord.AutoModRuleTriggerType.keyword,
            keyword_filter=discord.AutoModPresets(
                sexual_content=True,
                slurs=True,
                profanity=True
            )
        )
        action = discord.AutoModRuleAction(
            type=discord.AutoModRuleActionType.block_message 
        )

        rule = discord.AutoModRule(
            id=1,
            name="Filter",
            trigger=trigger,
            enabled=True,
            event_type=discord.AutoModRuleEventType.message_send,
            actions=[action] 
        )
        await guild.automodFilter(rule)
    except Exception as e:
        print(f"Failed to create AutoModRule: {e}")

@bot.event
async def on_ready():
    print(f"Bot is available, {bot.user}")
    await bot.tree.sync()

@bot.event
async def on_message(msg: discord.Message):
    content = msg.content
    print(content)

    guild = msg.guild
    if guild:
        await automodFilter(guild)
@bot.command()
async def welcome(ctx):
    await ctx.send("Thanks!")

@bot.tree.command()
async def hello(interaction:    discord.Interaction):
    await interaction.response.send_message("Hello bro!")

bot.run(config.DISCORD_TOKEN)
