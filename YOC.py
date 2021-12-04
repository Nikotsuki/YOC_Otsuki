"""
Nikolas Otsuki
file: 10.1_YOC
"""

class Guitar:
    instrument = "String"
    def __init__(self, color, type):
        self.__color = color
        self.__type = type
        self.__song = []
    
    def set_chord(self, chord):
        self.__chord = chord

    def get_chord(self):
        return self.__chord

    def play_chord(self):
        self.__song.append(self.get_chord())

    def play_song(self):
        print("Your song is:", self.__song)

    def clear_song(self):
        self.__song.clear()
    
    def del_chord(self):
        self.__song.pop(-1)

def main():
    x = Guitar("Black", "Acoustic")
    x.set_chord("B#, A, G")
    x.play_chord()
    x.set_chord("A")
    x.play_chord()
    x.del_chord()
    x.set_chord("A#")
    x.play_chord()
    x.play_song()
    x.clear_song()


if __name__ == "__main__":
    main()