import streamlit as st
import spotipy.util as util
import os

def callback():
    CLIENT_ID = os.environ.get('CLIENT_ID')
    CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
    REDIRECT_URI = os.environ.get('REDIRECT_URI')
    SCOPE = 'user-library-read playlist-modify-public'
    code = st.experimental_get_query_params().get("code")

    if code:
        token = util.oauth2.SpotifyOAuth(CLIENT_ID, CLIENT_SECRET, REDIRECT_URI).get_access_token(code)
        st.write("Authenticated successfully!")
        # Do something with the access token, like call the Spotify API
    else:
        st.write("Authentication failed.")
