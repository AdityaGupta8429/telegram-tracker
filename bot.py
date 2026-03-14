from telethon import TelegramClient, events
import requests

api_id = 28813625
api_hash = "792c04f8813f429d387ec93ba1a6332d"

bot_token = "8597255898:AAGL4xY1V9LCQV13Gl7NwJNqXVUiLy2-054"
chat_id = "7283933799"

# phone number without spaces
target_phone = "+918864882499"

client = TelegramClient("session", api_id, api_hash)

def send_message(text):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    requests.post(url, data={
        "chat_id": chat_id,
        "text": text
    })

@client.on(events.UserUpdate)
async def handler(event):
    user = await event.get_user()

    if user.phone and ("+" + user.phone) == target_phone:

        if event.online:
            print("User ONLINE")
            send_message("🟢 User is ONLINE")

        else:
            print("User OFFLINE")
            send_message("⚫ User went OFFLINE")

print("Bot started...")

with client:
    client.run_until_disconnected()