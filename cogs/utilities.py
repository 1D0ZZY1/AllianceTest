import sqlite3
from disnake.ext import commands

database = sqlite3.connect('server.db')
cursor = database.cursor()


class Utilities(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        cursor.execute("""CREATE TABLE IF NOT EXISTS profile (
            id BIGINT,
            member TEXT,
            nickname TEXT,
            realistic_events TEXT,
            regiment TEXT
        )""")

        cursor.execute("CREATE TABLE IF NOT EXISTS blacklist (id BIGINT, reason TEXT)")


def setup(bot):
    bot.add_cog(Utilities(bot))
