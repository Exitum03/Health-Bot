import discord
from discord.ext import commands, tasks
from itertools import cycle


class OnStartUp(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.status = cycle(["Stay healthy", f"{self.bot.command_prefix}help"])

    # events
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.bot.user} is ready")
        self.change_status.start()

    # background task
    @tasks.loop(seconds=10)
    async def change_status(self):
        await self.bot.change_presence(activity=discord.Game(next(self.status)))


# gets called when the cog is loaded
def setup(bot):
    bot.add_cog(OnStartUp(bot))

