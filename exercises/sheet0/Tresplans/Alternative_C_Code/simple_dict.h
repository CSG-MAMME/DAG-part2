typedef struct Dict_t {
	int key;
    struct Dict_t *next;
} Dict;

Dict* dict_new();
void dict_add(Dict *root, int key);
int dict_has(Dict *root, int key);
void dict_traverse(Dict *root);
void dict_free(Dict *root);
