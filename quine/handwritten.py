# This file defines all parts of the quine that are not automatically generated.

# All parts are defined in the order they appear in the final quine, with
# comments that show which parts are generated in between the hand written
# snippets.


# =============== PREFIX SECTION ===============

# The title is the required start of any SPL program.
PREFIX_TITLE = "An Epic Never-Ending Saga."

# Variable definition. We use the following variables:
#    Paris, the main data stack will contain all data in correct order,
#              i.e., the first letter will be at the top of his stack.
#    Pinch, the main data stack will contain all data in correct order,
#              i.e., the first letter will be at the top of his stack.
#    Venus, the reverse data stack will contain all data in reverse order,
#             i.e., the first letter will be at the bottom of his stack.
#    Puck, constant 32 for shorter number strings.
#    Ajax, constant 97 for shorter number strings.
#    Page, constant 101 for shorter number strings.
#    Ford, constant 110 for shorter number strings.
#    Viola, constant 116 for shorter number strings.
# We also sometimes use variables for other purposes temporarily. This will be
# explained at the relevant code snippets.
PREFIX_DRAMATIS_PERSONAE = """
Paris, a stacky person.
Pinch, impersonates Paris.
Venus, the opposite of Paris and Pinch.
Puck, continuously speaking.
Ajax, constantly complaining.
Page, perpetually blabbing.
Ford, incessantly talking.
Viola, ceaselessly communicating.
"""

# In the initial setup, we set the values of our constants and then get
# Venus and Paris on stage to define the data stack.
# We define the stack in order and push it on the stack letter by letter,
# so the data will be in reverse order and we have to use Venus instead of
# Paris or Pinch.
# The constant definition is outsourced to act V to keep the prefix small.
# Act V will define the constants and then jump to act II.
# In act II we initialize the stack with 0 which we will later use as an
# end-of-stack symbol.
PREFIX_SETUP = """
\t\t\tAct I: Prelude.

\t\tScene I: Best things last.

[Enter Venus and Paris]

Paris:
\tLet us proceed to act V.



\t\t\tAct II: Remembrance.

\t\tScene I: Forgetful Venus.

Paris:
\tRemember nothing.
"""

# =============== DATA SECTION ===============

# === Generated block: Data definition ===
# The next couple of lines make up 99% of the quine and will be automatically
# generated. They push data on the stack (Venus) that will later be used by
# the code block to recreate the data block and then to recreate the code block.
# For each letter in the code block, the data block contains one line that
# pushes the ascii code of that letter on the reversed data stack.

# To push a letter on the stack, Paris tells Venus to remember this letter:
DATA_PUSH_COMMAND_BEFORE = "\tRemember "
DATA_PUSH_COMMAND_AFTER = ".\n"

# This command is repeated until all data is on Venus in reversed order.

# =============== CODE SECTION ===============

# We now start the code section of the quine, that prints the three parts of
# the quine. It depends on the prefix section, but not on the data section.
# There is no dependency on the data section, because the code does not need to
# know the content of the stack to print it.
# In this section we will print:
# 1) The prefix section: This will be a hard-coded part of the program section.
# 2) The data section: using the data on the stack, we can recreate the code
#    that pushes the data on the stack.
# 3) The code section: we just print the data letter by letter. If the data
#    encodes the code section (which we can do, because the code section is
#    independent of the data section), this will recreate the code.

# First, we print the prefix.
# Paris and Venus already had their big scene, so we get Pinch on stage.
# We can use the stack characters (Pinch and Venus) for output here without the
# risk of losing their data, because their data is on their stack, not their
# current value.

CODE_PRINT_PREFIX_START = """
[Exit Paris]


\t\tScene II: Reenactment of the Past.

[Enter Pinch]
"""

