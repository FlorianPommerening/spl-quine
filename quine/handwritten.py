# This file defines all parts of the quine that are not automatically generated.

# All parts are defined in the order they appear in the final quine, with
# comments that show which parts are generated in between the hand written
# snippets.


# =============== PREFIX SECTION ===============

# The title is the required start of any SPL program.
PREFIX_TITLE = "An Epic Never-Ending Saga."

# Variable definition. We use the following variables:
#    Montague, the main data stack will contain all data in correct order,
#              i.e., the first character will be at the top of his stack.
#    Romeo, counts the current number of entries on Montague.
#    Capulet, the reverse data stack will contain all data in reverse order,
#             i.e., the first character will be at the bottom of his stack.
#    Juliet, counts the current number of entries on Capulet.
#    The Apothecary, constant 3 for shorter number strings.
#    Friar John, constant 113 for shorter number strings.
#    Friar Laurence, constant 64 for shorter number strings.
#    Paris, constant 8 for shorter number strings.
#    Tybalt, constant 32 for shorter number strings.
# We also sometimes use variables for other purposes temporarily. This will be
# explained at the relevant code snippets.
PREFIX_DRAMATIS_PERSONAE = """
Montague, a stacky person.
Romeo, his son he can always count on.
Capulet, the plain opposite of Montague.
Juliet, his daughter, always remembering where he put his stuff.
The Apothecary, a triple split personality.
Friar John, just a number in His herd.
Friar Laurence, wields the power the loving mighty noble Lord.
Paris, a proud rich noble Lord.
Tybalt, helps out with nothing.
"""

# In the initial setup, we set the values of our constants and then get
# Capulet and Juliet on stage to define the data stack.
# We define the stack in order and push it on the stack letter by letter,
# so the data will be in reverse order and we have to use Capulet instead of
# Montague.
# TODO: moving the constant definition into the code section and jumping there from here might save some lines.
PREFIX_SETUP = """
\t\t\tAct I: Prelude.

\t\tScene I: Best things last.

[Enter Capulet and Juliet]

Juliet:
\tLet us proceed to act V.



\t\t\tAct II: Remembrance.

\t\tScene I: Forgetful Capulet.

Juliet:
"""

# =============== DATA SECTION ===============

# === Generated block: Data definition ===
# The next couple of million lines will be automatically generated. They push
# data on the stack (Capulet) that will later be used by the code block to
# recreate the data block and then to recreate the code block.
# For each letter in the code block, the data block contains one line that
# pushes the ascii code of that letter on the reversed data stack.
# We do not count the elements on the stack. Instead, we write the total number
# of elements to Juliet in the code.

# To push a letter on the stack, Juliet tells Capulet to remember this letter:
DATA_PUSH_COMMAND_BEFORE = "\tRemember "
DATA_PUSH_COMMAND_AFTER = ".\n"

# This command is repeated until all data is on Capulet in reversed order.

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

# We start by setting Juliet to the number of items on the stack.
# This is part of the code, but need to know the size of the code.
# See codesection.py for details.

CODE_WRITE_CODE_SIZE = """
Capulet:
\tYou are nothing.
"""

# Next, we print the prefix.
# Juliet and Capulet already had their big scene, so we get Montague on stage.
# We can use both of the stack characters (Montague and Capulet) for output
# here without risk of losing their data, because their data is on their stack,
# not their current value.

CODE_PRINT_PREFIX_START = """
[Exit Juliet]


\t\tScene II: Reenactment of the Past.

[Enter Montague]
"""

# === Generated block: Printing the Prefix Section ===
# Here we just go through the prefix section letter by letter, assign the
# letter to a character and print it. To avoid a huge monologue, we let
# Montague and Capulet take turns insulting each other. we also use slightly
# randomized versions of the assignment commands, so the scene looks less
# boring.
#
# The scene will have the general format of the following lines:
# Montague:
#     You are as ... as .. .
#     Speak your Mind.
# Capulet:
#     Thou art as ... as .. .
#     Speak your Mind.
CODE_PRINT_PREFIX_ACTORS = ["Montague", "Capulet"]

CODE_PRINT_PREFIX_END = "[Exeunt]"

