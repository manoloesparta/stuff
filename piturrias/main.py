import os
import pprint
from string import digits
from dotenv import load_dotenv
from spotipy import util, Spotify


load_dotenv()
PLAYLIST_DEST = '6L2yWuWMLD6PkJrGJdbQIq'
pp = pprint.PrettyPrinter(indent=1)


def auth(username):
    scope = 'playlist-modify-private playlist-modify-public user-read-private'

    params = {
        'scope': scope,
        'username': username,
        'client_id': os.environ['CLIENT_ID'],
        'client_secret': os.environ['CLIENT_SECRET'],
        'redirect_uri': os.environ['REDIRECT_URI'],
    }

    try:
        token = util.prompt_for_user_token(**params)
    except:
        os.remove(f'.cache-{username}')
        token = util.prompt_for_user_token(**params)

    return Spotify(auth=token)


def get_songs():
    with open('dad_songs') as f:
        songs = f.readlines()

    splited = [ i.split('/') for i in songs ]

    song_names = []
    for sp in splited:
        try:
            name = clean_song_name(sp[3])
            song_names.append({
                'name': name,
                'album': sp[2],
                'artist': sp[1],
            })
            print(name)
        except Exception as e:
            pass 

    return song_names


def clean_song_name(name):
    result = name[:-1] .split('.')[0]
    result = result.replace('-', '')
    result = result.lstrip(digits)
    return result.strip()


def main():
    user = auth('manoloesparta')
    songs = get_songs()

    for song in songs:
        try:
            result = user.search(song['name'], limit=3)
            name = result['tracks']['items'][0]['uri']
            user.playlist_add_items(PLAYLIST_DEST, [name])
            print('yes')
        except Exception as e:
            print('no')
    

if __name__ == '__main__':
    main()
