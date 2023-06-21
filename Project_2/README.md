# Computer Security Project 2

### prog1.c

How to overflow, to create expected outputs:

- The program reads a string from the program arguments
- The string gets saved in a 8 bytes long buffer using the strcpy
- the problem is, that strcpy does not check the bounds of the argument
- That means, that longer strings also get copied in the buffer and thus, other variables may get overriden.
- This is exactly the case, as int val1 and int val2 are declared below the buffer
- As the local vars are saved on the stack and the stack grows downwards, the ints get overriden if we input a string > 8 bytes (characters)

So to achieve the expected outputs we just had to experiment, which strings get interpreted as the required ints.
For that we simply interpreted the ints as strings. As results, we got some nice strings:

Finally, to achieve the overflow, we used
./prog1 "AAAAAAAAGoblinJr"

- As you can see: 8xA to fill up the buffer, followed by 2x4 chars, to override the two 4 bytes ints

Analogue, for the other ints as well. Solutions:
GoblinJr
GonnaCry
GIVERENT
Spiderma

Does it work without flags enabled? Yes!
-z execstack
-> No difference, nothing is executed on stack anyways.
-fno-stack-protector
-> Interestingly, no canaries are modified. Probably because of simplicity of this approach. So it makes no difference.

### prog2.c

A segmentation fault in C is thrown, when a program attempts to read or write to a memory location that has not been allocated to it.
[datatrained.com/post/segmentation-fault-in-c/]
For this program a segfault is called when no arguments are passed to the program.
The reason is that argv[1] gets called in strcpy(), when no argument is passed.
We can bypass this by entering a string as first argument.
If the string is <= 9 chars, "[arg1] his lazy" gets printed
E.g.:
└─$ ./prog2 "123456789"  
SEGFAULT incoming
123456789 is lazy

If the string is > 9 chars, it overrides the string task, which leads to the argument being printed twice. (Expect the first 10 chars of it.)
E.g.:
└─$ ./prog2 "1234567890HALLO"
SEGFAULT incoming
1234567890HALLO HALLO

### prog3.c

Jump to the address of the `smash` function by overwriting the return address in the stack:

```sh
#! /bin/bash
gcc -o prog3 prog3.c
./prog3 "thisisjustaninnocentbufferhihi:)@"
```

It can be tested with the provided script `prog3_smash.sh`:

```sh
$ ./prog3_smash.sh
Access granted. Gonna cry?
You should have thought of that earlier.

```

### offbyone.c

The off by one error occurs because in the `func` function the input is copied into the buffer of size 256. However the loop iterates over 266, as `0 <= i <= 256`. The correct implementation of `func` should be `0 <= i < 256`.
Thats why the error is called off by one, as the programmer miscounted the amounts the loop will iterate, creating an error that iterates exactly once too often.

In order to exploit this with a stack smash we can create a perl script like `offbyone_stacksmash.pl` which when executed creates an input for `offbyone.c` with 257 A's, causing the buffer to overflow.