# === Printing the Data Section ===
# To print the data section, we want to loop through the data and for each
# entry, print the line that that added this entry to the stack. Since the
# stack that currently holds the data is, contains it in reverse order, we
# first have to reverse it. This is done by the following code block which
# moves the data from Capulet to Montague, and reverses it in the process.
# Capulet is also used as a temporary copy of Juliet's value to avoid calling
# her on stage for the test that ends the loop.
# Romeo counts the elements on Montague, but instead of adding one for each new
# element, we copy the total count before reversing the stack.
CODE_PRINT_DATA_SETUP = """[Enter Romeo and Juliet]

Juliet:
\tYou are as loving as me.


\t\tScene III: Reunion.

[Exeunt]
[Enter Capulet and Montague]

Montague:
\tYou are as dirty as Juliet.
\tAre you better than nothing?
\tIf not, let us proceed to scene IV.
\tRecall your unhappy childhood.

Capulet:
\tRemember me.

[Exit Capulet]
[Enter Juliet]

Montague:
\tYou are as smelly as the sum of yourself and a flirt-gill.
\tWe must return to scene III."""

# The data is now in correct order on Montague. We loop through it (just like
# the last code block did) and move it back on Capulet. We need to do this,
# because we will later need a second copy of the data.
# For each symbol on the stack, we generate the lines that added it to the
# stack in the data section. This is done in a later section of the code
# (act IV), where we jump to for each symbol. The code in act IV prints the
# lines and then returns to the start of the loop (act III).
# Again, the data is moved to Capulet and is reversed in the process, and
# again, Juliet counts elements on Capulet but is copied before the loop rather
# than incremented in the loop.
CODE_PRINT_DATA_LOOP = """
\t\tScene IV: Romeo's answer.

[Exeunt]
[Enter Romeo and Juliet]

Romeo:
\tYou are as loving as me.



\t\tAct III: Output.

\t\tScene I: Retaliation.

[Exeunt]
[Enter Capulet and Montague]

Capulet:
\tYou are as dirty as Romeo.
\tAre you better than nothing?
\tIf not, let us proceed to scene II.
\tRecall your unhappy childhood.

Montague:
\tRemember me.

[Exit Montague]
[Enter Romeo]

Capulet:
\tYou are as smelly as the sum of yourself and a wolf.
\tWe shall proceed to act IV."""

# === Printing the Code Section ===
# The data contains the encoded code section, so to print the code section, we
# need to loop the data again and this time just print every symbol.
# As before, we have the data on Capulet in reversed order, so we have to
# reverse it before we can print it.
CODE_PRINT_CODE_SETUP = """
\t\tScene II: Juliet's answer.

[Exeunt]
[Enter Romeo and Juliet]

Juliet:
\tYou are as loving as me.


\t\tScene III: Re-Retaliation.

[Exeunt]
[Enter Capulet and Montague]

Montague:
\tYou are as dirty as Juliet.
\tAre you better than nothing?
\tIf not, let us proceed to scene IV.
\tRecall your unhappy childhood.

Capulet:
\tRemember me.

[Exit Capulet]
[Enter Juliet]

Montague:
\tYou are as smelly as the sum of yourself and a flirt-gill.
\tWe must return to scene III."""

# Now the data is ordered correctly, and we can loop through it to print it.
# This time, we don't need the data after the loop, so we do not copy it again.
CODE_PRINT_CODE_LOOP = """
\t\tScene IV: Montague loses it.

[Exeunt]
[Enter Montague and Romeo]

Montague:
\tAre you as good as nothing?
\tIf so, we must proceed to act VI.

Romeo:
\tRecall my forbidden love.
\tSpeak your mind.

Montague:
\tYou are as rotten as the sum of yourself and the plague.
\tWe must return to scene IV."""

# === Utility Code Section ===
# The utility section is part of the code section and works like a method that
# generates the code in the data section for one symbol at a time.
# Whenever we jump to this act, Romeo and Capulet are on stage and Montague's
# value is the one we want to generate the push-command for.
# We use Romeo to print some stuff and as a temporary copy of Montague, so
# first we store his current value on his stack. We will restore it just before
# returning to the print loop (act III).
UTILITY_PRINT_PUSH_COMMAND_START = """

\t\t\tAct IV: Meta Play.

\t\tScene I: Capulet's accusations.

Capulet:
\tRemember yourself."""

# === Generated block: Printing the start of the push command ===
# Every push command starts and ends in the same way (DATA_PUSH_COMMAND_BEFORE
# and DATA_PUSH_COMMAND_AFTER), so we first print DATA_PUSH_COMMAND_BEFORE.
# The generated lines will alternate assignments ("You are as ... as ..") and
# print statements ("Speak your mind.") to print DATA_PUSH_COMMAND_BEFORE.

# We then jump to a scene that prints the number literal. This is a big
# switch-case statement over Montague's value which we temporarily store in
# Romeo.
UTILITY_SWITCH_CASE_START = "\tYou are as villainous as Montague."

