class Movie:
    '''
    Description: takes response from ImdbApi.movie_details() and turns into a Movie object.
    Input: string, string, string, string, string, string, string, string, int, list of strings, list of strings, list of strings, list of strings, list of strings
    '''
    def __init__(self, title, description, year, imdb_id, imdb_rating, rated, runtime, genres, stars, directors, language) -> None:
        self.title = title
        self.description = description
        self.year = year
        self.id = imdb_id
        self.rating = imdb_rating
        self.rated = rated
        self.runtime = runtime
        self.genres = genres
        self.actors = stars
        self.directors = directors
        self.language = language


