# create your Song class in this file
"""
This class only interacts with song
"""

class Song:
    #Determine items a song
    def __init__(self, title="", artist="", year=0, required=""):
        self.artist = artist
        self.title = title
        self.year = year
        self.required = required

    #Display inputted songs
    def __str__(self):
        if self.required == "n":
            required = "learned"
            return ("You have learned {} by {} ({})".format(self.title,self.artist, self.year))
        else:
            required = "y"
            return ("You have not learned {} by {} ({})".format(self.title,self.artist, self.year))

    def mark_learned(self):
        #Mark the song learned
        self.required = 'n'
        return self.required