# === Generated block: switch-case ===
# The switch-case statement checks the current value of Romeo against every
# number where we have a literal definition. We then jump to the scene that
# prints the literal.
# The code generated here will alternate between value tests ("Are you as good
# as ...") and conditional goto statements ("If so let us proceed to scene ...")

# Every scene that prints a number literal will return to scene II in the end,
# where we print DATA_PUSH_COMMAND_AFTER and return to act III to continue the
# main loop.
UTILITY_SWITCH_CASE_END = """
\t\tScene II: More accusations.

Capulet:"""

# === Generated block: Printing the end of the push command ===
# The lines generated here will alternate assignments ("You are as ... as ..")
# and print statements ("Speak your mind.") to print DATA_PUSH_COMMAND_AFTER.

# After we printed DATA_PUSH_COMMAND_AFTER, we return to the main loop. Before
# that, we have to restore Romeo's original value from his stack.
UTILITY_PRINT_PUSH_COMMAND_END = """
\tRecall everything I told you.
\tWe shall return to act III.
"""

# === Generated block: Printing a number literal ===
# We have one scene for each number literal which will use alternating
# assignments ("You are as ... as ..") and print statements ("Speak your
# mind.") to print every symbol used in the literal.
# Each such scene starts with the following lines
UTILITY_PRINT_LITERAL_START = """

\t\tScene %s: Even more accusations.

Capulet:"""
# At the end of each scene, we return to scene II, which prints
# DATA_PUSH_COMMAND_AFTER and returns to the main loop.
UTILITY_PRINT_LITERAL_END = "\tLet us return to scene II."


UTILITY_INITIALIZE_CONSTANTS = """
\t\t\tAct V: Constant Talking.

\t\tScene I: Unchanging Insults.

[Exeunt]
[Enter Friar John and Friar Laurence]

Friar John:
\tYou are as brave as the square of a honest handsome healthy hero.
Friar Laurence:
\tYou are as lovely as the sum of myself and the square of the difference
\tbetween the sweetest clearest pretty face and a rose.

[Exeunt]
[Enter Paris and the Apothecary]

The Apothecary:
\tYou are a proud rich noble Lord.

Paris:
\tThou art as trustworthy as the sum of a cunning roman and a cat.

[Exit the Apothecary]
[Enter Tybalt]

Paris:
\tYou are the product of your charming loving mother and a big old blossoming tree.

[Exeunt]
[Enter Capulet and Juliet]

Juliet:
\tWe shall return to act II.
"""

