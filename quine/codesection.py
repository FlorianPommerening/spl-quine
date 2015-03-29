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
    code_lines = []
    code_lines += generate_print_prefix(prefix)
    code_lines += generate_print_data()
    code_lines += generate_print_code()
    code_lines += generate_utility_section()
    code_lines += generate_final_section()
    code_so_far = "\n".join(code_lines)
    length_of_code = len(code_so_far)
    assign_length_code = spl.randomized.assign_number_command(length_of_code)
    remaining_code = shorten_code(code_so_far, len(assign_length_code))
    code = assign_length_code + remaining_code
    assert(len(code) == length_of_code)
    return code

def generate_print_prefix(prefix):
    return [
        handwritten.CODE_PRINT_PREFIX_START,
        spl.randomized.print_statements(prefix, handwritten.LITERALS, handwritten.CODE_PRINT_PREFIX_ACTORS),
        handwritten.CODE_PRINT_PREFIX_END,
    ]


def generate_print_data():
    return [
        handwritten.CODE_PRINT_DATA_SETUP,
        handwritten.CODE_PRINT_DATA_LOOP,
    ]


def generate_print_code():
    return [
        handwritten.CODE_PRINT_CODE_SETUP,
        handwritten.CODE_PRINT_CODE_LOOP,
    ]


def generate_utility_section():
    number_scenes = [(literal, spl.utilities.scene_number(i))
                     for i, literal in enumerate(sorted(handwritten.LITERALS.values()), start=3)]
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
    return code_lines


def generate_final_section():
    return [
        handwritten.CODE_END_OF_PROGRAM
    ]


def shorten_code(code, reduce_by):
    positive_adjectives_by_length = defaultdict(list)
    for adj in spl.tokens.POSITIVE_ADJECTIVES:
        positive_adjectives_by_length[len(adj)].append(adj)
    useful_lengths = [l for l in positive_adjectives_by_length
                          if l-1 in positive_adjectives_by_length]
    target_length = len(code) - reduce_by
    while len(code) > target_length:
        l = random.choice(useful_lengths)
        replace_from = random.choice(positive_adjectives_by_length[l])
        replace_to = random.choice(positive_adjectives_by_length[l-1])
        code = re.sub(replace_from, replace_to, code, count=1)
    return code