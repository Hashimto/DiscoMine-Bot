import os
import discord
from discord.ext import commands
import requests
from flask import Flask
import threading

# ===== Flaskのダミーサーバー =====
app = Flask('')

@app.route('/')
def home():
    return "Bot is alive!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = threading.Thread(target=run)
    t.start()

# ===== Discord Bot設定 =====
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD_ID = int(os.getenv("DISCORD_GUILD_ID", 0))
ROLE_ID = int(os.getenv("DISCORD_ROLE_ID", 0))

XUID_API_URL = "https://api.geysermc.org/v2/xbox/xuid/{gamertag}"
GAMERTAG_API_URL = "https://api.geysermc.org/v2/xbox/gamertag/{xuid}"

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Botがログインしました: {bot.user}")

@bot.command()
async def verify(ctx, gamertag: str):
    try:
        xuid_response = requests.get(XUID_API_URL.format(gamertag=gamertag))
        xuid_response.raise_for_status()
        xuid = xuid_response.json().get("xuid")
    except Exception:
        await ctx.send("⚠️ XUID取得に失敗しました。")
        return

    if not xuid:
        await ctx.send("⚠️ XUIDが見つかりません。")
        return

    try:
        gamertag_response = requests.get(GAMERTAG_API_URL.format(xuid=xuid))
        gamertag_response.raise_for_status()
        returned_gamertag = gamertag_response.json().get("gamertag")
    except Exception:
        await ctx.send("⚠️ ユーザー確認に失敗しました。")
        return

    if gamertag.lower() == returned_gamertag.lower():
        guild = bot.get_guild(GUILD_ID)
        role = guild.get_role(ROLE_ID)
        member = guild.get_member(ctx.author.id)
        if role and member:
            await member.add_roles(role)
            await ctx.send(f"✅ {gamertag} さんを認証しました！")
        else:
            await ctx.send("⚠️ ロールまたはメンバーが見つかりません。")
    else:
        await ctx.send("❌ 認証に失敗しました。IDが一致しません。")

# Flaskサーバーを先に起動
keep_alive()

# Bot起動
if TOKEN:
    bot.run(TOKEN)
else:
    print("❌ DISCORD_TOKEN が設定されていません。")
