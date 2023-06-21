# README.md

## Requirements

- gcc compiler to compile the C programs
- bash shell to run the shell scripts
- perl to execute the Perl scripts

## How to Run the BOF attacks

### prog1.c

1. Compile the program by running the command:

```bash
gcc -o prog1 prog1.c
```

2. Run the bash script provided:

```bash
./prog1.sh
```

### prog2.c

1. Compile the program by running the command:

```bash
gcc -o prog2 prog2.c
```

2. Run the bash script provided:

```bash
./prog2.sh
```

### prog3.c

1. Compile the program by running the command:

```bash
gcc -o prog3 prog3.c
```

2. Run the bash script provided:

```bash
./prog3_smash.sh
```

### offbyone.c

1. Compile the program by running the command:

```bash
gcc -o offbyone offbyone.c
```

2. Execute the perl script:

```bash
perl offbyone_stacksmash.pl
```

## Structure/Dependencies

Each folder contains a C source code file (.c) with a corresponding program name (e.g., `prog1.c`). The C programs demonstrate various programming pitfalls that can lead to security vulnerabilities.

Also included are shell scripts (e.g., `prog3_smash.sh`) or Perl scripts (e.g., `offbyone_stacksmash.pl`) which are used to exploit these vulnerabilities.
