CC = gcc 
FLAGS = -std=c11 -g -Wall -Wextra -pedantic-errors

heap: main.o heap.o
	${CC} ${FLAGS} main.o heap.o -o heap

main.o: main.c
	${CC} ${FLAGS} -c main.c

heap.o: heap.c heap.h
	${CC} ${FLAGS} -c heap.c

clean:
	rm *.o heap
