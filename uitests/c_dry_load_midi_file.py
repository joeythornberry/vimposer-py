from sys import argv

from vimposerparsing.open_midi_file import open_midi_file

def save_note_callback(p: int, x: int, l: int, track: int, velocity: int, instrument: int):
    print(f"saving note {p=} {x=} {l=} {track=} {velocity=} {instrument=}")

def save_tempo_callback(new_tempo: int):
    print(f"saving tempo {new_tempo=}")

open_midi_file(
        f"{argv[1]}",
        save_note_callback,
        save_tempo_callback,
        12
        )
