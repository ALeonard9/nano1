# webbrrowser is a library necessary to open web pages
import webbrowser

# class Video is a parent class that contains title and duration.
class Video():
    def __init__(self, title, duration, trailer_youtube):
        self.title = title
        self.duration = duration
        self.trailer_youtube_url = trailer_youtube

# Opens a browser showing the trailer of the selected movie
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

    def show_all(self):
        print("Title: "+ self.title +"\n Duration: " + self.duration + " minutes \n Trailer URL: " +self.trailer_youtube_url)

# class Movie is a child class of Video. Contains movie speicific information
class Movie(Video):
    """This class provides movie data"""

# Constants should be all uppercase
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

# Takes in parameters listed below. Assigns them to self.
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, duration):
        Video.__init__(self, movie_title, duration, trailer_youtube)
        self.storyline = movie_storyline
        self.poster_image_url= poster_image




class TV(Video):
    def __init__(self, title, duration, season, episode, trailer_youtube):
        Video.__init__(self, title, duration, trailer_youtube)
        self.season = season
        self.episode = episode
