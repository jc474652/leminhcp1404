# create your SongList class in this file
from song import Song
from operator import attrgetter


class SongList:
    """
    initiate the self attribute list_songs
    :return: None
    """
    def __init__(self):
        self.list_songs = []

    def load_songs(self):
        """
        Load the songs from csv file and append them to list_songs
        """

        in_file = open("songs.csv","r")
        lines = in_file.readlines()
        for line in lines:
            song_item = line.split(',')
            song_item[3] = song_item[3].strip('\n')
            loaded_song = Song(song_item[0],song_item[1],song_item[2],song_item[3])

            self.list_songs.append(loaded_song)

        in_file.close()

    def add_to_list(self, title, artist, year, is_required):
        #add the inputted song to the song list
        newSong = Song(title, artist, year, 'y')
        self.list_songs.append(newSong)

    def sort(self, key):
        """
        Sort the songs based on the sort_choice selected
        :param key: self, key
        :return: none
        """
        self.list_songs = sorted(self.list_songs, key=attrgetter(key, "title"))




    def save_songs(self):
        #save changes made to the songs and then out file
        csv_string = ""
        for each in self.list_songs:
            csv_string += "{},{},{},{}\n".format(each.title, each.artist, each.year, each.status)
        out_file = open("songs.csv", 'w')
        out_file.seek(0)
        out_file.truncate()
        out_file.write(csv_string)
        out_file.close()




