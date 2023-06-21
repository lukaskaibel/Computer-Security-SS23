#!/usr/bin/perl

# Create a string with 257 'A's
my $str = 'A' x 257;

# Execute the C program with the string as an argument
system("./offbyone", $str);