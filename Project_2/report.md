# Report_prog1.txt

## Problem

The initial problem in `prog1.c` is a buffer overflow vulnerability caused by the `strcpy` function not checking the bounds of the input argument.

## Solution

To exploit this buffer overflow, we can input a string longer than the buffer can hold. By doing so, we can override the values of the local variables declared after the buffer.

This overflow is achieved by entering a string of 8 'A' characters, followed by specific 4-character sequences to overwrite two 4-byte integers. As an example, we used the following command to achieve the buffer overflow:

```bash
./prog1 "AAAAAAAAGoblinJr"
```

To find suitable strings that would be interpreted as the required integers, we interpreted the integer values as strings. The final solutions are:

- GoblinJr
- GonnaCry
- GIVERENT
- Spiderma

## Observations

Interestingly, despite enabling flags like `-z execstack` and `-fno-stack-protector`, we observed no difference in the execution of the program, indicating that the buffer overflow could be performed regardless of these protections.

---

# Report_prog2.txt

## Problem

The problem in `prog2.c` arises from the fact that the program attempts to access the second argument passed (`argv[1]`) without first checking if it exists. This leads to a segmentation fault whenever the program is run without any arguments.

## Solution

The segmentation fault can be avoided by simply providing an argument when running the program. If the length of this argument is 9 characters or less, the output is "[arg1] is lazy". If the argument is longer than 9 characters, the first 10 characters of the argument will be printed twice. This is due to the argument overriding the string "task", which should have been printed in the output.

Here's how to avoid the segmentation fault:

```bash
./prog2 "1234567890HALLO"
```

## Observations

This solution and the resulting output shed light on how `strcpy` function behaves when there is a string size overflow. The longer string has overridden the expected output, thus leading to an unexpected program behavior.

---

# Report_prog3.txt

## Problem

The `prog3.c` program allows us to showcase a typical stack smashing exploit. This occurs when an attacker provides input that is longer than the buffer size, causing it to overflow and overwrite the return address in the stack.

## Solution

In this case, we can overflow the buffer and change the return address to the `smash` function's address. We create this overflow with the string "thisisjustaninnocentbufferhihi:)@", which when passed as an argument to `prog3.c`, causes a jump to the `smash` function.

This can be achieved by the following command:

```bash
./prog3 "thisisjustaninnocentbufferhihi:)@"
```

## Observations

This experiment demonstrates the potential security risks that come with buffer overflows. An attacker can manipulate the control flow of the program and execute arbitrary code by overwriting the return address on the stack.

---

# Report_offbyone.txt

## Problem

The `offbyone.c` program contains a typical "off by one" error. In the `func` function, a buffer of size 256 is allocated, but the loop is allowed to iterate 256 times, causing the index to reach 256 (0-based index). This results in a write beyond the allocated buffer space, which can lead to undefined behavior and potential security risks.

## Solution

To exploit this error, we create an input of 257 'A' characters, causing the buffer to overflow. We created a Perl script `offbyone_stacksmash.pl` to generate the overflow:

```bash
perl offbyone_stacksmash.pl
```

## Observations

This highlights the importance of proper boundary checking in programs. A small error like this one ("off by one") can lead to serious vulnerabilities. In this case, an overflow was caused that could potentially be exploited to execute arbitrary code.
