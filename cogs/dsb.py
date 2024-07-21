from pydsb import PyDSB
import datetime
import json
import asyncio
from discord.ext import commands, tasks
from dotenv import load_dotenv
import os

load_dotenv()

async def post(self, plan, datum):
    guild = self.bot.get_guild(810089469314990101)
    channel = guild.get_channel(1113094794558836846)
    await channel.send(f"__**Neuer Vertretungsplan vom {datum}**__\n<@&1022186035301589094>\n{plan['url']}")

async def in_json_eintragen(self, datum, daten):
    with open("vertretungsplan.json", "r") as f:
        data = json.load(f)
    try:
        data[datum]
        if data[datum]["uploaded_date"] != daten["uploaded_date"]:
            await post(self, daten, datum)
            data[datum] = daten
        else:
            pass
        
    except:
        await post(self, daten, datum)
        data[datum] = daten


    with open("vertretungsplan.json", "w") as f:
        json.dump(data, f, indent=4)

class dsbmobile(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def cog_load(self):
        self.banner_update.start()
        
    def cog_unload(self):
        self.banner_update.cancel()
        
    @tasks.loop(seconds=10)
    async def banner_update(self):
        now = datetime.datetime.now()
        formatted_date = now.strftime("%d_%m")
        tomorrow = (now + datetime.timedelta(days=1)).strftime("%d_%m")
        full_date = now.strftime("%d_%m_%y")
        full_date_2 = (now + datetime.timedelta(days=1)).strftime("%d_%m_%y")
        dsb = PyDSB(os.getenv("user"), os.getenv("pswd"))
        plans = dsb.get_plans()

        for plan in plans:
            if f"VPSch{formatted_date}" == plan["title"]:
                await in_json_eintragen(self, full_date, plan)
                await asyncio.sleep(5)
            if f"VPSch{tomorrow}" == plan["title"]:
                await in_json_eintragen(self, full_date_2, plan)
                await asyncio.sleep(5)

async def setup(bot):
    await bot.add_cog(dsbmobile(bot))