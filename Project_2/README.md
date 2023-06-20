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

