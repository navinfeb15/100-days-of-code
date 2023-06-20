import requests
import bs4
import datetime as dt
import pprint
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials

# Set the URL for the Billboard Hot 100 chart
url = "https://www.billboard.com/charts/hot-100/"

# Prompt the user to enter a date
user_date = input("Which date you want to travel to. Type your date in this format : YYYY-MM-DD\n")

# Append the user-entered date to the URL to create the URL for the desired chart
new_url = url + user_date

# Create an empty dictionary to store the song titles and artists
song_list = {}

# Retrieve the webpage for the desired chart
response = requests.get(url=new_url)

# Parse the HTML content of the webpage using BeautifulSoup
soup = bs4.BeautifulSoup(response.text, "html.parser")

# Find all the elements that contain a song title and artist
song_elements = soup.find_all("ul", class_="o-chart-results-list-row")

# Loop through each song element and extract the song title and artist
for element in song_elements:
    song = element.find("h3").getText().strip()  # Get the song title
    # Get the artist name using a CSS selector for the specific HTML elements
    artist = element.select('span.c-label.a-no-trucate.a-font-primary-s.lrv-u-font-size-14\@mobile-max.u-letter-spacing-0021.lrv-u-display-block.a-truncate-ellipsis-2line.u-max-width-330.u-max-width-230\@tablet-only')[0].getText().strip()
    song_list[song] = artist  # Add the song and artist to the song_list dictionary

# Set the desired scope for accessing Spotify data
scope = "user-library-read"

# Set the Spotify API credentials and redirect URI
SPOTIPY_CLIENT_ID = "0ef1d5750561441297060ee0d2bdf233"
SPOTIPY_CLIENT_SECRET = "<YOUR_CLIENT_SECRET>"
SPOTIPY_REDIRECT_URI = r"http://example.com"

# Create an instance of the SpotifyOAuth class using the credentials and redirect URI
client_credentials_manager = SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URI, scope="playlist-modify-public playlist-modify-public user-library-read", cache_path=".cache")

# Create a Spotify client using the SpotifyOAuth instance
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Create a new playlist on the user's Spotify account with the name of the desired chart
test = sp.user_playlist_create(user=sp.current_user()["id"], name=user_date + " Billboard 100", public=True, description='testing creatinf playlist by code')

# Extract the playlist ID from the response
playlist_id = test["id"]

# Define a function to search for a song's URI on Spotify based on its title and artist
def find_song_uri(song_name, song_artist):
    try:
        # Try to find a match for the song and artist
        result = sp.search(q=f'track:{song_name} artist:{song_artist}', type='track')["tracks"]['items'][0]['uri']
    except IndexError:
        # If no match is found for the song and artist, search for the song only
        result = sp.search(q=f'track:{song_name}', type='track')
        if len(result["tracks"]['items']) == 0:
            # If no match is found for the song, return None
            print(f"song: {song_name} : {song_artist} doesnt have URI")
            result = None
        else:
            # If a match is found for the song only, get its URI
            result = result["tracks"]['items'][0]['uri']
    finally:
        return result

# Use the find_song_uri function to get the URI for each song in the song_list dictionary
songs_uri = [find_song_uri(song, artist) for song, artist in song_list.items() if find_song_uri(song, artist)]

try:
    # Add the songs to the new playlist on the user's Spotify account
    add_songs = sp.user_playlist_add_tracks(user=sp.current_user()["id"], playlist_id=playlist_id, tracks=songs_uri)
except Exception:
    # If an error occurs, delete the playlist
    print(Exception, '\nDeleting playlist...\n')
    sp.user_playlist_unfollow(user=sp.current_user()["id"], playlist_id=playlist_id)