# this is just a test bot that I use for testing new features
import sys
sys.path.append(".")
from discord.ext import commands
from src import dpycheck
import discord
import asyncio

# setup bot instance
class Bot(commands.Bot):
    def __init__(self) -> None:
        super().__init__("!", intents=discord.Intents.all())
bot = Bot()
@bot.event
async def on_ready() -> None:
    print("BOT IS READY")

# setup error handler
class Formatter(dpycheck.Formatter):
    def custom_MaxConcurrencyReached(self, exc: commands.MaxConcurrencyReached) -> str:
        return "You must wait for the command to complete before running it again."
error_handler = dpycheck.ErrorHandler(
    [
        [
            1058192427049037874
        ]
    ],
    formatter=Formatter()
)


@bot.command("test")
@commands.max_concurrency(1, commands.BucketType.user, wait=False)
async def test(ctx: commands.Context) -> None:
    exc = ValueError()
    dpycheck.ErrorHandler.set_additional(
        exc,
        {"title": "embed (dict)", "description": "desc"},
        discord.Embed(title="embed (embed)", description="desc"),
        "string",
        ctx.message.attachments[0],
        ValueError("1 + 1 does NOT equal 3 >:(")
    )
    raise exc
test.on_error = error_handler.error

# run bot
with open("tests/token.txt", "r") as token:
    bot.run(token.read())