# === Generated block: Printing the Prefix Section ===
# Here we just go through the prefix section letter by letter, assign the
# letter to a character and print it. To avoid a huge monologue, we let
# Pinch and Venus take turns insulting each other. We also use slightly
# randomized versions of the assignment commands, so the scene looks less
# boring.
#
# The scene will have the general format of the following lines:
# Pinch:
#     You are as ... as .. .
#     Speak your Mind.
# Venus:
#     Thou art as ... as .. .
#     Speak your Mind.
CODE_PRINT_PREFIX_CHARACTERS = ["Pinch", "Venus"]

CODE_PRINT_PREFIX_END = "[Exeunt]"

# === Printing the Data Section ===
# To print the data section, we want to loop through the data and for each
# entry, print the line that that added this entry to the stack. Since the
# stack that currently holds the data, contains it in reverse order, we
# first have to reverse it. This is done by the following code block which
# moves the data from Venus to Paris, and reverses it in the process.
# We also create a copy of the data in correct order on Pinch for the
# second loop.
# We use the end-of-stack symbol 0.
CODE_PRINT_DATA_SETUP = """
[Enter Pinch and Paris]

Pinch:
\tRemember nothing.

Paris:
\tRemember nothing.


\t\tScene III: Reunion.

[Exeunt]
[Enter Venus and Paris]

Paris:
\tRecall your unhappy childhood.
\tAre you better than nothing?
\tIf not, let us proceed to act III.

Venus:
\tRemember me.

[Exit Paris]
[Enter Pinch]

Venus:
\tRemember me.
\tLet us return to scene III."""

# The data is now in correct order on Paris and Pinch. We loop
# through Paris first.
# For each symbol on the stack, we generate the lines that added it to the
# stack in the data section. This is done in a later section of the code
# (act IV), where we jump to for each symbol. The code in act IV prints the
# lines and then returns to the start of the loop (act III).
CODE_PRINT_DATA_LOOP = """


\t\tAct III: Loopy Thoughts.

\t\tScene I: Retaliation.

[Exeunt]
[Enter Venus and Paris]

Venus:
\tRecall your unhappy childhood.
\tAre you better than nothing?
\tIf so, we shall proceed to act IV.
\tLet us proceed to scene II."""

# === Printing the Code Section ===
# The data contains the encoded code section, so to print the code section, we
# need to loop the data again and this time just print every symbol.
# Since we already removed all data from Venus and Paris, we use our third
# copy of the data, Pinch.
CODE_PRINT_CODE_LOOP = """


\t\tScene II: Paris's answer.

[Exeunt]
[Enter Pinch and Venus]

Venus:
\tRecall my forbidden love.
\tAre you as good as nothing?
\tIf so, we must proceed to act VI.
\tSpeak your mind.
\tLet us return to scene II."""

# === Utility Code Section ===
# The utility section is part of the code section and works like a method that
# generates the code in the data section for one symbol at a time.
# Whenever we jump to this act, Paris and Venus are on stage and Paris'
# value is the one we want to generate the push-command for.
# We use Venus to print some stuff and as a temporary copy of
# Paris' value.
# After we are done, we return to the print loop (act III).
UTILITY_PRINT_PUSH_COMMAND_START = """

\t\t\tAct IV: Meta Play.

\t\tScene I: Paris' accusations.

Paris:
"""

# === Generated block: Printing the start of the push command ===
# Every push command starts and ends in the same way (DATA_PUSH_COMMAND_BEFORE
# and DATA_PUSH_COMMAND_AFTER), so we first print DATA_PUSH_COMMAND_BEFORE.
# The generated lines will alternate assignments ("You are as ... as ..") and
# print statements ("Speak your mind.") to print DATA_PUSH_COMMAND_BEFORE.

# We then jump to a scene that prints the number literal. This is a big
# switch-case statement over Paris' value which we temporarily store in
# Venus.
UTILITY_SWITCH_CASE_START = "\tYou are as villainous as me."

