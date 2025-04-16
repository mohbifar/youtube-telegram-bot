import requests
import time
from googleapiclient.discovery import build

telegram_token = '8005150199:AAHa5UL5uKikDytbICUk8qZmgQKKcExjW-Q'
chat_id = '-1002637620980'
youtube_api_key = 'AIzaSyAL2XAQi7bOFWglFDZ9fIxRT5YPHi7WreU'
channels = [
    'SlowMotionGymnastics-SMG',
    'BEAUTYOFSPORTS-e3t',
    'PhlowZone',
    'JumperOneAthletics',
    'thetennisview',
    'wwsportss',
    'ai.shutov',
    'shutuber6',
    'youngstars043',
    'tracksportsent',
    'RKAthletic',
    'thebestgymnastics',
    'daieb_ing',
    'jennibelleboutique',
    'YouarePowerful.Brave.Brilliant',
    'surf-ladies'
]

youtube = build('youtube', 'v3', developerKey=youtube_api_key)

def get_latest_video(channel_id):
    request = youtube.search().list(
        part="snippet",
        channelId=channel_id,
        order="date",
        maxResults=1
    )
    response = request.execute()
    video = response['items'][0]
    video_id = video['id']['videoId']
    video_title = video['snippet']['title']
    video_url = f'https://www.youtube.com/watch?v={video_id}'
    return video_title, video_url

def send_to_telegram(video_title, video_url):
    message = f"{video_title}\n{video_url}"
    url = f"https://api.telegram.org/bot{telegram_token}/sendMessage?chat_id={chat_id}&text={message}"
    requests.get(url)

def run_bot():
    processed_videos = set()
    while True:
        for channel in channels:
            video_title, video_url = get_latest_video(channel)
            if video_url not in processed_videos:
                send_to_telegram(video_title, video_url)
                processed_videos.add(video_url)
        time.sleep(3600)

if __name__ == "__main__":
    run_bot()
