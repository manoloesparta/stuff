heap: main.o heap.o
	gcc main.o heap.o -o heap

main.o: main.c
	gcc -c main.c

heap.o: heap.c heap.h
	gcc -c heap.c

clean:
	rm *.o heap