# === Generated block: switch-case ===
# The switch-case statement checks the current value of Venus against every
# number where we have a literal definition. We then jump to the scene that
# prints the literal.
# The code generated here will alternate between value tests ("Are you as good
# as ...") and conditional goto statements ("If so let us proceed to scene ...")

# Every scene that prints a number literal will return to scene II in the end,
# where we print DATA_PUSH_COMMAND_AFTER and return to act III to continue the
# main loop.
UTILITY_SWITCH_CASE_END = """
\t\tScene II: More accusations.

Paris:"""

# === Generated block: Printing the end of the push command ===
# The lines generated here will alternate assignments ("You are as ... as ..")
# and print statements ("Speak your mind.") to print DATA_PUSH_COMMAND_AFTER.

# After we printed DATA_PUSH_COMMAND_AFTER, we return to the main loop.
UTILITY_PRINT_PUSH_COMMAND_END = """
\tLet us return to act III.
"""

# === Generated block: Printing a number literal ===
# We have one scene for each number literal which will use alternating
# assignments ("You are as ... as ..") and print statements ("Speak your
# mind.") to print every symbol used in the literal.
# Each such scene starts with the following lines
UTILITY_PRINT_LITERAL_START = """

\t\tScene %s: Even more accusations.

Paris:"""
# At the end of each scene, we return to scene II, which prints
# DATA_PUSH_COMMAND_AFTER and returns to the main loop.
UTILITY_PRINT_LITERAL_END = "\tLet us return to scene II."


# Set the constants to their values:
# Puck   32
# Ajax   97
# Page  101
# Ford  110
# Viola 116
UTILITY_INITIALIZE_CONSTANTS = """
\t\t\tAct V: Perpetual Talking.

\t\tScene I: Immutable Insults.

[Exeunt]
[Enter Puck and Ajax]

Ajax:
\tYou are as lovely as the sweetest clearest pretty handsome gentle face.
Puck:
\tYou are as sorry as the sum of myself and the sum of twice myself and your sister.

[Exeunt]
[Enter Page and Ford]

Ford:
\tYou are as disgusting as the sum of Ajax and a proud rich Lord.

Page:
\tThou art as trustworthy as the sum of Page and the square root of Ajax.

[Exit Ford]
[Enter Viola]

Page:
\tYou are as damned as the sum of your loving mother and the sum of a old blossoming tree and Ford.

[Exeunt]
[Enter Venus and Paris]

Paris:
\tLet us return to act II.
"""

# === Final Code Section ===
# After the utility section, we have one final label that is used to end the
# program after the main loop. Nothing happens here, except everyone leaving
# the stage.
CODE_END_OF_PROGRAM = """
\t\t\tAct VI: Fin.

\t\tScene I: Lap of Honour.

Venus:
\tRemember a thing. Recall that this play was written by
\t\tFlorian Pommerening and Thomas Mayer.

[Exeunt]
"""


