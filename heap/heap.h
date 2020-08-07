#ifndef __HEAP_H__
#define __HEAP_H__

typedef unsigned char byte;

struct Heap {
    int limit;
    byte* memory;
} Heap;

struct Heap newHeap(int limit);
void* allocate(byte space);
void deallocate(void* start);

#endif
