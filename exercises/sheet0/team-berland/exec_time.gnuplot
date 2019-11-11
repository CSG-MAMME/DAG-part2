#!/usr/bin/gnuplot
load "styles.inc"
set terminal postscript color eps enhanced font 22 #size 5,5
set output 'exec_time.eps'
set datafile separator " "
set boxwidth 0.8
set bmargin 4
set style data histograms
set style fill solid 1.0 border -1
#set xrange [0:359]
set xtics rotate by -45 offset 0.0, 0.0 font ",12"
set yrange [0:5]
set ylabel "C++ Execution Time [s]" offset 0.0, 0.0
set y2range [0:250]
set y2label "Python3 Execution Time [s]" offset -1.0, 0.0 rotate by -90
set ytics nomirror
set y2tics 50
set grid y
set key left

# Plot 0
set title "{/bold Matroid Checking Running Time C++ vs Python3}" #offset 0.0,-0.8
#set key width 
#set key at screen 0.5,screen 1.00 vertical maxrows 1 Left reverse sample 1.2 width -2.5 font "Arial ,20"
#plot './src/exec_times.dat' \
#       using 1:3 with boxes title 'C++',\
#    '' using 1:2 with boxes title 'Python 3'
plot './src/exec_times.dat' using 3 title 'C++' axis x1y1, \
    '' using 2:xticlabels(1) title 'Python 3' axis x1y2

!epstopdf 'exec_time.eps'
!rm 'exec_time.eps'
