exercises = ex1 ex2 ex3 ex4

all:
	for d in $(exercises); \
	do \
		$(MAKE) --directory=$$d; \
	done

clean:
	for d in $(exercises); \
	do \
		$(MAKE) clean --directory=$$d; \
	done


