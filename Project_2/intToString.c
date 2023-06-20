#include <stdio.h>
#include <string.h>

int number = 1634562661;

int main(int argc, char **argv){
    // Interpret input integer as a string
    /*int number; 
    printf("Enter an integer: ");
    scanf("%d", &number); */
    char *string = (char *)&number; 
    printf("number as string = %s", string);
    return 0;
}

