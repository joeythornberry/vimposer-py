import struct
minimal_midi_file = [0x4d, 0x54, 0x68, 0x64, 0x00, 0x00, 0x00, 0x06, 0x00, 0x01, 0x00, 0x01, 0x01, 0xe0, 0x4d, 0x54, 0x72, 0x6b, 0x00, 0x00, 0x00, 0x17, 0x00, 0xff, 0x51, 0x03, 0x07, 0xa1, 0x20, 0x00, 0xc0, 0x00, 0x00, 0x90, 0x3c, 0x64, 0x81, 0x70, 0x80, 0x3c, 0x00, 0x00, 0xff, 0x2f, 0x00]

def write_minimal_midi_file(filename: str):
    with open(filename, "wb") as f:
        f.write(struct.pack(f"{len(minimal_midi_file)}B", *minimal_midi_file))
