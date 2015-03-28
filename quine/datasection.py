from . import handwritten


def generate(code):
    """
    The data section of the quine makes up the majority of th code. It contains
    four lines for each symbol in the code section, which push this symbol on
    the data stack and count this push.
    See comments in handwritten.py for details.

    :return: a string containing the full source code for the data section.
    """
    code_lines = [generate_push_command(symbol) for symbol in code]
    return "".join(code_lines)


def generate_push_command(symbol):
    return handwritten.DATA_PUSH_COMMAND_BEFORE \
        + handwritten.LITERALS[ord(symbol)] \
        + handwritten.DATA_PUSH_COMMAND_AFTER
