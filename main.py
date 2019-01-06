"""
Name: Le Minh
Date: 6/1/2019
Brief Project Description: This project will create a Graphical User Interface program based
on the list of songs in assignment 1.
GitHub URL: https://github.com/JCUS-CP1404/a2--jc474652
"""

from kivy.app import App
from kivy.lang import Builder
from songlist import SongList
from kivy.properties import StringProperty
from kivy.properties import ListProperty
from song import Song
from kivy.uix.button import Button


# Create your main program in this file, using the SongsToLearnApp class


class SongsToLearnApp(App):  # Class refering to the Kivy app
#Main

    message = StringProperty()
    message2 = StringProperty()
    current_sort = StringProperty()
    sort_choices = ListProperty()

    def __init__(self, **kwargs):
        """
        Initiate song_list to SongList class
        Initiate sort_choices as an array
        Initiate the current sorting option as "title"
        Initiate the function load_songs to load csv file
        :param kwargs:
        returns None
        """
        super(SongsToLearnApp, self).__init__(**kwargs)
        self.song_list = SongList()
        self.sort_choices = ["Title", "Artist", "Year", "required"]
        self.current_sort = self.sort_choices[0]
        self.song_list.load_songs()

    def build(self):
        """
        Build the Kivy GUI
        :return: widgets of the GUI
        """
        self.learn___ = "Songs to learn 2.0"  # Name the GUI's name
        self.title = self.learn___
        self.root = Builder.load_file('app.kv')
        self.create_widgets()
        return self.root

    def change_sort(self, sorting_choice):
        """
        Function to change the sorting of the song list
        :param sorting_choice: Based on what choice the user selects, the song list will be sorted that way
        :return: sorted song list
        """
        self.message = "song have been sorted by: {}".format(sorting_choice)
        self.song_list.sort(sorting_choice)
        self.root.ids.entriesBox.clear_widgets()
        self.create_widgets()
        sort_index = self.sort_choices.index(sorting_choice)
        self.current_sort = self.sort_choices[sort_index]

    def blank(self):
        """
        This function clear all the input the user put in after clicking the clear button
        :return: clear all the inputs
        """
        self.root.ids.song_title.text = ''
        self.root.ids.song_artist.text = ''
        self.root.ids.song_year.text = ''
        self.root.ids.entriesBox.clear_widgets()
        self.create_widgets()

    def create_widgets(self):
        """
        Create widgets that lists the songs from the csv file
        """
        num_song = len(self.song_list.list_songs)
        learned_song = 0
        for song in self.song_list.list_songs:  # Loop from the first song to the last song within the song list

            title = song.title
            artist = song.artist
            year = song.year
            learned = song.required
            display_text = self.generateDisplayText(title, artist, year,
                                                    learned)  # display what should be added to the widget

            if learned == "n":
                # Condition when the song is learned, count the number of learned songs and format their background color (Velvet)

                learned_song += 1
                button_color = self.getColor(learned)
            else:
                button_color = self.getColor(learned)  # If the song is not learned, display Blue color

            temp_button = Button(text=display_text, id=song.title,
                                 background_color=button_color)  # Mark the song learned
            temp_button.bind(on_release=self.entry)

            self.root.ids.entriesBox.add_widget(temp_button)  # Apply to the Kivy app
        self.message = "To learn: {}. Learned: {}".format(num_song - learned_song, learned_song)
        # Display number of songs learned and not learned

    def generateDisplayText(self, title, artist, year, learned): #Formating any text displayed in the messages
        if learned == "n":
            display_text = "{} by {} ({}) (Learned)".format(title, artist, year)
        else:
            display_text = "{} by {} ({})".format(title, artist, year)

        return display_text

    def getColor(self, learned): #Display colors of the song widgets
        if learned == "n":
            button_color = [1, 1, 1, 1]
        else:
            button_color = [1, 2, 2, 2]
        return button_color

# Display the 2nd message
    def entry(self, button):
        buttonText = button.text                #Determine the text on the widget buttons
        selectedSong = Song()
        for song in self.song_list.list_songs:

            songDisplayText = self.generateDisplayText(song.title, song.artist, song.year, song.required)
            #Display the text as formatted in generateDisplayText
            if buttonText == songDisplayText:
                selectedSong = song
                break

        selectedSong.mark_learned()
        self.root.ids.entriesBox.clear_widgets()    #Apply to Kivy GUI
        self.create_widgets()

        self.message2 = "You have learned {}".format(selectedSong.title)        #Display whatever changed in message 2

    def add_songs(self):
        """
        Function allows user to add any song they want
        :return: Add the song inputted to the song list
        """

        #Check for empty inputs
        if self.root.ids.song_title.text == "" or self.root.ids.song_artist.text == "" or self.root.ids.song_year.text == "":
            self.root.ids.status2.text = "All fields must be completed"
            return
        try:
            #Define song items inputted
            song_title = str(self.root.ids.song_title.text)
            song_artist = str(self.root.ids.song_artist.text)
            song_year = int(self.root.ids.song_year.text)
            is_required = "y"

            #Add the song inputted to the song list
            self.song_list.add_to_list(song_title, song_artist, song_year, is_required)
            temp_button = Button(
                text=self.generateDisplayText(song_title, song_artist, song_year, is_required))
            temp_button.bind(on_release=self.entry)

#Format the new song items
            temp_button.background_color = self.getColor(is_required)
            self.root.ids.entriesBox.add_widget(temp_button)

#Empty the inputs
            self.root.ids.song_title.text = ""
            self.root.ids.song_artist.text = ""
            self.root.ids.song_year.text = ""

        except ValueError: #Display error when year input is not a number
            self.message2 = "Please enter a valid year"

    def on_stop(self):
        self.song_list.save_songs()

SongsToLearnApp().run()
