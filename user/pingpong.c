#include "kernel/types.h"
#include "user/user.h"

int main(int argc, char *argv[])
{
  int iterations = 10;
  int p2c[2];
  int c2p[2];
  int READ = 0;
  int WRITE = 1;

  if (pipe(p2c) < 0 || pipe(c2p) < 0)
  {
    fprintf(1, "unable to created a pipe");
    exit(1);
  }

  int pid = fork();

  if (pid == 0)
  {
    char msg1[] = "pong";
    char buff1[128];
    close(p2c[WRITE]);
    close(c2p[READ]);
    while (1)
    {
      if (read(p2c[READ], buff1, sizeof(buff1)) == 0)
        exit(0);
      printf("pid %d recieved %s\n", pid, buff1);
      write(c2p[WRITE], msg1, sizeof(msg1));
    }
  }
  else
  {
    char msg2[] = "ping";
    char buff2[128];
    close(c2p[WRITE]);
    close(p2c[READ]);
    while (iterations)
    {
      write(p2c[WRITE], msg2, sizeof(msg2));
      read(c2p[READ], buff2, sizeof(buff2));
      printf("pid %d recieved %s\n", pid, buff2);
      iterations--;
    }
    close(p2c[WRITE]);
  }

  exit(0);
}
