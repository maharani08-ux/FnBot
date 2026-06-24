import discord
from discord.ext import commands
import json
import os
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot online sebagai {bot.user}")

@bot.command()
async def setlagu(ctx, music_id: str):
    with open("music.json", "w") as f:
        json.dump({"music_id": music_id}, f)
    await ctx.send(f"✅ Lagu diganti ke ID: {music_id}")

bot.run(os.getenv("DISCORD_TOKEN"))