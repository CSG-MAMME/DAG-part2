#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#include "uthash.h"


#define BUFFER_SIZE 256


typedef struct Hash {
    int key;
    UT_hash_handle hh;
} Hash;


/* Add a new key to the hash table. */
void hash_add(Hash **hashTable, int key);

/* Look for an entry with the provided key in the hash table.
 * Return the struct if found, and NULL otherwise.
 */
Hash *hash_find(Hash **hashTable, int key);

/* Delete the hash table and free the memory. */
void hash_delete(Hash **hashTable);

/* Parse the provided file and save results in the hash table. */
void parse_file(FILE *file, Hash **hashTable, int size);

/* Iterate over all bases in the hash table and compare them by pairs.
 * Return 0 if bases form a matroid. Return -1 otherwise.
 */
int compare_bases(Hash **hashTable);

/* Compare a pair of bases.
 * Return 0 if bases satisfy the exchange axiom, return -1 otherwise.
 */
int compare_pair(int b1, int b2, Hash **hashTable);


int
main(int argc, char* argv[])
{
	if (argc < 2) {
		printf("Usage: %s FILE(S)\n", argv[0]);
		printf("Example: %s ../matroid-or-not/*bases\n", argv[0]);
		return 1;
	}

	FILE *file = NULL;
	Hash * hashTable = NULL;
	clock_t start;
	double cpu_time_used;
	for (int i = 1; i < argc; i++) {
		/* Open file. */
		file = fopen(argv[i], "r");
	    
		if (file == NULL) {
		 	printf("File does not exist.");
		 	return 1;
		}

		printf("%s -> ", argv[i]);
		
		start = clock();

		/* Obtain a dictionary with the  */
		parse_file(file, &hashTable, BUFFER_SIZE);

		/* Compare bases contained on the file. */
		if (HASH_COUNT(hashTable) == 0 || compare_bases(&hashTable) < 0) {
			puts("No matroid.");
		} else {
			puts("Matroid.");
		}
		printf("%f seconds\n\n", ((double) clock() - start) / CLOCKS_PER_SEC); 

		/* Free memory. */
		hash_delete(&hashTable);
		fclose(file);
		file = NULL;
	}

clean:
	if (hashTable != NULL) {
		hash_delete(&hashTable);
	}

	if (file != NULL) {
		fclose(file);
	}

	return 0;
}


void
hash_add(Hash **p_hashTable, int key) {
    Hash *s;
    /* Allocate memory for the new hash. */
    s = malloc(sizeof(Hash));
    s->key = key;
    /* Add new hash to the table. */
    HASH_ADD_INT( *p_hashTable, key, s );
}


Hash *
hash_find(Hash **p_hashTable, int key) {
    Hash *s;
    /* Search the key in the hash table. */
    HASH_FIND_INT( *p_hashTable, &key, s );
    return s;
}


void
hash_delete(Hash **p_hashTable) {
	Hash *current, *tmp;
	/* Iterate over the hash table. */
	HASH_ITER(hh, *p_hashTable, current, tmp) {
		/* Delete and advance. */
		HASH_DEL(*p_hashTable, current);
		/* Free memory. */
		free(current);
	}
}


void
parse_file(FILE *file, Hash **p_hashTable, int size)
{
	int h;
	char line[size];
	while (fgets(line, sizeof(line), file)) {
		/* Skip line if starts with '#' (comment). */
	   	if (line[0] == '#') {
			continue;
		}

		/* Put the hash variable to zero. */
		h  = 0;
		/* Create a pointer to store the numbers. */
		char *num;
		/* Split lines by ' ' and convert the tokens to integers.
		 * Shift a bit to the left the value of the integer found.
		 * Add the result to the hash variable.
		 */
		num = strtok (line, " ");
		while (num != NULL) {
			h |= 1 << atoi(num);
			num = strtok(NULL, " ");
		}
		/* Add a new entry on the hash table. */
		hash_add(p_hashTable, h);
	}
}


int
compare_bases(Hash **p_hashTable)
{
	/* Allocate pointers for hashes. */
	Hash *b1, *b2;

	/* Iterate over all bases. */
    for(b1 = *p_hashTable; b1 != NULL; b1 = b1->hh.next) {
    	for(b2 = *p_hashTable; b2 != NULL; b2 = b2->hh.next) {
    		/* Skip comparison if bases are the same. */
			if (b1 == b2) {
				continue;
			}
			/* Return -1 if the exchange axiom is not satisfied. */
			if (compare_pair(b1->key, b2->key, p_hashTable) < 0) {
				return -1;
			}
    	}
	}

	return 0;
}


int
compare_pair(int b1, int b2, Hash **p_hashTable)
{
	/* Compute x = bits in b1 not in b2 and y = bits in b1 not in b1. */
	int x = b1 & ~b2;
	int y = b2 & ~b1;

	int match;
	for (int i = 0; i < sizeof(int) * 8; i++) {
		match = 0;
		/* Just check the bits that are 1 in x. */
		if (!(1 << i & x)) {
			continue;
		}

		for (int j = 0; j < sizeof(int) * 8; j++) {
			/* Just check the bits that are 1 in y. */
			if (!(1 << j & y)) {
				continue;
			}

			/* Search for b1 \ {x} U {y} in the table. */
			if (hash_find(p_hashTable, b1 & ~(1 << i) | (1 << j))) {
				match = 1;
				break;
			}
		}
		/* Return -1 if b1 \ {x} U any y is not in the table of bases. */
		if (!match) {
			return -1;
		}
	}

	return 0;
}
