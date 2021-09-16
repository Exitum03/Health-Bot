from discord.ext import commands
import os

bot = commands.Bot(command_prefix="-")
token = "ODgyNDY2NTg2Njc2NTYzOTg4.YS7zDQ.BPB7gt8JL0COQcIMNFxLZV-VhW4"


# used to load unloaded cogs while the bot is running
@bot.command()
async def load(ctx, extension):
    bot.load_extension(f"cogs.{extension}")
    await ctx.send(f"{extension} has been loaded")


@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f"cogs.{extension}")
    await ctx.send(f"{extension} has been unloaded")


@bot.command()
async def reload(ctx, extension):
    bot.unload_extension(f"cogs.{extension}")
    bot.load_extension(f"cogs.{extension}")
    await ctx.send(f"{extension} has been reloaded")


# loads the cogs when the bot is up
for files in os.listdir("./cogs"):
    if files.endswith(".py"):
        bot.load_extension(f"cogs.{files[:-3]}")


bot.run(token)
