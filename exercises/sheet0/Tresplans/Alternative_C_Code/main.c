#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#include "simple_dict.h"


#define BUFFER_SIZE 256


void parse_file(FILE *file, Dict *dict, int size);
int compare_bases(Dict *dict);
int compare_pair(int b1, int b2, Dict *dict);


int
main(int argc, char* argv[])
{
	if (argc < 2) {
		printf("Usage: %s FILE(S)\n", argv[0]);
		return 1;
	}

	FILE *file;
	Dict *dict;
	clock_t start;
	double cpu_time_used;
	for (int i = 1; i < argc; i++) {
		file = fopen(argv[i], "r");
	    
		if (file == NULL) {
		 	printf("File does not exist.");
		 	return 1;
		}
	
		/* Obtain a dictionary with the  */
		dict = dict_new();
		parse_file(file, dict, BUFFER_SIZE);

		puts(argv[i]);
		start = clock();
		if (compare_bases(dict) < 0) {
			puts("No matroid.");
		} else {
			puts("Matroid.");
		}
		printf("%f seconds\n\n", ((double) clock() - start) / CLOCKS_PER_SEC); 
		dict_free(dict);
		dict = NULL;
		fclose(file);
		file = NULL;
	}

clean:
	if (dict != NULL) {
		dict_free(dict);
	}

	if (file != NULL) {
		fclose(file);
	}

	return 0;
}


void
parse_file(FILE *file, Dict *dict, int size)
{
	int i, h;
	char line[size];
	while (fgets(line, sizeof(line), file)) {
		/* Check if line starts with # (comment). */
	   	if (line[0] == '#') {
			continue; /* Skip line. */
		}

		h  = 0;
		char *num;
		num = strtok (line, " ");
		while (num != NULL) {
			h |= 1 << atoi(num);
			num = strtok(NULL, " ");
		}
		dict_add(dict, h);
	}
}


int
compare_bases(Dict *dict)
{
	Dict *b1 = dict;
	Dict *b2;
	while (b1 != NULL) {
		b2 = dict;
		while (b2 != NULL) {
			if (b1->key == b2->key) {
				b2 = b2->next;
				continue;
			}

			if (compare_pair(b1->key, b2->key, dict) < 0) {
				return -1;
			}
			b2 = b2->next;
		}
		b1 = b1->next;
	}

	return 0;
}


int
compare_pair(int b1, int b2, Dict *dict)
{
	int x = b1 & ~b2;
	int y = b2 & ~b1;

	int match;
	for (int i = 0; i < sizeof(int) * 8; i++) {
		match = 0;
		if (!(1 << i & x)) {
			continue;
		}
		int j;
		for (j = 0; j < sizeof(int) * 8; j++) {
			if (!(1 << j & y)) {
				continue;
			}

			if (dict_has(dict, b1 & ~(1 << i) | (1 << j))) {
				match = 1;
				break;
			}
		}

		if (!match) {
			return -1;
		}
	}
	return 0;
}
