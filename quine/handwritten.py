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
"""

# In the initial setup, we set the values of our constants and then get
# Capulet and Juliet on stage to define the data stack.
# We define the stack in order and push it on the stack letter by letter,
# so the data will be in reverse order and we have to use Capulet instead of
# Montague.
# TODO: moving the constant definition into the code section and jumping there from here might save some lines.
PREFIX_SETUP = """
\t\t\tAct I: Prelude.

\t\tScene I: Forgetful Capulet.

[Enter Friar John and Friar Laurence]

Friar John:
\tYou are as brave as the square of a honest handsome healthy hero.
Friar Laurence:
\tYou are as lovely as the sum of myself and the square of the difference
\tbetween the sweetest clearest pretty face and a rose.

[Exit Friar Laurence]
[Enter the Apothecary]

Friar John:
\tThou art as trustworthy as the sum of a cunning roman and a cat.

[Exeunt]
[Enter Capulet and Juliet]

"""

# =============== DATA SECTION ===============

# === Generated block: Data definition ===
# The next couple of million lines will be automatically generated. They push
# data on the stack (Capulet) that will later be used by the code block to
# recreate the data block and then to recreate the code block.
# For each letter in the code block, the data block contains one line that
# pushes the ascii code of that letter on the reversed data stack.

# To push a letter on the stack, Juliet tells Capulet to remember this letter:
DATA_PUSH_COMMAND_BEFORE = """Juliet:
\tRemember """
# Capulet then responds with a command that increases the value to Juliet to
# count the new item (Note that the "." that ends Juliet's sentence):
DATA_PUSH_COMMAND_AFTER = """.
Capulet:
\tYou are as worried as the sum of yourself and the son."""

# These two commands are repeated until all data is on Capulet in reversed order.

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

# We start by printing the prefix.
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


# TODO: document starting from here.

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

CODE_PRINT_DATA_LOOP = """
\t\tScene IV: Romeo's answer.

[Exeunt]
[Enter Romeo and Juliet]

Romeo:
\tYou are as loving as me.



\t\tAct II: Output.

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
\tWe shall proceed to act III."""

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


CODE_PRINT_CODE_LOOP = """
\t\tScene IV: Montague loses it.

[Exeunt]
[Enter Montague and Romeo]

Montague:
\tAre you as good as nothing?
\tIf so, we must proceed to act IV.

Romeo:
\tRecall my forbidden love.
\tSpeak your mind.

Montague:
\tYou are as rotten as the sum of yourself and the plague.
\tWe must return to scene IV."""

UTILITY_PRINT_PUSH_COMMAND_START = """

\t\t\tAct III: Meta Play.

\t\tScene I: Capulet's accusations.

Capulet:
\tRemember yourself."""
#<auto>
#Juliet:
#\tRemember
#</auto>
UTILITY_SWITCH_CASE_START = "\tYou are as villainous as Montague."
#<auto>
#\tAre you as good as <spl code of a>
#\tIf so let us proceed to scene <scene of a>
#\t...
#</auto>


UTILITY_SWITCH_CASE_END = """
\t\tScene II: More accusations.

Capulet:"""

#<auto>
#\n
#Capulet:
#\tYou are as worried as the sum of yourself and the son.
#</auto>


UTILITY_PRINT_PUSH_COMMAND_END = """
\tRecall everything I told you.
\tWe shall return to act II.
"""

UTILITY_PRINT_CHARACTER_START = """

\t\tScene %s: Even more accusations."""
UTILITY_PRINT_CHARACTER_ACTORS = ["Capulet"]
#<auto>
#\tScene __: Even more accusations.
#
#Capulet:\n
# for char in "<spl code of a>"
#\tYou are as good as <spl code of char>.
#\tSpeak your mind.
#</auto>
UTILITY_PRINT_CHARACTER_END = "\tLet us return to scene II."

CODE_END_OF_PROGRAM = """
\t\t\tAct IV: Fin.

\t\tScene I: No questions left.

