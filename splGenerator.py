#!/usr/bin/python

import spl.constants
import spl.tokens
import spl.utilities

import sys
from Frame import *
from random import choice

sys.stdout = open("test.spl", "w")

print(prefix)

# create datastack
# <auto>
#Juliet:
#	Rember the sum of ...
#Capulet:
#	You are as worried as the sum of yourself and the son.
#</auto>
#done after the definition of codeblock

codeblock = [code_block_print_prefix]

#<auto>
#Montague:
#	You are as ... as .. .
#	Speak your Mind.
#Capulet:
#	You are as ... as .. .
#	Speak your Mind.
#</auto>

characters = ["Capulet:", "Montague:"]
character_no = 1
youareas = ["You are as ", "Thou art as "]
for char in prefix:
    codeblock += [characters[character_no]]
    line = ["\t", choice(youareas), choice(spl.tokens.adjectives), " as ", spl.constants.NUMBERS[ord(char)]]
    codeblock += ["".join(line)]
    codeblock += ["\tSpeak your mind."]
    character_no = 1 - character_no

codeblock += [code_block_reverse_stack]

#<auto>
#Juliet:
#	Rember 
#</auto>

for char in "Juliet:\n\tRemember ":
    line = ["\t", choice(youareas), choice(spl.tokens.adjectives), " as ", spl.constants.NUMBERS[ord(char)]]
    codeblock += ["".join(line)]
    codeblock += ["\tSpeak your mind."]

codeblock += ["\tYou are as villainous as Montague."]

#<auto>
#	You are as good as Montague
#	Are you as good as <codierung von a>
#	If so let us proceed to scene <scene von a>
#	...
#</auto>

ordered_keys = sorted(spl.constants.NUMBERS.keys())
scene_numbers = []

for i in range(len(ordered_keys)):
    scene_numbers.append(spl.utilities.scene_number(i + 3))

for scene_number, key in zip(scene_numbers, ordered_keys):
    line = ["\t", "Are you as ", choice(spl.tokens.adjectives), " as ", spl.constants.NUMBERS[key][:-1], "?"]
    codeblock += ["".join(line)]
    codeblock += ["\tIf so, let us proceed to scene " + scene_number + "."]

codeblock += [code_block_act_3_scene_2]

#<auto>
#\n
#Capulet:
#	You are as worried as the sum of yourself and the son.
#</auto>


for char in "\nCapulet:\n\tYou are as worried as the sum of yourself and the son.":
    line = ["\t", choice(youareas), choice(spl.tokens.adjectives), " as ", spl.constants.NUMBERS[ord(char)]]
    codeblock += ["".join(line)]
    codeblock += ["\tSpeak your mind."]

codeblock += [code_block_return_from_act_3]

#<auto>
#	Scene __: Even more accusations.
#
#Capulet:\n
# for char in codierung a 
#    You are as good as <codierung von char>.
#    Speak your mind.
#</auto>


for scene_number, key in zip(scene_numbers, ordered_keys):
    codeblock += ["\t\tScene " + scene_number + ": Even more accusations.\n"]
    codeblock += ["Capulet:"]
    for char in spl.constants.NUMBERS[key]:
        line = ["\t", choice(youareas), choice(spl.tokens.adjectives), " as ", spl.constants.NUMBERS[ord(char)]]
        codeblock += ["".join(line)]
        codeblock += ["\tSpeak your mind."]
    codeblock += ["\tLet us return to scene II.\n"]

codeblock += [code_block_act_4_scene_1]

code = "\n".join(codeblock)

for char in code:
    print("Juliet:")
    print("\tRemember " + spl.constants.NUMBERS[ord(char)])
    print("Capulet:")
    print("\tYou are as worried as the sum of yourself and the son.")

# create datastack
#<auto>
#Juliet:
#	Rember the sum of ...
#Capulet:
#	You are as worried as the sum of yourself and the son.
#</auto>


print(code)
