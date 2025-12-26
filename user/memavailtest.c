#include "kernel/types.h"
#include "kernel/stat.h"
#include "user/user.h"

int main(int argc, char *argv[])
{
  uint64 memafteralloc;
  uint64 memafterfree;
  uint64 initmem = memavail();

  printf("Mem before allocating %lu\n", initmem);
  char *buff = sbrk(8192);
  memset(buff, 0, sizeof(buff));
  memafteralloc = memavail();
  printf("Mem after allocating %lu\n", memafteralloc);
  sbrk(-8192);
  memafterfree = memavail();
  printf("Mem after freeing %lu\n", memafterfree);
  exit(0);
}