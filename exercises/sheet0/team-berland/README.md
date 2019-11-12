### Team Bearland - Sheet 0

This repo contains the source code for both, `C++` and `Python3`, implementations of the stated problem under the `\coding\` directory. To compile and run the code `cd into it` and run:
```
./matroid-or-not.sh
```

Three different result files will be generated: `results.txt` containing a summary of the execution, and `cpp.dat` and `py3.dat` with the parsed results to feed the `gnuplot` script.

To replicate the plots included in the report, run, in this directory:
```
gnuplot exec_time.gnuplot
```
and `evince exec_time.pdf` (or any other PDF viewer) to visualize the results.
