import requests
import config.imdb as imdb

class ImdbApi:
    '''
    Description: Stateless static class that contains the implementation of the IMDB API web service.
    Changes to the API parameters set by IMDB should be made at the config/imdb file and not to this code.
    '''
    def make_request(self, type, page):
        '''
        Description: calls on the IMDB API to retrieve a specific list of movies to suggest to the user.
        Receives: string that contains the category used to generate list, int for the page in the list
        Returns: returns a list of 20 movies which are JSON objects
        '''
        querystring = {"type":type,"page":page}
        response = requests.request("GET", imdb.url, headers=imdb.headers, params=querystring)
        response_as_dict = response.json()
        print("request for type: %s @ page: %i" % (type, page))
        return response_as_dict["movie_results"]

    def movie_details(self, imdb_id):
        '''
        Description: calls on the IMDB API to retrieve a specific details of the movie.
        Receives: string that contains the imdb_id primary key of the imdb database
        Returns: a JSON object that represents the movie of the primary key used.
        '''
        querystring = {"type":"get-movie-details","imdb":imdb_id}
        response = requests.request("GET", imdb.url, headers=imdb.headers, params=querystring)
        return response.json()