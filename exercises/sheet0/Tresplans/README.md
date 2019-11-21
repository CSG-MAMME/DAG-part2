# Tresplans Source Code

In this folder we present two codes to solve the same problem,
one in *Python 2 / 3* and the other in *C*.
Both codes have the same command line interface:
They read files from *stdin* and iterate over them checking if they form a matroid.
Both return the name of the files provided,
the result of checking if it contains a matroid,
and the time in seconds that took computing the result.

## Dependencies

The *Python* code has no external dependencies.

The *C* code has a dependency on **uthash** from Troy D. Hanson, a header contained in this folder.
Its license is *BSD revised*, so redistribution and use in source and binary forms,
with or without modification, are permitted just including a disclaimer (included in the source).

Also, non-POSIX-compliant implementations of *C* could require further dependencies.

## Alternative Code

We also have included an alternative implementation in *C*,
based in using linked lists that has higher computational complexity and is not commented at all.
It is a simpler implementation, so we kept it in case someone would like to take a look at it.
