echo "Compiling"
g++ matroid-or-not.cc -std=c++11 -Wall -O2 -o matroid-or-not.exe
echo "Running C++"
ls ../../matroid-or-not/ | ./matroid-or-not.exe
echo "Running Python3"
ls ../../matroid-or-not/ | ./matroid-or-not.py
echo "Done"