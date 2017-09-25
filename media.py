"""This package contains the Movie class that holds all the movie-related data
that will be shown on movie trailer website."""


class Movie():
    """This class contains all the information related to the movie.
    i.e. This class is used to display the movie title and poster.
    This class also contains the youtube trailer URL which can be
    used to play the trailer-video when clicked on poster."""


    def __init__(self, title, storyline, poster_image_url,
    	trailer_youtube_url):
        self.title = title  # is used for showing the
                            # movie title below poster image
        self.storyline = storyline  # not being used right now,
                                    # but later can be used to display
                                    # story line when mouse hovering over
                                    # movie poster
        self.poster_image_url = poster_image_url
                                # is used to show movie poster
        self.trailer_youtube_url = trailer_youtube_url
                                # is used to play the movie trailer
                                # in a pop up box
