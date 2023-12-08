#import keyboard._canonical_names
import winsound

from winsound import PlaySound
from keyboard import is_pressed
from strings import Strings
from time import sleep


string_1 = Strings('sounds/open_e', 5)
string_2 = Strings('sounds/open_b', 4)
string_3 = Strings('sounds/open_g', 3)
string_4 = Strings('sounds/open_d',2)
string_5 = Strings('sounds/open_a',1)
string_6 = Strings('sounds/open_e_low',0)


while True:
    if is_pressed('slash'):
        fret = string_6.get_fret()
        note = string_6.get_note(fret)
        if string_6.playing:
            PlaySound(note, winsound.SND_PURGE)
            sleep(0.1)
            PlaySound(note, winsound.SND_ASYNC)
        else:
            PlaySound(note, winsound.SND_ASYNC)
    if is_pressed('shift'):
        fret = string_5.get_fret()
        note = string_5.get_note(fret)
        if string_5.playing:
            PlaySound(None, winsound.SND_PURGE)
            PlaySound(note, winsound.SND_ASYNC)
        else:
            PlaySound(note, winsound.SND_ASYNC)
    if is_pressed('enter'):
        fret = string_4.get_fret()
        note = string_4.get_note(fret)
        if string_4.playing:
            PlaySound(None, winsound.SND_PURGE)
            PlaySound(note, winsound.SND_ASYNC)
        else:
            PlaySound(note, winsound.SND_ASYNC)
    if is_pressed('bracketright'):
        fret = string_3.get_fret()
        note = string_3.get_note(fret)
        if string_3.playing:
            PlaySound(None, winsound.SND_PURGE)
            PlaySound(note, winsound.SND_ASYNC)
        else:
            PlaySound(note, winsound.SND_ASYNC)
    if is_pressed('backslash'):
        fret = string_2.get_fret()
        note = string_2.get_note(fret)
        if string_2.playing:
            PlaySound(None, winsound.SND_PURGE)
            PlaySound(note, winsound.SND_ASYNC)
        else:
            PlaySound(note, winsound.SND_ASYNC)
    if is_pressed('backspace'):
        fret = string_1.get_fret()
        note = string_1.get_note(fret)
        if string_1.playing:
            PlaySound(None, winsound.SND_PURGE)
            PlaySound(note, winsound.SND_ASYNC)
        else:
            PlaySound(note, winsound.SND_ASYNC)
    if is_pressed('space'):
        PlaySound(None, winsound.SND_PURGE)

