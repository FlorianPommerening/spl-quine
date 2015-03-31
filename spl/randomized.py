import itertools
import random
import math

from . import tokens

# TODO: Fixed seed for testing
random.seed(0)


def assign_value_command(value):
    command = random.choice(tokens.ASSIGNMENT_COMMANDS)
    adjective = random.choice(tokens.ADJECTIVES)
    return command % (adjective, value)


def print_char_command():
    return random.choice(tokens.PRINT_CHAR_COMMANDS)


def value_test_command(value):
    command = random.choice(tokens.VALUE_TEST_COMMANDS)
    adjective = random.choice(tokens.ADJECTIVES)
    return command % (adjective, value)


def conditional_proceed_to_scene_command(scene):
    command = random.choice(tokens.CONDITIONAL_PROCEED_TO_SCENE_COMMANDS)
    return command % scene


def switch_statement(number_scenes):
    """
    Generate randomized SPL code for a switch statement that jumps to a different scene
    for each value.
    :param number_scenes: list of tuples (v, s) where v is a string representing
                          a value and s is the label of the scene for v.
    :return: a string containing code statements to jump to the correct scene.
    """
    code_lines = []
    for value, scene_number in number_scenes:
        code_lines.append("\t" + value_test_command(value))
        code_lines.append("\t" + conditional_proceed_to_scene_command(scene_number))
    return "\n".join(code_lines)


def print_statements(text, literals, actors=None):
    """
    Generate randomized SPL code to print the given text letter by letter.
    :param text: the text to print
    :param literals: dictionary mapping ascii codes to shakespeare literals.
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
        number = literals[ord(symbol)]
        code_lines += ["\t" + assign_value_command(number)]
        code_lines += ["\t" + print_char_command()]
    return "\n".join(code_lines)
