import itertools
from .handwritten import CODE_PRINT_PREFIX_START, CODE_PRINT_PREFIX_ACTORS, NUMBERS, CODE_PRINT_DATA_SETUP, \
    UTILITY_SWITCH_CASE_END, CODE_END_OF_PROGRAM, UTILITY_PRINT_PUSH_COMMAND_END, \
    DATA_PUSH_COMMAND_BEFORE, DATA_PUSH_COMMAND_AFTER, CODE_PRINT_PREFIX_END, CODE_PRINT_DATA_LOOP, \
    CODE_PRINT_CODE_SETUP, CODE_PRINT_CODE_LOOP, UTILITY_PRINT_PUSH_COMMAND_START, UTILITY_SWITCH_CASE_START, \
    UTILITY_PRINT_CHARACTER_ACTORS, UTILITY_PRINT_CHARACTER_START, UTILITY_PRINT_CHARACTER_END
import spl.utilities
from spl.generated import random_assignment_command, random_print_char_command, random_value_test_command, \
    random_conditional_proceed_to_scene_command


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
    code_lines = []

    # Hard-code printing commands for the prefix
    code_lines.append(CODE_PRINT_PREFIX_START)
    code_lines.append(generate_print_statements(prefix, CODE_PRINT_PREFIX_ACTORS))
    code_lines.append(CODE_PRINT_PREFIX_END)

    code_lines.append(CODE_PRINT_DATA_SETUP)
    code_lines.append(CODE_PRINT_DATA_LOOP)

    code_lines.append(CODE_PRINT_CODE_SETUP)
    code_lines.append(CODE_PRINT_CODE_LOOP)

    code_lines.append(UTILITY_PRINT_PUSH_COMMAND_START)

    # <auto>
    #Juliet:
    #	Remember
    #</auto>
    code_lines.append(generate_print_statements(DATA_PUSH_COMMAND_BEFORE))
    code_lines.append(UTILITY_SWITCH_CASE_START)

    #<auto>
    #	Are you as good as <spl code of a>
    #	If so let us proceed to scene <scene of a>
    #	...
    #</auto>

    ordered_keys = sorted(NUMBERS.keys())
    scene_numbers = []

    for i in range(len(ordered_keys)):
        scene_numbers.append(spl.utilities.scene_number(i + 3))

    for scene_number, key in zip(scene_numbers, ordered_keys):
        code_lines.append("\t" + random_value_test_command(NUMBERS[key]))
        code_lines.append("\t" + random_conditional_proceed_to_scene_command(scene_number))

    code_lines.append(UTILITY_SWITCH_CASE_END)

    #<auto>
    #.\n
    #Capulet:
    #	You are as worried as the sum of yourself and the son.
    #</auto>
    code_lines.append(generate_print_statements(DATA_PUSH_COMMAND_AFTER))

    code_lines.append(UTILITY_PRINT_PUSH_COMMAND_END)

    #<auto>
    #	Scene __: Even more accusations.
    #
    #Capulet:\n
    # for char in "<spl code of a>"
    #    You are as good as <spl code of char>.
    #    Speak your mind.
    #</auto>
    for scene_number, key in zip(scene_numbers, ordered_keys):
        code_lines.append(UTILITY_PRINT_CHARACTER_START % scene_number)
        code_lines.append(generate_print_statements(NUMBERS[key], UTILITY_PRINT_CHARACTER_ACTORS))
        code_lines.append(UTILITY_PRINT_CHARACTER_END)

    code_lines.append(CODE_END_OF_PROGRAM)

    return "\n".join(code_lines)


def generate_print_statements(text, actors=None):
    """
    Generate randomized SPL code to print the given text letter by letter.
    :param text: the text to print
    :param actors: the actors that should say the print line. If None, we
                   assume the actor is already talking and add no line to
                   indicate the actor. Otherwise, the list must contain either
                   one actor whose line is added before all the print
                   statements, or two actors who will take turns printing the
                   text.
    :return: a string containing code statements to print the text.
    """
    code_lines = []
    if actors is None:
        actors = [None]
    elif len(actors) == 1:
        code_lines = [actors[0] + ":"]
    else:
        assert len(actors) == 2

    for actor, symbol in zip(itertools.cycle(actors), text):
        if len(actors) > 1:
            code_lines += [actor + ":"]
        number = NUMBERS[ord(symbol)]
        code_lines += ["\t" + random_assignment_command(number)]
        code_lines += ["\t" + random_print_char_command()]
    return "\n".join(code_lines)