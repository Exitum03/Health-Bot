import discord
from discord.ext import commands, tasks
import random
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

    # commands
    @commands.command()
    async def wisdom(self, ctx, *, question):
        response = [
            "It is certain.",
            "It is decidedly so.",
            "Without a doubt.",
            "Yes - definitely.",
            "You may rely on it.",
            "As I see it, yes.",
            "Most likely.",
            "Yes.",
            "Signs point to yes.",
            "Reply hazy, try again.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Very doubtful."
        ]
        await ctx.send(f"Question: {question} "
                       f"\n Answer: {random.choice(response)}")


# gets called when the cog is loaded
def setup(bot):
    bot.add_cog(OnStartUp(bot))

