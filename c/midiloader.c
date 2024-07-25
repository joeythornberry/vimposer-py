#include <stdint.h>
#include <stdlib.h>
#include <stdio.h>
#include <wchar.h>

char * wchar_t_to_const_char(wchar_t * wchar_t_string) {
	size_t len = wcslen(wchar_t_string);
	char * char_string = malloc(len + 1);
	for (uint8_t i = 0; i < len; i++) {
		char_string[i] = wchar_t_string[i];
	}
	char_string[len] = '\0';
	return char_string;
}

const char read_bit(uint8_t input, uint8_t bit_to_read) {
	uint8_t bit = input & (1 << bit_to_read);
	if (bit == 0) {
		return '0';
	} else {
		return '1';
	}
}

void binary_repr(char dest[8], uint8_t input) {
	for(uint8_t i = 0; i < 8; i++) {
		dest[i] = read_bit(input, i);
	}
}

const char * parse_midi_file(wchar_t * filename_wchar_p, int (*save_note)(int, int, int, int)) {

	char * filename = wchar_t_to_const_char(filename_wchar_p);
	printf("conversion func attempt: %s\n", filename);

	FILE * midifile;
	midifile = fopen(filename, "rb");
	if (midifile == NULL) {
		return "Failed to open file.";
	}

	char bin_repr_buffer[8];
	char first = getc(midifile);
	binary_repr(bin_repr_buffer, first);
	printf("first: %s\n", bin_repr_buffer);
	printf("first_char: %c\n", first);

	char second = getc(midifile);
	binary_repr(bin_repr_buffer, second);
	printf("second: %s\n", bin_repr_buffer);
	printf("second_char: %c\n", second);

	//int note_save_result = save_note(-1,-1,-1,-1);

	fclose(midifile);

	free(filename);
	return "Midi parse successful.";
}

int dummy_save_note(int a, int b, int c, int d) {
	printf("saving note");
	return 0;
}

int main() {
	wchar_t * filename = L"../MIDI/d_minor_scale.mid";
	parse_midi_file(filename, *dummy_save_note);
}
