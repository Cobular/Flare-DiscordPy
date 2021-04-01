import os

from discord.ext.commands import Bot
from Flare import Flare

bot = Bot("~~")

bot.add_cog(Flare(bot))


@bot.command("ping")
async def ping_pong(ctx):
    ctx.send("pong")


bot.run(os.environ.get("BOT_TOKEN"))
