#include<stdio.h>
#include<string.h>

int main(int argc, char**argv) {
    char task[] = "is lazy";
    char user[10];
    printf("SEGFAULT incoming\n");
    strcpy(user,argv[1]);
    printf("%s %s\n",user,task);
    return 0;
}

