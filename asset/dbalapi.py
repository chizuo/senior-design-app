import requests
import config.restfulws as REST

class RestApi:
    '''
    Description: Stateless static class that contains the implementation of the REST API for RESTful web service
    '''
    def GET_User(credentials):
        '''
        Description: calls on the DBAL REST API (Get Method) to retrieve an identifier related to the program's hash identifier
        '''
        response = requests.get(REST.Path + credentials, verify=False)
        data = response.json()
        return data['uid']

    def GET_Movie(credentials):
        '''
        Description: calls on the DBAL REST API (GET Method) to retrieve the movie on the top of the user's save list.
        '''
        response = requests.get(REST.Path + credentials + '/movie', verify=False)
        data = response.json()
        return data['imdb_id']

    def POST_Movie(credentials, imdbID):
        '''
        Description: calls on the DBAL REST API (POST Method) to save the movie to the user's save list
        '''
        requests.post(REST.Path + credentials + '/' + imdbID, verify=False)
    
    def DELETE_Movie(credentials, imdbID):
        '''
        Description: calls on the DBAL REST API (DELETE Method) to remove a movie from the user's save list
        '''
        requests.delete(REST.Path + credentials + '/' + imdbID, verify=False)
