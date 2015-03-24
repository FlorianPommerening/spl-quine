#!/usr/bin/python

import spl.constants
from spl.generated import random_assignment_command, random_print_char_command, random_value_test_command, \
    random_return_to_scene_command, random_conditional_proceed_to_scene_command
import spl.tokens
import spl.utilities

import sys
from Frame import *

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
    codeblock += ["\t" + random_assignment_command(spl.constants.NUMBERS[ord(char)])]
    codeblock += ["\t" + random_print_char_command()]
    character_no = 1 - character_no

codeblock += [code_block_reverse_stack]

#<auto>
#Juliet:
#	Remember
#</auto>

for char in "Juliet:\n\tRemember ":
    codeblock += ["\t" + random_assignment_command(spl.constants.NUMBERS[ord(char)])]
    codeblock += ["\t" + random_print_char_command()]

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
    codeblock += ["\t" + random_value_test_command(spl.constants.NUMBERS[key])]
    codeblock += ["\t" + random_conditional_proceed_to_scene_command(scene_number)]

codeblock += [code_block_act_3_scene_2]

#<auto>
#\n
#Capulet:
#	You are as worried as the sum of yourself and the son.
#</auto>


for char in "\nCapulet:\n\tYou are as worried as the sum of yourself and the son.":
    codeblock += ["\t" + random_assignment_command(spl.constants.NUMBERS[ord(char)])]
    codeblock += ["\t" + random_print_char_command()]

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
        codeblock += ["\t" + random_assignment_command(spl.constants.NUMBERS[ord(char)])]
        codeblock += ["\t" + random_print_char_command()]
    codeblock += ["\t" + random_return_to_scene_command("II")]
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
