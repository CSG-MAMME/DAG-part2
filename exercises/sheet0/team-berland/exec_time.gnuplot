#!/usr/bin/gnuplot
load "../styles.inc"
set terminal postscript color eps enhanced font 22 size 5,5
set output 'mixture.eps'
set datafile separator ","
set bmargin 1.0
set tmargin 2.5
set lmargin 4.75
set rmargin 1.0
set yrange [0:10]
set xrange [0:359]
set xtics auto
set ytics auto
set grid y
set multiplot layout 3,1 rowsfirst

# Variables
LS=1 # Lines to skip
SP=10 #points to skip

# Plot 0
set title "{/bold Host 1 - Wrk2 Server and iPerf3 Client}" offset 0.0,-0.8
set key width -1.6
set key at screen 1.01,screen 0.99 vertical maxrows 1 Left sample 1.2 width -2.5 font "Arial ,20"
set obj 9 rect from screen 0.04, 0.96 to screen 0.99, 0.99 fs empty dt 3 behind
unset xtics
plot 'data/server.dat' \
       using 1:2 every LS with l ls 2101 notitle 'Cubic Kollaps',\
    '' using 1:2 every SP with p ls 2101 notitle 'Cubic Kollaps',\
    '' using 1:3 every LS with l ls 2102 notitle 'Cubic Mininet', \
    '' using 1:3 every SP with p ls 2102 notitle 'Cubic Mininet', \
    '' using 1:4 every LS with l ls 2103 notitle 'Reno Kollaps', \
    '' using 1:4 every SP with p ls 2103 notitle 'Reno Kollaps', \
    '' using 1:5 every LS with l ls 2104 notitle 'Reno Mininet',\
    '' using 1:5 every SP with p ls 2104 notitle 'Reno Mininet',\
	10000000\
		w lp ls 2101 title 'Cubic Kollaps',\
	10000000\
		w lp ls 2102 title 'Cubic Mininet',\
	10000000\
		w lp ls 2103 title 'Reno Kollaps',\
	10000000\
		w lp ls 2104 title 'Reno Mininet'

# Plot 1
set title "{/bold Host 2 - Wrk2 Client (Running from 120s to 240s)}" offset 0.0,-0.8
set ylabel "Deviation from baseline (%)" offset 1.75,0
set tmargin 1
unset key
unset xtics
plot 'data/client1.dat' \
	   using 1:2 every LS with l ls 2101 notitle 'Cubic Kollaps',\
	'' using 1:2 every SP with p ls 2101 notitle 'Cubic Kollaps',\
	'' using 1:3 every LS with l ls 2102 notitle 'Cubic Mininet', \
	'' using 1:3 every SP with p ls 2102 notitle 'Cubic Mininet', \
	'' using 1:4 every LS with l ls 2103 notitle 'Reno Kollaps', \
	'' using 1:4 every SP with p ls 2103 notitle 'Reno Kollaps', \
	'' using 1:5 every LS with l ls 2104 notitle 'Reno Mininet',\
	'' using 1:5 every SP with p ls 2104 notitle 'Reno Mininet',\
	10000000\
		w lp ls 2101 title 'Cubic Kollaps',\
	10000000\
		w lp ls 2102 title 'Cubic Mininet',\
	10000000\
		w lp ls 2103 title 'Reno Kollaps',\
	10000000\
		w lp ls 2104 title 'Reno Mininet'

# Plot 2
set title "{/bold Host 3 - iPerf3 Server}" offset 0.0,-0.8
unset key
unset ylabel
set tmargin 1
set xtics
set bmargin 3.0
set xlabel "Time (s)" offset 0,0.5
plot 'data/client2.dat' \
   	   using 1:2 every LS with l ls 2101 notitle 'Cubic Kollaps',\
	'' using 1:2 every SP with p ls 2101 notitle 'Cubic Kollaps',\
	'' using 1:3 every LS with l ls 2102 notitle 'Cubic Mininet', \
	'' using 1:3 every SP with p ls 2102 notitle 'Cubic Mininet', \
	'' using 1:4 every LS with l ls 2103 notitle 'Reno Kollaps', \
	'' using 1:4 every SP with p ls 2103 notitle 'Reno Kollaps', \
	'' using 1:5 every LS with l ls 2104 notitle 'Reno Mininet',\
	'' using 1:5 every SP with p ls 2104 notitle 'Reno Mininet',\
	10000000\
		w lp ls 2101 title 'Cubic Kollaps',\
	10000000\
		w lp ls 2102 title 'Cubic Mininet',\
	10000000\
		w lp ls 2103 title 'Reno Kollaps',\
	10000000\
		w lp ls 2104 title 'Reno Mininet'

unset multiplot
!epstopdf 'mixture.eps'
!rm 'mixture.eps'