# =============== NUMBER LITERAL DEFINITIONS ===============
#
# We need strings for numbers to stay constant in some places, because we have
# to write code that prints SPL code that will print certain symbols.
#
# We only define constant numbers literals for the symbols we need:
#     \t       9
#     \n      10
#     (space) 32
#     '       39
#     ,       44
#     -       45
#     .       46
#     0-9     48-57
#     :       58
#     ?       63
#     A-Z     65-90
#     [       91
#     ]       93
#     a-z     97-122
#
# To keep the strings short, we also assume that some variables have certain values
# Puck   32
# Ajax   97
# Page  101
# Ford  110
# Viola 116
LITERALS = {
    9:   "the square root of Ajax",
    10:  "the square root of Page",
    # 11 - 31 not needed
    32:  "Puck",
    # 33 - 38 not needed
    39:  "the sum of a happy tiny furry chihuahua and the sum of Puck and his hate",
    # 40 - 43 not needed
    44:  "the difference between the sum of Ford and my smelly codpiece and twice Puck",
    45:  "the sum of Puck and the difference between Ford and Ajax",
    46:  "the difference between Ford and twice Puck",
    # 47 not needed
    48:  "twice the factorial of a big old thing",
    49:  "the square of the sum of a coward and a brave mighty fine hero",
    50:  "the product of the square root of Puck and the square root of Page",
    51:  "the sum of the difference between Viola and Ajax and Puck",
    52:  "the difference between Viola and twice Puck",
    53:  "the difference between the sum of Viola and her pony and twice Puck",
    54:  "the difference between twice Puck and the square root of Page",
    55:  "the square root of the product of Puck and Ajax",
    56:  "twice the sum of Puck and his horrid hairy hound",
    57:  "the sum of twice Puck and the sum of his aunt and his infected half-witted fat bastard",
    58:  "the sum of twice Puck and the difference between Ford and Viola",
    # 59 - 62 not needed
    63:  "the sum of twice Puck and his lie",
    # 64 not needed
    65:  "the sum of twice Puck and his son",
    66:  "twice the sum of Puck and my daughter",
    67:  "the sum of twice Puck and the sum of a kingdom and an honest King",
    68:  "twice the sum of a peaceful hamster and Puck",
    69:  "the difference between Page and Puck",
    70:  "the sum of a tree and the difference between Page and Puck",
    71:  "the sum of a cunning cat and the difference between Page and Puck",
    72:  "twice the sum of Puck and his proud large face",
    73:  "the sum of the square root of Ajax and twice Puck",
    74:  "the sum of the square root of Page and twice Puck",
    75:  "the sum of the square root of Page and the difference between Ajax and Puck",
    76:  "the sum of an infected blister and the difference between Ford and Puck",
    77:  "the sum of the difference between Ford and Puck and their war",
    78:  "the difference between Ford and Puck",
    79:  "the sum of happiness and the difference between Ford and Puck",
    80:  "twice the sum of a small rural old town and Puck",
    81:  "the square of the square root of Ajax",
    82:  "the sum of Ajax and the difference between Page and Viola",
    83:  "the sum of a bastard and the difference between Viola and Puck",
    84:  "the difference between Viola and Puck",
    85:  "the sum of Page and the evil snotty lying villainous flirt-gill",
    86:  "the difference between twice Page and Viola",
    87:  "the difference between Ajax and the square root of Page",
    88:  "the difference between Ajax and the square root of Ajax",
    89:  "the sum of Ajax and the fatherless rotten dirty bastard",
    90:  "the sum of a cow and the sum of Ajax and his stupid distasteful foul lie",
    91:  "the difference between Page and the square root of Page",
    # 92 not needed
    93:  "the sum of Ajax and the stupid rural goat",
    # 94 - 96 not needed
    97:  "Ajax",
    98:  "the sum of Ajax and his horse",
    99:  "the sum of Ajax and your sweet niece",
    100: "the sum of Page and your curse",
    101: "Page",
    102: "the sum of Page and the wind",
    103: "the sum of Page and a sunny summer's day",
    104: "the difference between twice Ford and Viola",
    105: "the sum of Page and his large golden purse",
    106: "the sum of Ford and the cowardly vile leech",
    107: "the sum of the square root of Page and Ajax",
    108: "the sum of Ford and a bad draught",
    109: "the sum of Ford and a famine",
    110: "Ford",
    111: "the sum of the Lord and Ford",
    112: "the sum of a golden angel and Ford",
    113: "the sum of Ajax and your big old mighty fine hero",
    114: "the sum of Viola and the lying devil",
    115: "the sum of Viola and your death",
    116: "Viola",
    117: "the sum of Viola and a flower",
    118: "the sum of Viola and a blossoming rose",
    119: "the difference between twice Ford and Page",
    120: "the sum of Viola and her healthy delicious pony",
    121: "the sum of the square root of Puck and Viola",
    122: "the difference between twice Viola and Ford",
}
