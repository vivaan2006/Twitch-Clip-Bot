import requests
import json
import os
from datetime import datetime, timedelta, timezone

CLIENT_ID = 'zhttm83knfhraecoqb3q45gpu9qats'
CLIENT_SECRET = 'd7p2tledku6tyvthfqdlfuyc9pe99p'

def get_access_token():
    url = 'https://id.twitch.tv/oauth2/token'
    params = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'grant_type': 'client_credentials'
    }
    response = requests.post(url, params=params)
    response.raise_for_status()
    return response.json()['access_token']

def get_broadcaster_id(token, username):
    headers = {
        'Client-ID': CLIENT_ID,
        'Authorization': f'Bearer {token}'
    }
    url = f'https://api.twitch.tv/helix/users?login={username}'
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()['data'][0]['id']

def get_top_clips(token, broadcaster_id, limit=10):
    headers = {
        'Client-ID': CLIENT_ID,
        'Authorization': f'Bearer {token}'
    }

    yesterday = (datetime.now(timezone.utc) - timedelta(days=1)).isoformat()

    params = {
        'first': limit,
        'started_at': yesterday,
        'broadcaster_id': broadcaster_id
    }

    response = requests.get('https://api.twitch.tv/helix/clips', headers=headers, params=params)
    response.raise_for_status()
    return response.json()['data']

if __name__ == '__main__':
    try:
        token = get_access_token()
        username = 'KaiCenat'  # Pick your streamer here
        broadcaster_id = get_broadcaster_id(token, username)
        clips = get_top_clips(token, broadcaster_id)
        os.makedirs('../clips', exist_ok=True)
        with open('../clips/top_clips.json', 'w') as f:
            json.dump(clips, f, indent=2)
        print("✅ Fetched and saved top clips.")
    except Exception as e:
        print("❌ Error:", e)