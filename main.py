import os
import disnake
from disnake.ext import commands

intents = disnake.Intents().all()
bot = commands.Bot(command_prefix='!', test_guilds=[981965725092679760], sync_commands_debug=True, intents=intents)

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")

token = "OTgyMDMzMjQ4OTA3NTg3NjM0.Gq8jIw.N4L45A31EQYP66yHx1X1-yJfcASk9lWfalITlU"
bot.run(token)
