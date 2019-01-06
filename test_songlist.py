"""
(incomplete) Tests for SongList class
"""
from songlist import SongList
from song import Song

# test empty SongList
song_list = SongList()
print(song_list)
assert len(song_list.list_songs) == 0

# test loading songs
song_list.load_songs()

print(song_list.list_songs)
assert len(song_list.list_songs) == 6
print(song_list)
assert len(song_list.list_songs) > 0  # assuming CSV file is not empty

# TODO: add tests below to show the various required methods work as expected
# test sorting songs
song_list.sort("title")


# test adding a new Song
song_list.add_to_list(Song("21 Guns", "Green Day", "2006", "y"))
print(song_list)
