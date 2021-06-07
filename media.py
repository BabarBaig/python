<<<<<<< HEAD
import webbrowser

''' In this sample file:
~ Read some data from a text file
~ Pass it to a website to check for profanities
~ Print website response (true/false) for any profanities
'''

class Movie():
    """ This class provides a way to store movie-related information """
    VALID_RATINGS = ['G', 'PG', 'PG-13', 'R']
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
=======
import webbrowser

''' In this sample file:
~ Read some data from a text file
~ Pass it to a website to check for profanities
~ Print website response (true/false) for any profanities
'''

class Movie():
    """ This class provides a way to store movie-related information """
    VALID_RATINGS = ['G', 'PG', 'PG-13', 'R']
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
>>>>>>> 3a3eeac04cbe757a5a977da746abe95ab991826d