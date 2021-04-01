import os

from aiohttp import web
from discord.ext import commands, tasks


class Flare(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot
        self.web_server.start()
        self.app = web.Application()
        self.routes = web.RouteTableDef()

        @self.routes.get(os.environ.get('FLARE_PATH', "/"))
        async def welcome(request):
            return web.Response(text="Bot is Online!!")

        self.webserver_port = os.environ.get('FLARE_PORT', 5000)
        self.app.add_routes(self.routes)

    @tasks.loop()
    async def web_server(self):
        runner = web.AppRunner(self.app)
        await runner.setup()
        site = web.TCPSite(runner, host=os.environ.get("FLARE_HOST", None), port=self.webserver_port)
        await site.start()

    @web_server.before_loop
    async def web_server_before_loop(self):
        await self.bot.wait_until_ready()
