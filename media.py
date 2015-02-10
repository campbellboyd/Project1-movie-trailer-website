'''
Created on 7 Feb 2015

@author: campbell
'''
import webbrowser

class Movie():

# defines data items and their source
    def __init__(self, movie_title, opened, storyline, director, writer, stars, poster_image, trailer_youtube):
        self.title = movie_title
        self.opened = opened
        self.storyline = storyline
        self.director = director
        self.writer = writer
        self.stars  = stars
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        
#define method to run trailer when clicked
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)