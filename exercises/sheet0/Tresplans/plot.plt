#!/usr/bin/gnuplot

set terminal epslatex 8 standalone
set output 'temp_plot.tex'
set title '\huge Running Time Benchmark'

set style fill solid
set boxwidth 0.9 absolute

set grid y
set logscale y

set ylabel '\Large Time in logarithmic scale (s)'
set key left top vertical Left

set xtics rotate by 45 right

plot "c.dat" using 2:xtic(1) with histogram title "C execution time",\
"python.dat" using 2:xtic(1) with histogram title "Python execution time"

set output

system('pdflatex temp_plot.tex && mv temp_plot.pdf Tresplans_exec_time.pdf && rm temp_plot*')
