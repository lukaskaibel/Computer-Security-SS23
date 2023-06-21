#include <stdio.h>

void func(char *str) {
    char buf[256];
    int i;

    // Overflow occurs here, as loop should only do i < 256
    for (i=0;i<=256;i++)
        buf[i] = str[i];
}

int main(int argc, char **argv) {
    func(argv[1]);
}