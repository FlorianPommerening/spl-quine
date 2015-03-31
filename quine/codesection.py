from . import handwritten
import spl.utilities
import spl.randomized
import spl.tokens

from collections import defaultdict
import random
import re

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
    print_prefix_section = generate_print_prefix(prefix)
    print_data_section = generate_print_data()
    print_code_section = generate_print_code()
    final_section = generate_final_section()
    # Compute the set of characters we used so far.
    used_characters = set()
    used_characters |= set(print_prefix_section)
    used_characters |= set(print_data_section)
    used_characters |= set(print_code_section)
    used_characters |= set(final_section)
    utility_section = generate_utility_section(used_characters)
    code_lines = [
        print_prefix_section,
        print_data_section,
        print_code_section,
        utility_section,
        final_section,
    ]
    return "\n".join(code_lines)

def generate_print_prefix(prefix):
    return "\n".join([
        handwritten.CODE_PRINT_PREFIX_START,
        spl.randomized.print_statements(prefix, handwritten.LITERALS,
                                        handwritten.CODE_PRINT_PREFIX_CHARACTERS),
        handwritten.CODE_PRINT_PREFIX_END,
    ])


def generate_print_data():
    return "\n".join([
        handwritten.CODE_PRINT_DATA_SETUP,
        handwritten.CODE_PRINT_DATA_LOOP,
    ])


def generate_print_code():
    return handwritten.CODE_PRINT_CODE_LOOP


def generate_utility_section(used_characters):
    used_characters |= set(handwritten.UTILITY_PRINT_PUSH_COMMAND_START)
    used_characters |= set(handwritten.UTILITY_SWITCH_CASE_START)
    used_characters |= set(handwritten.UTILITY_SWITCH_CASE_END)
    used_characters |= set(handwritten.UTILITY_PRINT_PUSH_COMMAND_END)
    used_characters |= set(handwritten.UTILITY_INITIALIZE_CONSTANTS)
    used_characters |= set(handwritten.UTILITY_PRINT_LITERAL_START)
    used_characters |= set(handwritten.UTILITY_PRINT_LITERAL_END)
    for tokens in (spl.tokens.ASSIGNMENT_COMMANDS,
                   spl.tokens.VALUE_TEST_COMMANDS,
                   spl.tokens.PRINT_CHAR_COMMANDS,
                   spl.tokens.CONDITIONAL_PROCEED_TO_SCENE_COMMANDS,
                   spl.tokens.ADJECTIVES):
        for token in tokens:
            used_characters |= set(token)
    used_characters -= set("%")

    while True:
        additional_characters = set()
        for c in used_characters:
            additional_characters |= set(handwritten.LITERALS[ord(c)])
        if additional_characters - used_characters:
            used_characters |= additional_characters
        else:
            break

    used_literals = [lit for c, lit in sorted(handwritten.LITERALS.items())
                            if chr(c) in used_characters]
    number_scenes = [(literal, spl.utilities.scene_number(i))
                     for i, literal in enumerate(used_literals, start=3)]
    code_lines = [
        handwritten.UTILITY_PRINT_PUSH_COMMAND_START,
        spl.randomized.print_statements(handwritten.DATA_PUSH_COMMAND_BEFORE, handwritten.LITERALS),
        handwritten.UTILITY_SWITCH_CASE_START,
        spl.randomized.switch_statement(number_scenes),
        handwritten.UTILITY_SWITCH_CASE_END,
        spl.randomized.print_statements(handwritten.DATA_PUSH_COMMAND_AFTER, handwritten.LITERALS),
        handwritten.UTILITY_PRINT_PUSH_COMMAND_END,
    ]
    for literal, scene_number in number_scenes:
        code_lines += [
            handwritten.UTILITY_PRINT_LITERAL_START % scene_number,
            spl.randomized.print_statements(literal, handwritten.LITERALS),
            handwritten.UTILITY_PRINT_LITERAL_END
        ]
    code_lines += [
        handwritten.UTILITY_INITIALIZE_CONSTANTS,
    ]
    return "\n".join(code_lines)


def generate_final_section():
    return handwritten.CODE_END_OF_PROGRAM
