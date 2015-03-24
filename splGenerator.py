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
#	Remember the sum of ...
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

for char in prefix:
    codeblock += [characters[character_no]]
    line = ["\t", choice(spl.tokens.ASSIGNMENT_COMMANDS) % (choice(spl.tokens.ADJECTIVES), spl.constants.NUMBERS[ord(char)])]
    codeblock += ["".join(line)]
    codeblock += ["\t" + choice(spl.tokens.PRINT_CHAR_COMMANDS)]
    character_no = 1 - character_no

codeblock += [code_block_reverse_stack]

#<auto>
#Juliet:
#	Remember
#</auto>

for char in "Juliet:\n\tRemember ":
    line = ["\t", choice(spl.tokens.ASSIGNMENT_COMMANDS) % (choice(spl.tokens.ADJECTIVES), spl.constants.NUMBERS[ord(char)])]
    codeblock += ["".join(line)]
    codeblock += ["\t" + choice(spl.tokens.PRINT_CHAR_COMMANDS)]

codeblock += ["\tYou are as villainous as Montague."]

#<auto>
#	You are as good as Montague
#	Are you as good as <spl code of a>
#	If so let us proceed to scene <scene of a>
#	...
#</auto>

ordered_keys = sorted(spl.constants.NUMBERS.keys())
scene_numbers = []

for i in range(len(ordered_keys)):
    scene_numbers.append(spl.utilities.scene_number(i + 3))

for scene_number, key in zip(scene_numbers, ordered_keys):
    line = ["\t", choice(spl.tokens.VALUE_TEST_COMMANDS) % (choice(spl.tokens.ADJECTIVES), spl.constants.NUMBERS[key])]
    codeblock += ["".join(line)]
    codeblock += ["\t" % choice(spl.tokens.CONDITIONAL_PROCEED_TO_SCENE_COMMANDS) % scene_number]

codeblock += [code_block_act_3_scene_2]

#<auto>
#\n
#Capulet:
#	You are as worried as the sum of yourself and the son.
#</auto>


for char in "\nCapulet:\n\tYou are as worried as the sum of yourself and the son.":
    line = ["\t", choice(spl.tokens.ASSIGNMENT_COMMANDS) % (choice(spl.tokens.ADJECTIVES), spl.constants.NUMBERS[ord(char)])]
    codeblock += ["".join(line)]
    codeblock += ["\t" + choice(spl.tokens.PRINT_CHAR_COMMANDS)]

codeblock += [code_block_return_from_act_3]

#<auto>
#	Scene __: Even more accusations.
#
#Capulet:\n
# for char in "<spl code of a>"
#    You are as good as <spl code of char>.
#    Speak your mind.
#</auto>


for scene_number, key in zip(scene_numbers, ordered_keys):
    codeblock += ["\t\tScene " + scene_number + ": Even more accusations."]
    codeblock += [""]
    codeblock += ["Capulet:"]
    for char in spl.constants.NUMBERS[key]:
        line = ["\t", choice(spl.tokens.ASSIGNMENT_COMMANDS) % (choice(spl.tokens.ADJECTIVES), spl.constants.NUMBERS[ord(char)])]
        codeblock += ["".join(line)]
        codeblock += ["\t", choice(spl.tokens.PRINT_CHAR_COMMANDS)]
    codeblock += ["\t" + choice(spl.tokens.RETURN_TO_SCENE_COMMANDS) % "II"]
    codeblock += [""]

codeblock += [code_block_act_4_scene_1]

code = "\n".join(codeblock)

for char in code:
    print("Juliet:")
    print("\tRemember %s." % spl.constants.NUMBERS[ord(char)])
    print("Capulet:")
    print("\tYou are as worried as the sum of yourself and the son.")

# create datastack
#<auto>
#Juliet:
#	Remember the sum of ...
#Capulet:
#	You are as worried as the sum of yourself and the son.
#</auto>


print(code)
