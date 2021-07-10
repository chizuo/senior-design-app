# Go Ahead, Make My Movie Night 
CSC492 Senior Design Project - Application

Code contribution described in the report are found in [/assets](https://github.com/chizuo/senior-design-app/tree/main/asset)

[user.py](https://github.com/chizuo/senior-design-app/blob/main/asset/user.py) contains the AppHash class that creates a hashed identifier based off the system running the application. The result is meant to represent the user in the database. 

[movieUI.py](https://github.com/chizuo/senior-design-app/blob/main/asset/movieUI.py) contains the implementation of the movieUI, representing the observer, that uses the Movie class, RestApi class, and ImdbApi class

[movie.py](https://github.com/chizuo/senior-design-app/blob/main/asset/movie.py) contains the Movie class and subject of the observer.

[imdb.py](https://github.com/chizuo/senior-design-app/blob/main/asset/imdb.py) contains the ImdbApi class that implements the REST API of the IMDb Web Service. The config files for this class can be found at [./config/imdb.py](https://github.com/chizuo/senior-design-app/blob/main/config/imdb.py)

[dbalapi.py](https://github.com/chizuo/senior-design-app/blob/main/asset/dbalapi.py) contains the RestApi class that implements the REST API linked below below. The config files for this class can be foudn at [./config/restfulws.py](https://github.com/chizuo/senior-design-app/blob/main/config/restfulws.py)

Link to corresponding [REST API](https://github.com/chizuo/senior-design-api)
