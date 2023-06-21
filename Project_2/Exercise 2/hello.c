#include <stdio.h>
#include <string.h>


void write_buf(char *str) {
   char buf[32];
   strcpy(buf, str);
}

int main(int argc, char **argv) {
  if (argc <= 1) {
    printf("Missing argument. Please provide an input string.");
    return -1;
  }
  write_buf(argv[1]);
  return 0;
}
