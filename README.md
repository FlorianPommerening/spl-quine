# README #

# What is this?

This is a quine, a program that reproduces its own source code, in the
[Shakespeare Programming Language (SPL)](http://shakespearelang.sourceforge.net/).
Well, actually, it is a python bootstrapper which generates the SPL quine.


# Why did you do it?

  1. Why not?
  2. Quines are possible in every Turing-complete programming language
     and we were interested to see what a quine would look like in SPL.
     As far as we know, there is no other quine in SPL yet, so we had
     to write one ourselves.
  3. We needed an example for a seminar.


# How do I run it?

You can generate the quine by calling `make spl`. This step should only
require Python and generates a file called `splquine.spl` which contains
the quine source code.

To compile and run it, you are going to need a version of `spl2c` and
`gcc`. The official release of SPL 1.2.1 still contains a few minor bugs.
Kyle Cartmell [forked the code](https://bitbucket.org/kcartmell/marlowe) 
and fixed some of them, and we [forked his code again](https://bitbucket.org/FlorianPommerening/spl-fixes)
for some additional fixes.
Clone our version parallel to this clone, build and install (`make
install`) spl there. Our Makefile looks for spl2c in `../spl/spl/spl2c`
but you can change this path, if your version is somewhere else.

Once you have spl2c set up, use `make splquine` to generate the binary
splquine. This binary is the compiled version of `splquine.spl` and
output its source code.


# How does it work?

The repository contains some slides about this. They are in German but
the interesting bit (slide 21/31 or page 25/35) is English pseudo code.

The quine is made up of three parts: the prefix, the code, and the data.

The prefix part starts the program and sets everything so the next
segment can define elements of a list.
(think: `data = [`)

The code part has four things to do:

  1. finalize the list opened in the prefix.
     (think: `];`)
  2. print the prefix.
     (think: `print('data = [');`)
  3. loop through the data once. For each element, print the code that
     would generate the list element.
     (think: `for c in data: print(ord(c) + ', ');`)
  4. loop through the data again. For each element, print it as a
     character.
     (think: `for c in data: print(chr(c));`)

The data part adds one element to the list for each letter in the code.

it is easy to see that the prefix does not depend on anything, the code
only depends on the prefix (in step 2.), and the data depends only on
the code, so we can actually generate the parts in this order. We then
write them to a file in the order: prefix, data, code.

Executing this program will start a list (prefix), add some elements to
it, then print the prefix, regenerate the code that created the list
(no matter what the list contains), and then print the elements of the
list. Since the list contains the code, this will regenerate the whole
program.

The hard part for SPL is step 3. of the code part: here we need to
generate SPL code that (when executed) adds a certain character to a
list (stack in this case). We achieved this with a large switch/case
that jumps to the correct "function" for each symbol. The function then
generates (letter by letter) the statement needed to add this symbol to
the list. Every new symbol needs its own function of a few hundred
lines and every character in those lines needs to be encoded with one
line in the code part. This is the main reason for the large size of
the quine.

# Who are you?

We are Florian Pommerening and Thomas Mayer. The beautiful esoteric
programming language SPL was developed by Karl Wiberg and Jon Åslund.

# When did you write it?

We attended a seminar on self-reference in 2009 and Florian's topic was
about quines. We had previously used SPL for some homework assignments
(generating Mersenne pseudo primes and a DPLL SAT solver). For some
reason both exercises changed from "use a programming language of your
choice" to "use a programming language approved by your tutor"
afterwards.

We implemented the quine as an example for the seminaran tested small
parts of it, but it took too long to translate/compile the whole thing.
Our Makefile back then automated the process of translating to C++,
compiling and cleaning up the temporary files. We wanted to make sure
that our program actually was a quine, so we took an old laptop, typed
in `make; make clean` and let it run for three days. We then noticed
that adding `; make clean` was a bit too optimistic: after three days
of translating the SPL source code to C++, the C++ compiler exhausted
the 2GB of memory on the laptop almost immediately, `make` failed, and
`make clean` deleted the result of the three day computation. We didn't
have time to try again before the seminar.

Years later, Florian had access to a compute cluster, where we could
run the compilation with 64 GB RAM (we ended up needing 56 GB of that).
We could finally verify that we had, indeed, written a quine. Since
then, we made some improvements to the code to the point where it now
compiles in 10 minutes using less than 4GB RAM on a regular PC (see
VERSIONS).