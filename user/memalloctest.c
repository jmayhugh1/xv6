#include "kernel/types.h"
#include "user/user.h"

struct A
{
  char a; // 1 btye
  int x; // 4 bytes
  char b; // 1 byte
};

// struct B has a suze of 4 + 1 + 1 + 2 (padding to mke it a multiple of 4)
struct B
{
  int x; // 4 bytes
  char a; // 1 bytes
  char b; // 1 btye
};
int main(int argc, char *argv[])
{

  struct A buffA[256];
  struct B buffB[256];

  printf("The size of struct A is %lu\n", sizeof(buffA[0]));
  printf("The size of struct B is %lu\n", sizeof(buffB[0]));

  printf("The size of a 256 length array of A is %lu\n", sizeof(buffA));
  printf("The size of a 256 length array of B is %lu\n", sizeof(buffB));

  return 0;
}