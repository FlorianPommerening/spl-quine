import random

from . import tokens


def random_assignment_command(value):
    command = random.choice(tokens.ASSIGNMENT_COMMANDS)
    adjective = random.choice(tokens.ADJECTIVES)
    return command % (adjective, value)


def random_print_char_command():
    return random.choice(tokens.PRINT_CHAR_COMMANDS)


def random_value_test_command(value):
    command = random.choice(tokens.VALUE_TEST_COMMANDS)
    adjective = random.choice(tokens.ADJECTIVES)
    return command % (adjective, value)


def random_conditional_proceed_to_scene_command(scene):
    command = random.choice(tokens.CONDITIONAL_PROCEED_TO_SCENE_COMMANDS)
    return command % scene