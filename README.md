このコードはRenderで動かすDiscord BotのコードをChatGPTに書いてもらったものです。

# DiscoMine-Botとは
Discord Botに統合版のminecraftのユーザーIDをDMしそのユーザーのXuidを検索し、出力されたxuidをもう一度検索し出てきたユーザーIDと送られてきたユーザーIDが同じものと分かればDiscord内でロールを付与するためのコードです。

# 参考にしたサイト
誰でも作れる！Discord Bot 2024（初期設定編）
https://note.com/exteoi/n/n00342a623c93#cbc9e24f-6483-49dc-be95-36f6a73b3d5a

# Renderでの設定
### 1. ダッシュボード
New を押しWeb Service を選択
### 2. GitHubとの連携
Public Git Repository を選択しこのリポジトリのURLを追加
### 3. Build Command
Build Command に``pip install -r requirements.txt``と打ち込む
### 4. Start Command
Start Command に``python bot.py``
### 5. プランを選択
Free Plan を選択
### 6. トークンやサーバーの設定
デプロイ後、Environment タブで次を追加

  ``DISCORD_TOKEN``  → Bot トークン
  
  ``DISCORD_GUILD_ID``  → サーバーID
  
  ``DISCORD_ROLE_ID``  → ロールID

  ``PYTHON_VERSION``  → ``3.11.9``
### 7. セーブ&デプロイ
Advanced を開きAuto-Deploy を``On Commit``にする

その後に``Deploy web service``を押す

# その他とその後
何か直す必要があったらAIに聞くかDiscordにてDMしてください

Discordはプロフィールにリンクがあります
