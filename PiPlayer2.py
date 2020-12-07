import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint
import sys
import json

kl_alb = 'spotify:album:3DGQ1iZ9XKUQxAUWjfC34w'

scope = "user-read-playback-state,user-modify-playback-state"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="70e434b1c2da43c7acbe139ade2d1205",
                                               client_secret="19ecc6a4352f4246b2724fb0cb8f3684",
                                               redirect_uri="http://127.0.0.1:9090",
                                               scope=scope))

album = sp.album_tracks(kl_alb)
pprint(album)

sp.start_playback(uris=kl_alb)