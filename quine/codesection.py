import itertools
from .handwritten import CODE_PRINT_PREFIX_START, CODE_PRINT_PREFIX_CHARACTERS, NUMBERS, code_block_reverse_stack, \
    code_block_act_3_scene_2, code_block_act_4_scene_1, code_block_return_from_act_3, \
    DATA_PUSH_COMMAND_BEFORE, DATA_PUSH_COMMAND_AFTER
import spl.utilities
from spl.generated import random_assignment_command, random_print_char_command, random_value_test_command, \
    random_conditional_proceed_to_scene_command, random_return_to_scene_command


def generate(prefix):
    """
    The code section of the quine includes everything from the end of the
    data definition until the last line. The code section only depends on the
    content of the prefix section, not on the content of the data section.

    In this section we will print:
        1) The prefix section: This will be a hard-coded part of the program
           section.
        2) The data section: using the data on the stack, we can recreate the
           code that pushes the data on the stack.
        3) The code section: we just print the data letter by letter. If the
           data encodes the code section (which we can do, because the code
           section is independent of the data section), this will recreate the
           code.
    See comments in handwritten.py for details.

    :return: a string containing the full source code for the code section.
    """
    code_lines = [CODE_PRINT_PREFIX_START]

    # Hard-code printing commands for the prefix
    actors = CODE_PRINT_PREFIX_CHARACTERS
    for actor, symbol in zip(itertools.cycle(actors), prefix):
        code_lines += [actor + ":"]
        number = NUMBERS[ord(symbol)]
        code_lines += ["\t" + random_assignment_command(number)]
        code_lines += ["\t" + random_print_char_command()]

    code_lines += [code_block_reverse_stack]

    #<auto>
    #Juliet:
    #	Remember
    #</auto>
    for symbol in DATA_PUSH_COMMAND_BEFORE:
        number = NUMBERS[ord(symbol)]
        code_lines += ["\t" + random_assignment_command(number)]
        code_lines += ["\t" + random_print_char_command()]

    code_lines += ["\tYou are as villainous as Montague."]

    #<auto>
    #	You are as good as Montague
    #	Are you as good as <spl code of a>
    #	If so let us proceed to scene <scene of a>
    #	...
    #</auto>

    ordered_keys = sorted(NUMBERS.keys())
    scene_numbers = []

    for i in range(len(ordered_keys)):
        scene_numbers.append(spl.utilities.scene_number(i + 3))

    for scene_number, key in zip(scene_numbers, ordered_keys):
        code_lines += ["\t" + random_value_test_command(NUMBERS[key])]
        code_lines += ["\t" + random_conditional_proceed_to_scene_command(scene_number)]

    code_lines += [code_block_act_3_scene_2]

    #<auto>
    #.\n
    #Capulet:
    #	You are as worried as the sum of yourself and the son.
    #</auto>
    for symbol in DATA_PUSH_COMMAND_AFTER:
        number = NUMBERS[ord(symbol)]
        code_lines += ["\t" + random_assignment_command(number)]
        code_lines += ["\t" + random_print_char_command()]

    code_lines += [code_block_return_from_act_3]

    #<auto>
    #	Scene __: Even more accusations.
    #
    #Capulet:\n
    # for char in "<spl code of a>"
    #    You are as good as <spl code of char>.
    #    Speak your mind.
    #</auto>
    for scene_number, key in zip(scene_numbers, ordered_keys):
        code_lines += ["\t\tScene " + scene_number + ": Even more accusations."]
        code_lines += [""]
        code_lines += ["Capulet:"]
        for symbol in NUMBERS[key]:
            number = NUMBERS[ord(symbol)]
            code_lines += ["\t" + random_assignment_command(number)]
            code_lines += ["\t" + random_print_char_command()]
        code_lines += ["\t" + random_return_to_scene_command("II")]
        code_lines += [""]

    code_lines += [code_block_act_4_scene_1]

    return "\n".join(code_lines)