# === Final Code Section ===
# After the utility section, we have one final label that is used to end the
# program after the main loop. Nothing happens here, except everyone leaving
# the stage.
CODE_END_OF_PROGRAM = """
\t\t\tAct VI: Fin.

\t\tScene I: No questions left.

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
# Friar Laurence  64
# Friar John     113
# The Apothecary   3
# Paris            8
# Tybalt          32

LITERALS = {
    9:   "the square of the Apothecary",
    10:  "the sum of a rural cow and Paris",
    # 11 - 31 not needed
    32:  "Tybalt",
    # 33 - 38 not needed
    39:  "the sum of the Apothecary and the sum of the peaceful sunny moon and Tybalt",
    # 40 - 43 not needed
    44:  "the difference between Friar Laurence and the sum of a healthy happy cute tiny pony and a beautiful red rose",
    45:  "the difference between Friar Laurence and the sum of a amazing golden lovely blossoming summer's day "
         "and the Apothecary",
    46:  "the sum of Friar Laurence and the sum of the cursed half-witted damned distasteful flirt-gill "
         "and the snotty leech",
    # 47 not needed
    48:  "the sum of Friar Laurence and a foul rotten smelly villainous toad",
    49:  "the square of the difference between a famine and a fat-kidneyed sorry miserable starvation",
    50:  "the sum of a hamster and the square of the difference between a hound and a dirty disgusting hairy wolf",
    51:  "the sum of a peaceful chihuahua and the square of the difference between Paris and the wind",
    52:  "the difference between Friar Laurence and the sum of Paris and a amazing sunny summer's day",
    53:  "the sum of the cube of the Apothecary and the difference between the cube of the Apothecary and a hero",
    54:  "the difference between Friar Laurence and the sum of Paris and a handsome hero",
    55:  "the difference between Friar Laurence and the sum of Paris and a cat",
    56:  "the sum of Friar Laurence and a foul rotten oozing beggar",
    57:  "the sum of the difference between Friar Laurence and Paris and a hair",
    58:  "the sum of the difference between Friar Laurence and Paris and a rural pony",
    # 59 - 62 not needed
    63:  "the sum of Friar Laurence and the devil",
    # 64 not needed
    65:  "the sum of Friar Laurence and a road",
    66:  "the sum of the clearest sky and Friar Laurence",
    67:  "the sum of the sum of a furry grandmother and a grandfather and Friar Laurence",
    68:  "the sum of Friar Laurence and a normal old road",
    69:  "the sum of a squirrel and the sum of Friar Laurence and a furry old pony",
    70:  "the sum of Friar Laurence and the sum of a bottomless large nose and a healthy tree",
    71:  "the sum of Friar Laurence and the difference between Paris and a roman",
    72:  "the difference between Paris and a foul fatherless infected dirty oozing rotten leech",
    73:  "the sum of the sum of Paris and a cat and Friar Laurence",
    74:  "the sum of Paris and the sum of a lovely sky and Friar Laurence",
    75:  "the sum of a Paris and the sum of Friar Laurence and the Apothecary",
    76:  "the sum of Friar Laurence and the difference between a normal black good smooth road "
         "and the reddest green rose",
    77:  "the sum of Friar Laurence and the difference between a brave charming handsome cute hero and the Apothecary",
    78:  "the sum of the difference between a mighty noble rich brave chihuahua and a healthy squirrel "
         "and Friar Laurence",
    79:  "the sum of Friar Laurence and the sum of a fair amazing beautiful fine angel and a hog",
    80:  "the difference between Friar Laurence and a dirty fat-kidneyed misused smelly flirt-gill",
    81:  "the difference between Friar John and Tybalt",
    82:  "the sum of Friar Laurence and the sum of a big mighty old gentle squirrel and a healthy door",
    83:  "the sum of a beautiful large blossoming green mistletoe and the sum of Friar Laurence and the Apothecary",
    84:  "the sum of Friar Laurence and the sum of the mighty fine joy and the huge pretty amazing sweet happiness",
    85:  "the difference between Friar John and the sum of the cube of the Apothecary and a flower",
    86:  "the difference between Friar John and the cube of the Apothecary",
    87:  "the sum of an angel and the difference between Friar John and the cube of the Apothecary",
    88:  "the sum of Friar Laurence and the difference between a big loving rich trustworthy aunt "
         "and a evil smelly villainous hound",
    89:  "the sum of the Apothecary and the difference between Friar John and the cube of the Apothecary",
    90:  "the sum of the difference between Friar John and the cube of the Apothecary and a golden furry hair",
    91:  "the sum of Friar Laurence and the cube of the Apothecary",
    # 92 not needed
    93:  "the sum of Friar Laurence and the difference between Tybalt and the Apothecary",
    # 94 - 96 not needed
    97:  "the difference between Friar John and the old rural loving red lantern",
    98:  "the sum of Tybalt and the sum of Friar Laurence and the bluest sky",
    99:  "the sum of Friar Laurence and the sum of Tybalt and the Apothecary",
    100: "the sum of Friar Laurence and the sum of Tybalt and the brave noble hero",
    101: "the sum of Friar John and the sum of a horrible stinking smelly codpiece and a hairy dusty hog",
    102: "the sum of the cursed foul infected blister and the difference between Friar John and the Apothecary",
    103: "the difference between Friar John and the sum of a delicious healthy sweet horse and a normal cat",
    104: "the sum of the sum of a beggar and Friar John and a half-witted disgusting sorry coward",
    105: "the sum of a villainous lying dirty bastard and Friar John",
    106: "the sum of a snotty oozing fat-kidneyed flirt-gill and the sum of a plum and Friar John",
    107: "the difference between Friar John and the sum of a tiny old proud chihuahua and a cowardly goat",
    108: "the sum of Friar John and the difference between the Apothecary and Paris",
    109: "the sum of Friar John and an infected stinking bastard",
    110: "the difference between Friar John and the Apothecary",
    111: "the difference between Friar John and a furry animal",
    112: "the sum of Friar John and a plague",
    113: "Friar John",
    114: "the sum of Friar John and the Lord",
    115: "the difference between Friar John and a fat pig",
    116: "the sum of Friar John and the Apothecary",
    117: "the sum of Friar John and a little gentle chihuahua",
    118: "the difference between Friar John and the sum of a fatherless vile devil and the Hell",
    119: "the sum of Friar John and the sum of the clearest sweetest summer's day and the reddest rose",
    120: "the sum of a black bottomless face and the sum of Friar John and the Apothecary",
    121: "the sum of Friar John and a smooth old rural stone wall",
    122: "the difference between twice Friar Laurence and the sum of a tiny old town and a large tree",
}
