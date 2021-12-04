Nikolas Otsuki
class: Guitar
This class is a representation of the real world object, guitar. It gives the guitar a color as well as an identifier if it is an acoustic or electric guitar. The class is able to save a chord and add it to a song it the form of a list of chords played. 
The class variable is the instrument variable set to "String". This is simply to know that all guitars and string instruments. 
The data variable color is the color of the guitar.
The data variable type is what type of guitar it is. 
The data variable song is the song that is created after playing a chord.
The data variable chord is the chord the user wishes to play and be recorded into the song. 
The set_chord method sets which chord the user wants to play. The necesary argument is a string of whatever wanted chord (A,B,C#,D,E, etc.). The string inputted can also be multiple chords as the program simply reads the string as a whole.
The get_chord method simply retrieves the chord currently set. This is used in later methods to access the chords.
The play_chord method retrieves the saves chord and adds it to the song list. This is useful in case you missinput the chord.
The splay_song method prints the song list with each string of chord(s) as an item in a list. The song will come after a short message.
The clear_song method clears whatever has been saved in the song list. No arguemnts are needed for this method or the previous three methods. 
The del_chord method deletes the latest item in the song list. This is useful for going back and correcting mistakes. Requires no argument.


The demo program creates a guitar with a color and type. It then sets a group of chords, plays them, plays another set, deletes that set, replaces it with the correct set, then plays the song. It then deletes the whole song. The demo utilizes every method it a specific way but the user could do anything they want with in any order.
Nothing is needed to run the program. Simply running it should work.