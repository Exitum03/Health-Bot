from discord.ext import commands
import main


class ErrorHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # error handler
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        # handles the loading, unloading, and reloading errors
        if isinstance(error, commands.errors.CommandInvokeError):
            await ctx.send("Cog does not exist! Try again.")
        # commands that doesn't exist
        elif isinstance(error, commands.errors.CommandNotFound):
            await ctx.send(f"Command does not exist. Enter \"{self.bot.command_prefix}help\" for the list of the commands")


def setup(bot):
    bot.add_cog(ErrorHandler(bot))
