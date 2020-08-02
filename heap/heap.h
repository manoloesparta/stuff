#ifndef __HEAP_H__
#define __HEAP_H__

struct Heap {
    int limit;
    unsigned char memory;
} Heap;

struct Heap newHeap(int limit);
void* mallocHeap(unsigned char bytes);
void freeHeap(void* start);

#endif