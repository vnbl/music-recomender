import streamlit as st 
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv

load_dotenv('../.env')

client_id = os.getenv('SPOTIPY_CLIENT_ID')
client_secret = os.getenv('SPOTIPY_CLIENT_SECRET')
redirect_uri = 'http://127.0.0.1:8502'#os.getenv('REDIRECT_URI')

cache_path = os.path.join(os.getcwd(), ".cache/")

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope='user-library-read', cache_path=cache_path))

def process_artist(artist_name, sp):
    """
    Args:
        artist_name (str): The name of the artist to search for.
        sp (spotipy.Spotify): An authenticated Spotipy client instance.
    Returns:
        str: A comma-separated string of genres or 'No genres found' if no genres are found.
 
    Searches for the artist on Spotify and returns their genres as a comma-separated string.
    If no genres are found, returns 'No genres found'. Handles errors gracefully.
    """
    try:
        search_results = sp.search(q=artist_name, type='artist')
        genres_info = []

        if 'artists' in search_results and 'items' in search_results['artists']:
            artists = search_results['artists']['items']
            for artist in artists:
                if artist['name'].lower() == artist_name.lower():
                    genres_info = artist.get('genres', [])
                    break
        
        genre_string = ', '.join(genres_info) if genres_info else 'No genres found'
        return genre_string
    except Exception as e:
        return f'Error: {e}'


def fetch_artist_genres(artist_name):
    """
    Args:
        artist_name (str): The name of the artist to search for.
    Returns:
        str: A comma-separated string of genres or 'No genres found' if no genres are found.
 
    Searches for the artist on Spotify and returns their genres as a comma-separated string.
    If no genres are found, returns 'No genres found'. Handles errors gracefully.
    """
    try:
        search_results = sp.search(q=artist_name, type='artist')
        genres_info = []

        if 'artists' in search_results and 'items' in search_results['artists']:
            artists = search_results['artists']['items']

            for artist in artists:
                if artist['name'].lower() == artist_name.lower():
                    genres_info = artist.get('genres', [])
                    break
        genre = ', '.join(genres_info) if genres_info else 'No genres found'
        return genre
    except Exception as e:
        return f'Error: {e}'

def search_artist_genres():
    """
    Streamlit app function to search for an artist's genres.
    
    Prompts the user to enter an artist's name and displays the genres associated with that artist.
    """
    try:
        st.title("Artist Genre Finder")
        artist_name = st.text_input('Enter the name of the artist you want to search')

        button = st.button('Search')

        if button:
            if artist_name:
                genre_string = process_artist(artist_name, sp)
                st.write(f'Genres for {artist_name}: {genre_string}')
            else:
                st.write('Please enter an artist name')
    except Exception as e:
        st.write(f'Error: {e}')



search_artist_genres()
