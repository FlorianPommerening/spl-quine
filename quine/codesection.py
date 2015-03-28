import itertools
from . import handwritten
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
    # Print prefix section
    code_lines = [
        handwritten.CODE_PRINT_PREFIX_START,
        generate_print_statements(prefix, handwritten.CODE_PRINT_PREFIX_ACTORS),
        handwritten.CODE_PRINT_PREFIX_END,
    ]

    # Print data section
    code_lines += [
        handwritten.CODE_PRINT_DATA_SETUP,
        handwritten.CODE_PRINT_DATA_LOOP,
    ]

    # Print code section
    code_lines += [
        handwritten.CODE_PRINT_CODE_SETUP,
        handwritten.CODE_PRINT_CODE_LOOP,
    ]

    # Utility section
    number_scenes = [(spl.utilities.scene_number(i), literal)
                     for i, literal in enumerate(sorted(handwritten.LITERALS.values()), start=3)]

    code_lines += [
        handwritten.UTILITY_PRINT_PUSH_COMMAND_START,
        generate_print_statements(handwritten.DATA_PUSH_COMMAND_BEFORE),
        handwritten.UTILITY_SWITCH_CASE_START,
        generate_switch_statement(number_scenes),
        handwritten.UTILITY_SWITCH_CASE_END,
        generate_print_statements(handwritten.DATA_PUSH_COMMAND_AFTER),
        handwritten.UTILITY_PRINT_PUSH_COMMAND_END,
    ]

    for scene_number, literal in number_scenes:
        code_lines += [
            handwritten.UTILITY_PRINT_LITERAL_START % scene_number,
            generate_print_statements(literal),
            handwritten.UTILITY_PRINT_LITERAL_END
        ]

    # Final section
    code_lines += [
        handwritten.CODE_END_OF_PROGRAM
    ]

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
        number = handwritten.LITERALS[ord(symbol)]
        code_lines += ["\t" + random_assignment_command(number)]
        code_lines += ["\t" + random_print_char_command()]
    return "\n".join(code_lines)


def generate_switch_statement(number_scenes):
    """
    Generate randomized SPL code for a switch statement that jumps to a different scene
    for each literal.
    :param number_scenes: list of tuples (s, l) where s is the label of the scene for literal l.
    :return: a string containing code statements to jump to the correct scene.
    """
    code_lines = []
    for scene_number, literal in number_scenes:
        code_lines.append("\t" + random_value_test_command(literal))
        code_lines.append("\t" + random_conditional_proceed_to_scene_command(scene_number))
    return "\n".join(code_lines)
