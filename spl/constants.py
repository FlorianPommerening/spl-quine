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
    9:   "the square of the Apothecary.",
    10:  "the sum of a rural cow and a furry large white horse.",
    # 11 - 31 not needed
    32:  "a amazing beautiful blossoming tiny purple flower.",
    # 33 - 38 not needed
    39:  "the sum of the Apothecary and the sum of the peaceful sunny moon and a warm yellow old little pretty lantern.",
    # 40 - 43 not needed
    44:  "the difference between Friar Laurence and the sum of a healthy happy cute tiny pony and a beautiful red rose.",
    45:  "the difference between Friar Laurence and the sum of a amazing golden lovely blossoming summer's day "
         "and the Apothecary.",
    46:  "the sum of Friar Laurence and the sum of the cursed half-witted damned distasteful flirt-gill "
         "and the snotty leech.",
    # 47 not needed
    48:  "the sum of Friar Laurence and a foul rotten smelly villainous toad.",
    49:  "the square of the difference between a famine and a fat-kidneyed sorry miserable starvation.",
    50:  "the sum of a hamster and the square of the difference between a hound and a dirty disgusting hairy wolf.",
    51:  "the sum of a peaceful chihuahua and the square of the difference between a normal red fair morning "
         "and the wind.",
    52:  "the difference between Friar Laurence and the sum of a charming noble pretty angel "
         "and a amazing sunny summer's day.",
    53:  "the sum of the cube of the Apothecary and the difference between the cube of the Apothecary and a hero.",
    54:  "the difference between Friar Laurence and the sum of the brave healthy noble Lord and a handsome hero.",
    55:  "the difference between Friar Laurence and the sum of a happy cute gentle pony and a cat.",
    56:  "the sum of Friar Laurence and a foul rotten oozing beggar.",
    57:  "the sum of the difference between Friar Laurence and a brave mighty proud hero  and a hair.",
    58:  "the sum of the difference between Friar Laurence and a mighty noble brave King and a rural pony.",
    # 59 - 62 not needed
    63:  "the sum of Friar Laurence and the devil.",
    # 64 not needed
    65:  "the sum of Friar Laurence and a road.",
    66:  "the sum of the clearest sky and Friar Laurence.",
    67:  "the sum of the sum of a furry grandmother and a grandfather and Friar Laurence.",
    68:  "the sum of Friar Laurence and a normal old road.",
    69:  "the sum of a squirrel and the sum of Friar Laurence and a furry old pony.",
    70:  "the sum of Friar Laurence and the sum of a bottomless large nose and a healthy tree.",
    71:  "the sum of Friar Laurence and the difference between a black yellow blue cat and a roman.",
    72:  "the difference between a fair golden beautiful angel "
         "and a foul fatherless infected dirty oozing rotten leech.",
    73:  "the sum of the sum of a normal tiny red pony and a cat and Friar Laurence.",
    74:  "the sum of a golden yellow sunny lantern and the sum of a lovely sky and Friar Laurence.",
    75:  "the sum of a mighty sunny trustworthy kingdom and the sum of Friar Laurence and the Apothecary.",
    76:  "the sum of Friar Laurence and the difference between a normal black good smooth road "
         "and the reddest green rose.",
    77:  "the sum of Friar Laurence and the difference between a brave charming handsome cute hero and the Apothecary.",
    78:  "the sum of the difference between a mighty noble rich brave chihuahua and a healthy squirrel "
         "and Friar Laurence.",
    79:  "the sum of Friar Laurence and the sum of a fair amazing beautiful fine angel and a hog.",
    80:  "the difference between Friar Laurence and a dirty fat-kidneyed misused smelly flirt-gill.",
    81:  "the difference between Friar John and a tiny little furry old purple chihuahua.",
    82:  "the sum of Friar Laurence and the sum of a big mighty old gentle squirrel and a healthy door.",
    83:  "the sum of a beautiful large blossoming green mistletoe and the sum of Friar Laurence and the Apothecary.",
    84:  "the sum of Friar Laurence and the sum of the mighty fine joy and the huge pretty amazing sweet happiness.",
    85:  "the difference between Friar John and the sum of the cube of the Apothecary and a flower.",
    86:  "the difference between Friar John and the cube of the Apothecary.",
    87:  "the sum of an angel and the difference between Friar John and the cube of the Apothecary.",
    88:  "the sum of Friar Laurence and the difference between a big loving rich trustworthy aunt "
         "and a evil smelly villainous hound.",
    89:  "the sum of the Apothecary and the difference between Friar John and the cube of the Apothecary.",
    90:  "the sum of the difference between Friar John and the cube of the Apothecary and a golden furry hair.",
    91:  "the sum of Friar Laurence and the cube of the Apothecary.",
    # 92 not needed
    93:  "the sum of Friar Laurence and the difference between the clearest reddest sweetest amazing golden morning "
         "and the Apothecary.",
    # 94 - 96 not needed
    97:  "the difference between Friar John and the old rural loving red lantern.",
    98:  "the sum of a red furry cute loving pretty cat and the sum of Friar Laurence and the bluest sky.",
    99:  "the sum of Friar Laurence and the sum of the large sunny peaceful happy proud kingdom and the Apothecary.",
    100: "the sum of Friar Laurence and the sum of the amazing fine bold brave charming king "
         "and the mighty noble hero.",
    101: "the sum of Friar John and the sum of a horrible stinking smelly codpiece and a hairy dusty hog.",
    102: "the sum of the cursed foul infected blister and the difference between Friar John and the Apothecary.",
    103: "the difference between Friar John and the sum of a delicious healthy sweet horse and a normal cat.",
    104: "the sum of the sum of a beggar and Friar John and a half-witted disgusting sorry coward.",
    105: "the sum of a villainous lying dirty bastard and Friar John.",
    106: "the sum of a snotty oozing fat-kidneyed flirt-gill and the sum of a plum and Friar John.",
    107: "the difference between Friar John and the sum of a tiny old proud chihuahua and a cowardly goat.",
    108: "the sum of Friar John and the difference between the Apothecary and a furry green tiny hamster.",
    109: "the sum of Friar John and an infected stinking bastard.",
    110: "the difference between Friar John and the Apothecary.",
    111: "the difference between Friar John and a furry animal.",
    112: "the sum of Friar John and a plague.",
    113: "Friar John.",
    114: "the sum of Friar John and the Lord.",
    115: "the difference between Friar John and a fat pig.",
    116: "the sum of Friar John and the Apothecary.",
    117: "the sum of Friar John and a little gentle chihuahua.",
    118: "the difference between Friar John and the sum of a fatherless vile devil and the Hell.",
    119: "the sum of Friar John and the sum of the clearest sweetest summer's day and the reddest rose.",
    120: "the sum of a black bottomless face and the sum of Friar John and the Apothecary.",
    121: "the sum of Friar John and a smooth old rural stone wall.",
    122: "the difference between twice Friar Laurence and the sum of a tiny old town and a large tree.",
}