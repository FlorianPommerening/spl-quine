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
#    Ajax, constant 3 for shorter number strings.
#    Page, constant 8 for shorter number strings.
#    Ford, constant 32 for shorter number strings.
#    Viola, constant 64 for shorter number strings.
#    Puck, constant 113 for shorter number strings.
# We also sometimes use variables for other purposes temporarily. This will be
# explained at the relevant code snippets.
PREFIX_DRAMATIS_PERSONAE = """
Paris, a stacky person.
Pinch, impersonates Paris.
Venus, the opposite of Paris and Pinch.
Ajax, a triple split personality.
Page, a proud rich noble Lord.
Ford, helps out with nothing.
Viola, is twice as brave as Ford.
Puck, a random bystander.
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


UTILITY_INITIALIZE_CONSTANTS = """
\t\t\tAct V: Perpetual Talking.

\t\tScene I: Immutable Insults.

[Exeunt]
[Enter Puck and Viola]

Puck:
\tYou are as brave as the square of a honest handsome healthy hero.
Viola:
\tYou are as lovely as the sum of myself and the square of the difference
\tbetween the sweetest clearest pretty face and a rose.

[Exeunt]
[Enter Page and Ajax]

Ajax:
\tYou are a proud rich noble Lord.

Page:
\tThou art as trustworthy as the sum of a cunning roman and a cat.

[Exit Ajax]
[Enter Ford]

Page:
\tYou are as damned as the product of your charming loving mother and a big old blossoming tree.

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
# Ajax    3
# Page    8
# Ford   32
# Viola  64
# Puck  113
LITERALS = {
    9:   "the square of Ajax",
    10:  "the sum of a rural cow and Page",
    # 11 - 31 not needed
    32:  "Ford",
    # 33 - 38 not needed
    39:  "the sum of Ford and the sum of Page and his hate",
    # 40 - 43 not needed
    44:  "the difference between Viola and the sum of a healthy happy cute tiny pony and a beautiful red rose",
    45:  "the difference between Viola and the sum of a amazing golden lovely blossoming summer's day "
         "and Ajax",
    46:  "the sum of Viola and the sum of the cursed half-witted damned distasteful flirt-gill "
         "and the snotty leech",
    # 47 not needed
    48:  "twice the product of Ajax and Page",
    49:  "the square of the difference between a famine and a fat-kidneyed sorry miserable starvation",
    50:  "the sum of a hamster and the square of the difference between a hound and a dirty disgusting hairy wolf",
    51:  "the sum of a peaceful chihuahua and the square of the difference between Page and the wind",
    52:  "the difference between Viola and the sum of Page and a amazing sunny summer's day",
    53:  "the sum of the cube of Ajax and the difference between the cube of Ajax and a hero",
    54:  "the difference between Viola and the sum of Page and a handsome hero",
    55:  "the difference between Viola and the sum of Page and a cat",
    56:  "the difference between Viola and Page",
    57:  "the sum of the difference between Viola and Page and a hair",
    58:  "the sum of the difference between Viola and Page and a rural pony",
    # 59 - 62 not needed
    63:  "the sum of Viola and the devil",
    # 64 not needed
    65:  "the sum of Viola and a road",
    66:  "the sum of the clearest sky and Viola",
    67:  "the sum of the sum of a furry grandmother and a grandfather and Viola",
    68:  "the sum of Viola and a normal old road",
    69:  "the sum of a squirrel and the sum of Viola and a furry old pony",
    70:  "the sum of Viola and the sum of a bottomless large nose and a healthy tree",
    71:  "the sum of Viola and the difference between Page and a roman",
    72:  "the difference between Page and a foul fatherless infected dirty oozing rotten leech",
    73:  "the sum of the sum of Page and a cat and Viola",
    74:  "the sum of Page and the sum of a lovely sky and Viola",
    75:  "the sum of Page and the sum of Viola and Ajax",
    76:  "the sum of Viola and the difference between a normal black good smooth road "
         "and the reddest green rose",
    77:  "the sum of Viola and the difference between a brave charming handsome cute hero and Ajax",
    78:  "the sum of the difference between a mighty noble rich brave chihuahua and a healthy squirrel "
         "and Viola",
    79:  "the sum of Viola and the sum of a fair amazing beautiful fine angel and a hog",
    80:  "the difference between Viola and a dirty fat-kidneyed misused smelly flirt-gill",
    81:  "the difference between Puck and Ford",
    82:  "the sum of Viola and the sum of a big mighty old gentle squirrel and a healthy door",
    83:  "the sum of a beautiful large blossoming green mistletoe and the sum of Viola and Ajax",
    84:  "the sum of Viola and the sum of the mighty fine hero and the huge pretty amazing sweet happiness",
    85:  "the difference between Puck and the sum of the cube of Ajax and a flower",
    86:  "the difference between Puck and the cube of Ajax",
    87:  "the sum of an angel and the difference between Puck and the cube of Ajax",
    88:  "the sum of Viola and the difference between a big loving rich trustworthy aunt "
         "and a evil smelly villainous hound",
    89:  "the sum of Ajax and the difference between Puck and the cube of Ajax",
    90:  "the sum of the difference between Puck and the cube of Ajax and a golden furry hair",
    91:  "the sum of Viola and the cube of Ajax",
    # 92 not needed
    93:  "the sum of Viola and the difference between Ford and Ajax",
    # 94 - 96 not needed
    97:  "the difference between Puck and twice Page",
    98:  "the sum of Ford and the sum of Viola and the bluest sky",
    99:  "the sum of Viola and the sum of Ford and Ajax",
    100: "the square of the sum of Page and his brave hero",
    101: "the sum of Puck and the sum of a horrible stinking smelly codpiece and a hairy dusty hog",
    102: "the sum of the cursed foul infected blister and the difference between Puck and Ajax",
    103: "the difference between Puck and the sum of a delicious healthy sweet horse and a normal cat",
    104: "the sum of the sum of a beggar and Puck and a half-witted disgusting sorry coward",
    105: "the difference between Puck and Page",
    106: "the sum of a snotty oozing fat-kidneyed flirt-gill and the sum of a plum and Puck",
    107: "the difference between Puck and the sum of a tiny old proud chihuahua and a cowardly goat",
    108: "the sum of Puck and the difference between Ajax and Page",
    109: "the sum of Puck and an infected stinking bastard",
    110: "the difference between Puck and Ajax",
    111: "the difference between Puck and a furry animal",
    112: "the sum of Puck and a plague",
    113: "Puck",
    114: "the sum of Puck and the Lord",
    115: "the difference between Puck and a fat pig",
    116: "the sum of Puck and Ajax",
    117: "the sum of Puck and a little gentle chihuahua",
    118: "the difference between Puck and the sum of a fatherless vile devil and the Hell",
    119: "the sum of Puck and the sum of the clearest sweetest summer's day and the reddest rose",
    120: "the sum of a black bottomless face and the sum of Puck and Ajax",
    121: "the sum of Puck and Page",
    122: "the difference between twice Viola and the sum of a tiny old town and a large tree",
}
