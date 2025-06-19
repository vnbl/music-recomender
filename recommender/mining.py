import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from pyspark.sql import SparkSession
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv('../.env')

client_id = os.getenv('SPOTIPY_CLIENT_ID')
client_secret = os.getenv('SPOTIPY_CLIENT_SECRET')

spark = SparkSession.builder.appName('Spotify Artist Data Mining').getOrCreate()

def get_spotify_client(client_id, client_secret):
    credentials = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=credentials)
    return sp

def mine_artist_data(artist_name, sp):
    try:
        # Search for the artist
        results = sp.search(q=artist_name, type='artist')
        artist_data = []

        if results['artists']['items']:
            for artist in results['artists']['items'][0:1]:  # Only process the first artist
                data = {}
                
                # Dynamically extract all key-value pairs from the artist object
                for key, value in artist.items():
                    if isinstance(value, list):
                        data[key] = ', '.join(map(str, value))  # Convert list to a comma-separated string
                    elif isinstance(value, dict):
                        # Flatten nested dictionaries
                        for sub_key, sub_value in value.items():
                            data[f"{key}_{sub_key}"] = str(sub_value)
                    else:
                        data[key] = str(value)

                artist_data.append(data)

        return artist_data

    except Exception as e:
        print(f"Error retrieving artist data: {e}")
        return []

    
sp = get_spotify_client(client_id, client_secret)

# Example usage
artists = ['Bad Bunny', 'Taylor Swift', 'BTS']
artist_info = []

for artist in artists:
    artist_info.extend(mine_artist_data(artist, sp))

# Convert to DataFrame
artist_df = spark.createDataFrame(artist_info)

# Show DataFrame
print(artist_df.show())  # To print a Spark DataFrame
artist_df.toPandas().to_csv("output.csv")  # To save as a CSV file