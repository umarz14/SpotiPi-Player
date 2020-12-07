import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint

scope = "user-read-playback-state,user-modify-playback-state"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="70e434b1c2da43c7acbe139ade2d1205",
                                               client_secret="19ecc6a4352f4246b2724fb0cb8f3684",
                                               redirect_uri="http://127.0.0.1:9090",
                                               scope=scope))

# Shows playing devices
res = sp.devices()
pprint(res)

# Change track
#sp.start_playback(uris=['spotify:track:2HbKqm4o0w5wEeEFXm2sD4'])

