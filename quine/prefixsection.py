from . import handwritten


def generate():
    """
    The prefix section of the quine includes everything from the start of the
    program until the first line that adds data. The prefix section does not
    depend on the data section or the code section.

    The code generated here starts the program, defines the necessary variables
    and initializes constants. It then sets the scene for the data definition
    to begin. See comments in handwritten.py for details.

    :return: a string containing the full source code for the prefix.
    """
    code_lines = [
        handwritten.PREFIX_TITLE,
        handwritten.PREFIX_DRAMATIS_PERSONAE,
        handwritten.PREFIX_SETUP
    ]
    return "\n".join(code_lines)
























