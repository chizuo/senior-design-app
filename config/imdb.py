# Description: Variables in this file are CONST values, considered to be config. items, that are used for the ImdbApi calls. 
# Note: Any changes to the IMDB API call items should be made here and not on the code.

headers = {
            'x-rapidapi-key': "dda6d06c29msh1eb4baff5cea14ep1bf5acjsn07a454014447",
            'x-rapidapi-host': "movies-tvshows-data-imdb.p.rapidapi.com"
        }

url = "https://movies-tvshows-data-imdb.p.rapidapi.com/"

trending = "get-trending-movies"
random = "get-random-movies"
nowPlaying = "get-nowplaying-movies"