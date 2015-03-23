#!/usr/bin/python

#--------- Zeichenliste --------
#\t	9
#\n	10
#" "	32
#'      39
#,      44
#-      45
#.	46
#0-9	48-57
#:	58
#A-Z	65-90
#[	91
#]	93
#a-z	97-122

# Friar Laurence 64
# Friar John 113
# The Apothecary 3


def create_zeichentabelle():
    table = {}
    table[9] = "the square of the Apothecary."
    table[10] = "the sum of a rural cow and a furry large white horse." 
    table[32] = "a amazing beautiful blossoming tiny purple flower."
    
    table[39] = "the sum of the Apothecary and the sum of the peaceful sunny moon and a warm yellow old little pretty lantern."
    
    table[44] = "the difference between Friar Laurence and the sum of a healthy happy cute tiny pony and a beautiful red rose."
    table[45] = "the difference between Friar Laurence and the sum of a amazing golden lovely blossoming summer's day and the Apothecary."
    table[45] = "the difference between Friar Laurence and the sum of a amazing golden lovely blossoming summer's day and the Apothecary."
    table[46] = "the sum of Friar Laurence and the sum of the cursed half-witted damned distasteful flirt-gill and the snotty leech." 

    table[48] = "the sum of Friar Laurence and a foul rotten smelly villainous toad."
    table[49] = "the square of the difference between a famine and a fat-kidneyed sorry miserable starvation."
    table[50] = "the sum of a hamster and the square of the difference between a hound and a dirty disgusting hairy wolf." 
    table[51] = "the sum of a peaceful chihuahua and the square of the difference between a normal red fair morning and the wind."
    table[52] = "the difference between Friar Laurence and the sum of a charming noble pretty angel and a amazing sunny summer's day."
    table[53] = "the sum of the cube of the Apothecary and the difference between the cube of the Apothecary and a hero."
    table[54] = "the difference between Friar Laurence and the sum of the brave healthy noble Lord and a handsome hero."
    table[55] = "the difference between Friar Laurence and the sum of a happy cute gentle pony and a cat."
    table[56] = "the sum of Friar Laurence and a foul rotten oozing beggar."
    table[57] = "the sum of the difference between Friar Laurence and a brave mighty proud hero  and a hair." 
    table[58] = "the sum of the difference between Friar Laurence and a mighty noble brave King and a rural pony."
    table[63] = "the sum of Friar Laurence and the devil."
    table[65] = "the sum of Friar Laurence and a road."
    table[66] = "the sum of the clearest sky and Friar Laurence." 
    table[67] = "the sum of the sum of a furry grandmother and a grandfather and Friar Laurence." 
    table[68] = "the sum of Friar Laurence and a normal old road."
    table[69] = "the sum of a squirrel and the sum of Friar Laurence and a furry old pony."
    table[70] = "the sum of Friar Laurence and the sum of a bottomless large nose and a healthy tree."
    table[71] = "the sum of Friar Laurence and the difference between a black yellow blue cat and a roman." 
    table[72] = "the difference between a fair golden beautiful angel and a foul fatherless infected dirty oozing rotten leech."
    table[73] = "the sum of the sum of a normal tiny red pony and a cat and Friar Laurence."
    table[74] = "the sum of a golden yellow sunny lantern and the sum of a lovely sky and Friar Laurence." 
    table[75] = "the sum of a mighty sunny trustworthy kingdom and the sum of Friar Laurence and the Apothecary."
    table[76] = "the sum of Friar Laurence and the difference between a normal black good smooth road and the reddest green rose."
    table[77] = "the sum of Friar Laurence and the difference between a brave charming handsome cute hero and the Apothecary."
    table[78] = "the sum of the difference between a mighty noble rich brave chihuahua and a healthy squirrel and Friar Laurence." 
    table[79] = "the sum of Friar Laurence and the sum of a fair amazing beautiful fine angel and a hog." 
    table[80] = "the difference between Friar Laurence and a dirty fat-kidneyed misused smelly flirt-gill."
    table[81] = "the difference between Friar John and a tiny little furry old purple chihuahua." 
    table[82] = "the sum of Friar Laurence and the sum of a big mighty old gentle squirrel and a healthy door." 
    table[83] = "the sum of a beautiful large blossoming green mistletoe and the sum of Friar Laurence and the Apothecary."
    table[84] = "the sum of Friar Laurence and the sum of the mighty fine joy and the huge pretty amazing sweet happiness."
    table[85] = "the difference between Friar John and the sum of the cube of the Apothecary and a flower."
    table[86] = "the difference between Friar John and the cube of the Apothecary."
    table[87] = "the sum of an angel and the difference between Friar John and the cube of the Apothecary."
    table[88] = "the sum of Friar Laurence and the difference between a big loving rich trustworthy aunt and a evil smelly villainous hound."
    table[89] = "the sum of the Apothecary and the difference between Friar John and the cube of the Apothecary."
    table[90] = "the sum of the difference between Friar John and the cube of the Apothecary and a golden furry hair."

    table[91] = "the sum of Friar Laurence and the cube of the Apothecary."

    table[93] = "the sum of Friar Laurence and the difference between the clearest reddest sweetest amazing golden morning and the Apothecary."

    table[97] = "the difference between Friar John and the old rural loving red lantern."
    table[98] = "the sum of a red furry cute loving pretty cat and the sum of Friar Laurence and the bluest sky."
    table[99] = "the sum of Friar Laurence and the sum of the large sunny peaceful happy proud kingdom and the Apothecary."
    table[100] = "the sum of Friar Laurence and the sum of the amazing fine bold brave charming king and the mighty noble hero."
    table[101] = "the sum of Friar John and the sum of a horrible stinking smelly codpiece and a hairy dusty hog."
    table[102] = "the sum of the cursed foul infected blister and the difference between Friar John and the Apothecary."
    table[103] = "the difference between Friar John and the sum of a delicious healthy sweet horse and a normal cat."
    table[104] = "the sum of the sum of a beggar and Friar John and a half-witted disgusting sorry coward."
    table[105] = "the sum of a villainous lying dirty bastard and Friar John."
    table[106] = "the sum of a snotty oozing fat-kidneyed flirt-gill and the sum of a plum and Friar John."
    table[107] = "the difference between Friar John and the sum of a tiny old proud chihuahua and a cowardly goat."
    table[108] = "the sum of Friar John and the difference between the Apothecary and a furry green tiny hamster."
    table[109] = "the sum of Friar John and an infected stinking bastard."
    table[110] = "the difference between Friar John and the Apothecary."
    table[111] = "the difference between Friar John and a furry animal."
    table[112] = "the sum of Friar John and a plague."
    table[113] = "Friar John."
    table[114] = "the sum of Friar John and the Lord."
    table[115] = "the difference between Friar John and a fat pig."
    table[116] = "the sum of Friar John and the Apothecary."
    table[117] = "the sum of Friar John and a little gentle chihuahua."
    table[118] = "the difference between Friar John and the sum of a fatherless vile devil and the Hell."
    table[119] = "the sum of Friar John and the sum of the clearest sweetest summer's day and the reddest rose."
    table[120] = "the sum of a black bottomless face and the sum of Friar John and the Apothecary."
    table[121] = "the sum of Friar John and a smooth old rural stone wall."
    table[122] = "the difference between twice Friar Laurence and the sum of a tiny old town and a large tree."
    return table

