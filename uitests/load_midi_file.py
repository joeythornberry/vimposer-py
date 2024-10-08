from config.DefaultFrontend import Frontend 
from vimposercore.VimposerAPI import VimposerAPI
from vimposercore.KeyboardManager import KeyboardManager

from vimposermidi.MidiViewport import MidiViewport
from vimposerparsing.TicksPerCharCalculator import TicksPerCharCalculator
from vimposerparsing.parse_midi_file import parse_midi_file
from config import config

v = VimposerAPI(Frontend(), MidiViewport())

config.init(v)

def save_note_callback(p: int, x: int, l: int, track: int) -> int:
    if len(v.midi_manager.track_midi_manager.tracks) <= track:
        v.create_track(p, x, l)
        return 0
    else:
        v.midi_manager.new_note(p, x, l, track, False)
        return 0

parse_midi_file(
        "MIDI/bwv1052a.mid",
        save_note_callback,
        TicksPerCharCalculator(12)
        )

v.km.listen(v.midi_manager.midi_window.frontend.s.getkey)
v.midi_manager.midi_window.frontend.close()
