CC="gcc"
TARGET="executable"

# Process all bases.
all: output_info py_code c_code

plot: py_data c_data
	gnuplot plot.plt

output_info:
	@echo "# Output structure:"
	@echo "FILENAME -> OUTPUT"
	@echo "NUMBER OF ELLAPSED_SECONDS"
	@echo ""

# Run the Python version with all bases.
py_code:
	@echo "# Python results"
	python main.py ../matroid-or-not/*.bases

# Run the C version with all bases
c_code:
	@echo "# C results"
	${CC} -o ${TARGET} -O3 main.c
	./${TARGET} ../matroid-or-not/*.bases

# Create a file containing the Python data for the plots.
py_data:
	python main.py ../matroid-or-not/*.txt\
		| awk '/^$$/ {next} {print $$1;}'\
		| xargs -I{} basename {}\
		| paste - -\
		> python.dat

# Create a file containing the C data for the plots.
c_data:
	${CC} -o ${TARGET} -O3 main.c
	./${TARGET} ../matroid-or-not/*.txt\
		| awk '/^$$/ {next} {print $$1;}'\
		| xargs -I{} basename {}\
		| paste - -\
		> c.dat

