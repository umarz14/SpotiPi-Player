import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint


import time
import nfc
import requests
import uuid
import sys

#nfc_reader_path="usb"

# this function gets called when a NFC tag is detected
def touched(tag):

    if tag.ndef:
        for record in tag.ndef.records:
            try:
                receivedtext = record.text
            except:
                print("Error reading a *TEXT* tag from NFC.")
                return True
            
            receivedtext_lower = receivedtext.lower()

            print("")
            print("Read from NFC tag: "+ receivedtext)

            if receivedtext_lower.startswith ('spotify'):
                scope = "user-read-playback-state,user-modify-playback-state"
                sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="70e434b1c2da43c7acbe139ade2d1205",
                                               client_secret="19ecc6a4352f4246b2724fb0cb8f3684",
                                               redirect_uri="http://127.0.0.1:9090",
                                               scope=scope))

                # Shows playing devices
                res = sp.devices()
                pprint(res)
            
            if receivedtext_lower.startswith ('track', 8):
                # Change track
                sp.start_playback(uris=[receivedtext])
            
            if receivedtext_lower.startswith ('album', 8):
                sp.start_playback(context_uri=receivedtext)
            


    else:
        print("")
        print ("NFC reader could not read tag. This can be because the reader didn't get a clear read of the card. If the issue persists then this is usually because (a) the tag is encoded (b) you are trying to use a mifare classic card, which is not supported or (c) you have tried to add data to the card which is not in text format. Please check the data on the card using NFC Tools on Windows or Mac.")

    return True

print("")
print("")
print("Loading and checking readnfc")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("")
print("SCRIPT")

print("")
print("NFC READER")
print("Connecting to NFC reader...")
try:
    reader = nfc.ContactlessFrontend()
    assert reader.open('usb:001:005') is True
except IOError as e:
    print ("... could not connect to reader")
    print ("")
    print ("You should check that the reader is working by running the following command at the command line:")
    print (">  python -m nfcpy")
    print ("")
    print ("If this reports that the reader is in use by readnfc or otherwise crashes out then make sure that you don't already have readnfc running in the background via pm2. You can do this by running:")
    print (">  pm2 status             (this will show you whether it is running)")
    print (">  pm2 stop readnfc       (this will allow you to stop it so you can run the script manually)")
    print ("")
    print ("If you want to remove readnfc from running at startup then you can do it with:")
    print (">  pm2 delete readnfc")
    print (">  pm2 save")
    print (">  sudo reboot")
    print ("")
    sys.exit()

print("... and connected to " + str(reader))

print("")
print("OK, all ready! Present an NFC tag.")
print("")

while True:
    reader.connect(rdwr={'on-connect': touched, 'beep-on-connect': False})
    time.sleep(0.1)
