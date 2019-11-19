#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "simple_dict.h"

Dict *
dict_new()
{
	Dict *dict = (Dict *) malloc(sizeof(Dict));
	assert(dict != NULL);
	dict->key = -1;
	dict->next = NULL;
	return dict;
}

void
dict_add(Dict *root, int key)
{
	Dict *dict = root;
	if (dict->key != -1) {
		while (dict->next != NULL) {
			dict = dict->next;
		}

		Dict *nextEntry = dict_new();
		dict->next = nextEntry;
		dict = dict->next;
	}

	dict->key = key;
}

int
dict_has(Dict *root, int key)
{
	if (root->key == -1) {
		return 0;
	}

	Dict *dict = root;
	while (dict != NULL) {
		if (dict->key == key) {
			return 1;
		}
		dict = dict->next;
	}

	return 0;
}


void
dict_traverse(Dict *root)
{
	if (root->key == -1) {
		return;
	}

	Dict *dict = root;

	while (dict != NULL) {
		printf("%d ", dict->key);
		dict = dict->next;
	}
	puts("");
	return;
}


void
dict_free(Dict *root)
{
	if (root == NULL) {
		return;
	}

	Dict *dict = root;
	Dict *temp;
	while (dict != NULL) {
		temp = dict;
		dict = dict->next;
		free(temp);
	}
}
