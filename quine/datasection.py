from .handwritten import NUMBERS, DATA_PUSH_COMMAND_BEFORE, DATA_PUSH_COMMAND_AFTER


def generate(code):
    """
    The data section of the quine makes up the majority of th code. It contains
    four lines for each symbol in the code section, which push this symbol on
    the data stack and count this push.
    See comments in handwritten.py for details.

    :return: a string containing the full source code for the data section.
    """
    code_lines = []
    for symbol in code:
        number = NUMBERS[ord(symbol)]
        code_lines.append(DATA_PUSH_COMMAND_BEFORE + number + DATA_PUSH_COMMAND_AFTER)
    return "\n".join(code_lines)
