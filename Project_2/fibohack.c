#include <stdio.h>
#include <string.h>

char buffer[8];
int val1 = 0;
int val2 = 0;


int fibonacci(int i) {
    printf("%d\n", i);
    if (i == 0) {
	return 0;
    }
    if (i == 1) {
	return 1;
    }
    return fibonacci(i-1) + fibonacci(i-2);	

}

int main(int argc, char **argv){
    int i = 8;
    printf("fib(%d) = %d\n", i, fibonacci(i));
    //strcpy(buffer,argv[1]);
    //printf("val1 = %d, val2 = %d\n", val1, val2);
    return 0;
}