def int_to_roman(input):
   if type(input) != type(1):
      raise TypeError, "expected integer, got %s" % type(input)
   if not 0 < input < 4000:
      raise ValueError, "Argument must be between 1 and 3999"   
   ints = (1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1)
   nums = ('M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')
   result = ""
   for i in range(len(ints)):
      count = int(input / ints[i])

      result += nums[i] * count
      input -= ints[i] * count
   return result


table = create_zeichentabelle()
import sys
from Frame import *
from words import *
from random import choice
sys.stdout = open("test.spl", "w")

print prefix

# create datastack
#<auto>
#Juliet:
#	Rember the sum of ...
#Capulet:
#	You are as worried as the sum of yourself and the son.
#</auto>
#done after the definition of codeblock

codeblock = [code_block_print_prefix]

#<auto>
#Montague:
#	You are as ... as .. .
#	Speak your Mind.
#Capulet:
#	You are as ... as .. .
#	Speak your Mind.
#</auto>

characters = ["Capulet:", "Montague:"]
character_no = 1
youareas = ["You are as ", "Thou art as "]
for char in prefix:
    codeblock += [characters[character_no]]
    line = ["\t", choice(youareas), choice(adjectives), " as ", table[ord(char)]]
    codeblock += ["".join(line)]
    codeblock += ["\tSpeak your mind."]
    character_no = 1 - character_no

codeblock += [code_block_reverse_stack]

#<auto>
#Juliet:
#	Rember 
#</auto>

for char in "Juliet:\n\tRemember ":
    line = ["\t", choice(youareas), choice(adjectives), " as ", table[ord(char)]]
    codeblock += ["".join(line)]
    codeblock += ["\tSpeak your mind."]

codeblock += ["\tYou are as villainous as Montague."]

#<auto>
#	You are as good as Montague
#	Are you as good as <codierung von a>
#	If so let us proceed to scene <scene von a>
#	...
#</auto>

ordered_keys = sorted(table.keys())
scene_numbers = []

for i in xrange(len(ordered_keys)):
    scene_numbers.append(int_to_roman(i+3))

for scene_number, key in zip(scene_numbers, ordered_keys):
    line = ["\t", "Are you as ", choice(adjectives), " as ", table[key][:-1], "?"]
    codeblock += ["".join(line)]
    codeblock += ["\tIf so, let us proceed to scene " + scene_number + "."]

codeblock += [code_block_act_3_scene_2]

#<auto>
#\n
#Capulet:
#	You are as worried as the sum of yourself and the son.
#</auto>


for char in "\nCapulet:\n\tYou are as worried as the sum of yourself and the son.":
    line = ["\t", choice(youareas), choice(adjectives), " as ", table[ord(char)]]
    codeblock += ["".join(line)]
    codeblock += ["\tSpeak your mind."]

codeblock += [code_block_return_from_act_3]

#<auto>
#	Scene __: Even more accusations.
#
#Capulet:\n
# for char in codierung a 
#    You are as good as <codierung von char>.
#    Speak your mind.
#</auto>


for scene_number, key in zip(scene_numbers, ordered_keys):
    codeblock += ["\t\tScene " + scene_number + ": Even more accusations.\n"]
    codeblock += ["Capulet:"]    
    for char in table[key]:
	line = ["\t", choice(youareas), choice(adjectives), " as ", table[ord(char)]]
	codeblock += ["".join(line)]
	codeblock += ["\tSpeak your mind."]
    codeblock += ["\tLet us return to scene II.\n"]


codeblock += [code_block_act_4_scene_1]

code = "\n".join(codeblock)

for char in code:
    print "Juliet:"
    print "\tRemember "  + table[ord(char)]
    print "Capulet:"
    print "\tYou are as worried as the sum of yourself and the son."

# create datastack
#<auto>
#Juliet:
#	Rember the sum of ...
#Capulet:
#	You are as worried as the sum of yourself and the son.
#</auto>


print code
