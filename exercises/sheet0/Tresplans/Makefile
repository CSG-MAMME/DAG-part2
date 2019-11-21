CC="tcc"
TARGET="executable"

all: output_info python_code c_code


output_info:
	@echo "# Output structure:"
	@echo "FILENAME -> OUTPUT"
	@echo "NUMBER OF ELLAPSED_SECONDS"
	@echo ""

python_code:
	@echo "# Python results"
	python main.py ../matroid-or-not/*.bases

c_code:
	@echo "# C results"
	${CC} -o ${TARGET} main.c
	./${TARGET} ../matroid-or-not/*.bases
