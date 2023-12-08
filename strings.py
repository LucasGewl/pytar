from keyboard import is_pressed


class Strings:
    def __init__(self, string: str, row: int) -> None:
        self.string = string
        self.row = row
        self.frets = [[],
                      [],
                      [],
                      [],
                      [],
                      ['high_f.wav', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=']]
        self.playing = False

    def get_fret(self) -> int:
        if self.row == 5:
            if is_pressed('1'):
                return 0
        if self.row == 4:
            if is_pressed('q'):
                return 0
        return -1

    def get_note(self, pos: int) -> str:
        self.playing = True
        if pos >= 0:
            return self.string + '/' + self.frets[self.row][pos]
        return self.string + '/' + self.string[7:] + '.wav'
