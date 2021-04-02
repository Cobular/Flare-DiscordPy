<h1 align="center"><img src="https://github.com/JakeCover/Flare-DiscordPy/blob/main/flare_logo.png" width=24> Flare</h1>

<p align="center">An easy-to-use, dead-simple cog to add a tiny, simple, fast webpage to your bot in order to enable uptime monitoring with something like UptimeRobot.</p>

Heavily inspired from this StackOverflow answer: https://stackoverflow.com/a/62481294/5623598. Thanks random internet person!!


## Usage
Simply install the cog with `pip install flare` and then import it: `from Flare import Flare`. Finally, load the cog with `bot.add_cog(Flare(bot))` and you're off to the races!!

Take a look at http://localhost:5000/ to see the bot's status page. 

#### Example
For an example implementation, take a look at `example_bot/bot.py`, where there is a minimum viable bot implementing this page.


## Configuration
The cog has three env vars, but the defaults work fine for a plug and play setup. If you want to change them, here's what you need to know:
  * `FLARE_PORT` is the port the webserver is exposed on, and it defaults to 5000. Set it to any number to change the port to your heart's desire.
  * `FLARE_PATH` is the path to the page. This defaults to `/`, but you can change it with this var to whatever you choose.
  * `FLARE_HOST` is the host to listen on, defaults to `None` which in this case means all interfaces. You can set it to a specific IP if you would like to change this configuration.
