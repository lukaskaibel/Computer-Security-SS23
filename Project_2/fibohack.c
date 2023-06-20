#include <stdio.h>
#include <string.h>

char buffer[8];
int val1 = 0;
int val2 = 0;

// TODO: Not done yet

int main(int argc, char **argv){

    strcpy(buffer,argv[1]);
    printf("val1 = %d, val2 = %d\n", val1, val2);
    return 0;
}

