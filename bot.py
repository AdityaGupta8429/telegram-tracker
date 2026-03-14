from telethon import TelegramClient, events
import requests
import asyncio

api_id = 28813625
api_hash = "792c04f8813f429d387ec93ba1a6332d"

bot_token = 8597255898:AAGL4xY1V9LCQV13Gl7NwJNqXVUiLy2-054
chat_id = 7283933799

target = +91 88648 82499

client = TelegramClient("session", api_id, api_hash)

def send_message(text):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": text
    }
    requests.post(url, data=data)

@client.on(events.UserUpdate)
async def handler(event):
    user = await event.get_user()

    if user.username == target_username:

        if event.online:
            print("User ONLINE")
            send_message("🟢 User is ONLINE")

        else:
            print("User OFFLINE")
            send_message("⚫ User went OFFLINE")


async def main():
    print("Bot started...")
    await client.run_until_disconnected()

client.start()
asyncio.run(main())