[Exeunt]
"""



# We need strings for numbers to stay constant in some places,
# because we have to write code that prints SPL code that will print certain symbols.

# We only define constant numbers literals for the symbols we need:
#  \t       9
#  \n      10
#  (space) 32
#  '       39
#  ,       44
#  -       45
#  .       46
#  0-9     48-57
#  :       58
#  ?       63
#  A-Z     65-90
#  [       91
#  ]       93
#  a-z     97-122

# To keep the strings short, we also assume that some variables have certain values
# Friar Laurence  64
# Friar John     113
# The Apothecary   3

NUMBERS = {
    9:   "the square of the Apothecary",
    10:  "the sum of a rural cow and a furry large white horse",
    # 11 - 31 not needed
    32:  "an amazing beautiful blossoming tiny purple flower",
    # 33 - 38 not needed
    39:  "the sum of the Apothecary and the sum of the peaceful sunny moon and a warm yellow old little pretty lantern",
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
    51:  "the sum of a peaceful chihuahua and the square of the difference between a normal red fair morning "
         "and the wind",
    52:  "the difference between Friar Laurence and the sum of a charming noble pretty angel "
         "and a amazing sunny summer's day",
    53:  "the sum of the cube of the Apothecary and the difference between the cube of the Apothecary and a hero",
    54:  "the difference between Friar Laurence and the sum of the brave healthy noble Lord and a handsome hero",
    55:  "the difference between Friar Laurence and the sum of a happy cute gentle pony and a cat",
    56:  "the sum of Friar Laurence and a foul rotten oozing beggar",
    57:  "the sum of the difference between Friar Laurence and a brave mighty proud hero  and a hair",
    58:  "the sum of the difference between Friar Laurence and a mighty noble brave King and a rural pony",
    # 59 - 62 not needed
    63:  "the sum of Friar Laurence and the devil",
    # 64 not needed
    65:  "the sum of Friar Laurence and a road",
    66:  "the sum of the clearest sky and Friar Laurence",
    67:  "the sum of the sum of a furry grandmother and a grandfather and Friar Laurence",
    68:  "the sum of Friar Laurence and a normal old road",
    69:  "the sum of a squirrel and the sum of Friar Laurence and a furry old pony",
    70:  "the sum of Friar Laurence and the sum of a bottomless large nose and a healthy tree",
    71:  "the sum of Friar Laurence and the difference between a black yellow blue cat and a roman",
    72:  "the difference between a fair golden beautiful angel "
         "and a foul fatherless infected dirty oozing rotten leech",
    73:  "the sum of the sum of a normal tiny red pony and a cat and Friar Laurence",
    74:  "the sum of a golden yellow sunny lantern and the sum of a lovely sky and Friar Laurence",
    75:  "the sum of a mighty sunny trustworthy kingdom and the sum of Friar Laurence and the Apothecary",
    76:  "the sum of Friar Laurence and the difference between a normal black good smooth road "
         "and the reddest green rose",
    77:  "the sum of Friar Laurence and the difference between a brave charming handsome cute hero and the Apothecary",
    78:  "the sum of the difference between a mighty noble rich brave chihuahua and a healthy squirrel "
         "and Friar Laurence",
    79:  "the sum of Friar Laurence and the sum of a fair amazing beautiful fine angel and a hog",
    80:  "the difference between Friar Laurence and a dirty fat-kidneyed misused smelly flirt-gill",
    81:  "the difference between Friar John and a tiny little furry old purple chihuahua",
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
    93:  "the sum of Friar Laurence and the difference between the clearest reddest sweetest amazing golden morning "
         "and the Apothecary",
    # 94 - 96 not needed
    97:  "the difference between Friar John and the old rural loving red lantern",
    98:  "the sum of a red furry cute loving pretty cat and the sum of Friar Laurence and the bluest sky",
    99:  "the sum of Friar Laurence and the sum of the large sunny peaceful happy proud kingdom and the Apothecary",
    100: "the sum of Friar Laurence and the sum of the amazing fine bold brave charming king "
         "and the mighty noble hero",
    101: "the sum of Friar John and the sum of a horrible stinking smelly codpiece and a hairy dusty hog",
    102: "the sum of the cursed foul infected blister and the difference between Friar John and the Apothecary",
    103: "the difference between Friar John and the sum of a delicious healthy sweet horse and a normal cat",
    104: "the sum of the sum of a beggar and Friar John and a half-witted disgusting sorry coward",
    105: "the sum of a villainous lying dirty bastard and Friar John",
    106: "the sum of a snotty oozing fat-kidneyed flirt-gill and the sum of a plum and Friar John",
    107: "the difference between Friar John and the sum of a tiny old proud chihuahua and a cowardly goat",
    108: "the sum of Friar John and the difference between the Apothecary and a furry green tiny hamster",
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