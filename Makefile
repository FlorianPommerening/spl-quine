SPLPATH = ../spl/spl

# compiler commands
CC    = gcc
SPL2C = $(SPLPATH)/bin/spl2c

# compiler flags
CCFLAGS      = -O2 -Wall -Wno-unused
INCLUDEFLAGS = -I$(SPLPATH)/include
LDFLAGS      = -L$(SPLPATH)/lib -lspl -lm

.PHONY: default spl test
default: splquine

spl: splquine.spl
splquine.spl:
	./bootstrap.py > splquine.spl

splquine.c: splquine.spl
	$(SPL2C) < $< > $@

splquine.o: splquine.c
	$(CC) $(CCFLAGS) $(INCLUDEFLAGS) -c $<

splquine: splquine.o
	$(CC) $(CCFLAGS) $^ $(LDFLAGS) -o $@

test: splquine.out
splquine.out: splquine
	./splquine > splquine.out

splquine.diff: splquine.spl splquine.out
	diff splquine.spl splquine.out > splquine.diff

# clean-up funtion
.PHONY: clean
clean:
	rm -f *~ *.o *.c *.spl splquine
