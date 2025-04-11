import os
import asyncio
import requests
from telegram import Bot

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHANNEL = "@ماجراجویی‌های_ورزشی"
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

YOUTUBE_CHANNELS = [
    "UCqxPjMDgtg85WWGUioyl3tg",
    "UCDy24mzKpEtSm9Ugq8eY-7Q"
]

async def send_videos():
    bot = Bot(token=TOKEN)
    while True:
        try:
            for channel in YOUTUBE_CHANNELS:
                videos = get_videos(channel)
                for video in videos:
                    await bot.send_message(CHANNEL, video)  # اضافه کردن await
            await asyncio.sleep(3600)
        except Exception as e:
            print(f"Error: {e}")
            await asyncio.sleep(60)

def get_videos(channel_id):
    url = f"https://www.googleapis.com/youtube/v3/search?key={YOUTUBE_API_KEY}&channelId={channel_id}&part=snippet,id&order=date&maxResults=1"
    response = requests.get(url).json()
    return [f"https://youtu.be/{item['id']['videoId']}" for item in response.get('items', [])]

if __name__ == "__main__":
    asyncio.run(send_videos())
