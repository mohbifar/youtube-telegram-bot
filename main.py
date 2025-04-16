import requests
import time
from googleapiclient.discovery import build

telegram_token = '8005150199:AAHa5UL5uKikDytbICUk8qZmgQKKcExjW-Q'
chat_id = '-1002637620980'
youtube_api_key = 'AIzaSyAL2XAQi7bOFWglFDZ9fIxRT5YPHi7WreU'

playlist_ids = [
    'PLXMgkRzUOYP2Z7rJ-ZCO9X5F9RZ6y7mY1',  # SlowMotionGymnastics-SMG
    'PLTCXR2uMOuIuqaAAMFlRI0U80iGnryHLg',  # BEAUTYOFSPORTS-e3t
    'PLtd6S0eFFEvQXp-kOhkZqKwSCdQzXeQxH',  # PhlowZone
    'PLgAC9mDdYwAW7-Gvs9dRe1Zga1V0SkO4E',  # JumperOneAthletics
    'PLS9C1a_P9Q_bEvkMQG0N1BdyO4XLz-QY9',  # thetennisview
    'PLhDh5rk4PONVubF7OERsK5z4w5c6cKVG9',  # ai.shutov
    'PLlvFlAcrxQiihHDXILcTtUR9fipjKpZ2R',  # shutuber6
    'PLUoFcV8NB9E0apns1Ac9b8xuE0rBdNQLn',  # youngstars043
    'PLsx5t-N1J2Whf3OdKqT8JfnzkVmMD2ZB-',  # tracksportsent
    'PLjlLb-jDDiHrAQGIt7C1PQWZ3HQtzYMhz',  # RKAthletic
    'PLvGZpKNz3gcL5EEXp9TCpZ_OuMWc1qMNN',  # jennibelleboutique
    'PLMWxZonmwQeoRmcdO-9q8E7JWufLJtnZ1',  # YouarePowerful.Brave.Brilliant
    'PLsQJ08OYHDBb6MWR1h0G4Q4AocZr9edhR',  # surf-ladies
    'PLbNIm1Un5UM8KjXjQGUXF3uyDN2cRx8De',  # mmd_short78
]

youtube = build('youtube', 'v3', developerKey=youtube_api_key)

def get_latest_video_from_playlist(playlist_id):
    request = youtube.playlistItems().list(
        part='snippet',
        playlistId=playlist_id,
        maxResults=1
    )
    response = request.execute()
    video = response['items'][0]
    video_id = video['snippet']['resourceId']['videoId']
    title = video['snippet']['title']
    url = f'https://www.youtube.com/watch?v={video_id}'
    return title, url

def send_to_telegram(video_title, video_url):
    message = f"{video_title}\n{video_url}"
    url = f"https://api.telegram.org/bot{telegram_token}/sendMessage"
    requests.post(url, data={'chat_id': chat_id, 'text': message})

def run_bot():
    processed = set()
    while True:
        for playlist_id in playlist_ids:
            try:
                title, url = get_latest_video_from_playlist(playlist_id)
                if url not in processed:
                    send_to_telegram(title, url)
                    processed.add(url)
            except Exception as e:
                continue
        time.sleep(3600)

if __name__ == "__main__":
    run_bot()
