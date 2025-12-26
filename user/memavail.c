#include "kernel/types.h"
#include "user/user.h"

int main(int argc, char *argv[])
{
  printf("There are %lu bytes of memory available\n", memavail());

  exit(0);
}