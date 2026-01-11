import os
import requests
import discord
from discord.ext import commands

DISCORD_TOKEN = os.environ["DISCORD_TOKEN"]
ROBLOX_API_KEY = os.environ["ROBLOX_API_KEY"]

UNIVERSE_ID = "7221342074"
TOPIC = "AC"

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")


@bot.command(name="robloxmsg")
async def send_roblox_message(ctx, message: str):
    """
    Usage:
    !robloxmsg 86400
    """

    url = f"https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}:publishMessage"

    headers = {
        "x-api-key": ROBLOX_API_KEY,
        "Content-Type": "application/json"
    }

    payload = {
        "topic": TOPIC,
        "message": message
    }

    await ctx.send("📡 Sending message to Roblox...")

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=10)

        if response.status_code == 200:
            await ctx.send("✅ **Message sent to Roblox!**")
        else:
            await ctx.send(
                f"❌ **Roblox API Error**\n"
                f"Status: `{response.status_code}`\n"
                f"Response: ```{response.text}```"
            )

    except requests.exceptions.RequestException as e:
        await ctx.send(f"🌐 **Connection error:** `{e}`")


bot.run(DISCORD_TOKEN)
