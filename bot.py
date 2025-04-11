import os
import time
import requests
from telegram import Bot

TOKEN = "8005150199:AAHa5UL5uKikDytbICUk8qZmgQKKcExjW-Q"
CHANNEL = "@ماجراجویی‌های_ورزشی"
YOUTUBE_API_KEY = "AIzaSyAL2XAQi7bOFWglFDZ9fIxRT5YPHi7WreU"

YOUTUBE_CHANNELS = [
    "UCqxPjMDgtg85WWGUioyl3tg",
    "UCDy24mzKpEtSm9Ugq8eY-7Q",
]

bot = Bot(token=TOKEN)

def get_videos(channel_id):
    url = f"https://www.googleapis.com/youtube/v3/search?key={YOUTUBE_API_KEY}&channelId={channel_id}&part=snippet,id&order=date&maxResults=1"
    response = requests.get(url).json()
    return [f"https://youtu.be/{item['id']['videoId']}" for item in response.get('items', [])]

while True:
    try:
        for channel in YOUTUBE_CHANNELS:
            videos = get_videos(channel)
            for video in videos:
                bot.send_message(CHANNEL, video)
        time.sleep(3600)
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(60)
