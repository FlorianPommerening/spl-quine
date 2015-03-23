prefix = """An Epic Never-Ending Saga.

Montague, a stacky person.
Romeo, his son he can always count on.
Capulet, the plain opposite of Montague.
Juliet, his daughter, always remembering where he put his stuff.
The Apothecary, a triple split personality.
Friar John, just a number in His herd.
Friar Laurence, wields the power the loving mighty noble Lord.


			Act I: Prelude.

		Scene I: Forgetful Capulet.

[Enter Friar John and Friar Laurence]

Friar John:
	You are as brave as the square of a honest handsome healthy hero.
Friar Laurence:
	You are as lovely as the sum of myself and the square of the difference between the sweetest clearest pretty face and a rose.

[Exit Friar Laurence]
[Enter the Apothecary]

Friar John:
	Thou art as trustworthy as the sum of a cunning roman and a cat.

[Exeunt]
[Enter Capulet and Juliet]

"""
#<auto>
#Juliet:
#	Rember the sum of ...
#Capulet:
#	You are as worried as the sum of yourself and the son.
#</auto>
code_block_print_prefix = """
[Exit Juliet]

		Scene II: Reenactment of the Past.

[Enter Montague]

"""
#<auto>
#Montague:
#	You are as ... as .. .
#	Speak your Mind.
#Capulet:
#	You are as ... as .. .
#	Speak your Mind.
#</auto>
code_block_reverse_stack = """
[Exeunt]
[Enter Romeo and Juliet]

Juliet:
    You are as loving as me.

	    Scene III: Reunion.

[Exeunt]
[Enter Capulet and Montague]

Montague:
    You are as dirty as Juliet.
    Are you better than nothing?
    If not, let us proceed to scene IV.
    Recall your unhappy childhood.

Capulet:
    Remember me.

[Exit Capulet]
[Enter Juliet]

Montague:
    You are as smelly as the sum of yourself and a flirt-gill.
    We must return to scene III.
		

	    Scene IV: Romeo's answer.

[Exeunt]
[Enter Romeo and Juliet]

Romeo:
    You are as loving as me.


		Act II: Output.

	    Scene I: Retaliation.

[Exeunt]
[Enter Capulet and Montague]

Capulet:
    You are as dirty as Romeo.
    Are you better than nothing?
    If not, let us proceed to scene II.
    Recall your unhappy childhood.

Montague:
    Remember me.

[Exit Montague]
[Enter Romeo]

Capulet:
    You are as smelly as the sum of yourself and a wolf.
    We shall proceed to act III.

	    Scene II: Juliet's answer.

[Exeunt]
[Enter Romeo and Juliet]

Juliet:
    You are as loving as me.

	Scene III: Re-Retaliation.

[Exeunt] 
[Enter Capulet and Montague]

Montague:
    You are as dirty as Juliet.
    Are you better than nothing?
    If not, let us proceed to scene IV.
    Recall your unhappy childhood.

Capulet:
    Remember me.

[Exit Capulet]
[Enter Juliet]

Montague:
    You are as smelly as the sum of yourself and a flirt-gill.
    We must return to scene III.

	Scene IV: Montague loses it.

[Exeunt]
[Enter Montague and Romeo]

Montague:
    Are you as good as nothing?
    If so, we must proceed to act IV.

Romeo:
    Recall my forbidden love.
    Speak your mind.

Montague:
    You are as rotten as the sum of yourself and the plague.
    We must return to scene IV.


	    Act III: Meta Play.

	Scene I: Capulet's accusations.

Capulet:
    Remember yourself."""
#<auto>
#Juliet:
#	Rember 
#</auto>

#<auto>
#	You are as good as Montague
#	Are you as good as <codierung von a>
#	If so let us proceed to scene <scene von a>
#	...
#</auto>


code_block_act_3_scene_2="""
	Scene II: More accusations.

Capulet:
"""

#<auto>
#\n
#Capulet:
#	You are as worried as the sum of yourself and the son.
#</auto>


code_block_return_from_act_3="""
	Recall everything I told you.
	We shall return to act II.
"""

#<auto>
#	Scene __: Even more accusations.
#
#Capulet:\n
# for char in codierung a 
#    You are as good as <codierung von char>.
#    Speak your mind.
#</auto>

code_block_act_4_scene_1="""
	    Act IV: Fin.
	
	Scene I: No questions left.

[Exeunt]
"""




