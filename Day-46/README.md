# Day-46
# README

# Billboard  Hot 100 Playlist Creator

This is a  Python script  that creates a  Spotify playlist  of the top songs on the  Billboard Hot 100  chart for a user-specified date. The script retrieves the song titles and artists from the  Billboard website  and uses the  Spotify API  to search for each song and add its URI to the playlist.

## Requirements

To run the script, you need to have the following installed:

-   Python 3
-   Requests  library:  `pip install requests`
-   BeautifulSoup4  library:  `pip install beautifulsoup4`
-   Spotipy  library:  `pip install spotipy`

You also need to have a  Spotify  account and register an app to get the  client ID  and secret for the Spotify API.

## Usage

1.  Clone or download the repository.
2.  Open a terminal or  command prompt  and navigate to the directory containing the script.
3.  Run the script using the command  `python billboard_playlist.py`.
4.  Enter the date you want to create the playlist for in the format  `YYYY-MM-DD`.
5.  Follow the instructions to authorize the script to access your Spotify account.
6.  Wait for the script to finish creating the playlist. The script will print the name and URL of the playlist when it's done.
7.  Enjoy listening to your new playlist!

## Notes

-   The script uses the  `SpotifyOAuth`  class from the  Spotipy library  to authorize access to the Spotify API. This means you need to log in to your Spotify account in a  web browser  to authorize the script.
-   The script creates a new  public playlist  with a name that includes the date you entered.
-   The script may not be able to find all the songs on the  Billboard chart  on Spotify. In this case, the script will print a message indicating which songs it couldn't find.
-   If the script encounters an error while adding songs to the playlist, it will delete the playlist.