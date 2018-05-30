The Marble Game
======================================================
I finally want to solve that one game at my
grandma's house, the one with all those marbles on a
board. We begin in this configuration:
    @ @ @
  @ @ @ @ @
@ @ @ @ @ @ @
@ @ @ O @ @ @
@ @ @ @ @ @ @
  @ @ @ @ @
    @ @ @
Where @s represent marbles and the central
hole is open. When a marble jumps over another marble,
the jumped marble is taken out. The goal is to
be left with just one marble.

So to solve this, I wrote this little game thing.
To play the marble game, you run run.py on round with the flag
-p. You just type

  python run.py round -p

All you will see is the start of the game

------------WELCOME--------------
  0 1 2 3 4 5 6 7 8
0       @ @ @
1     @ @ @ @ @
2   @ @ @ @ @ @ @
3   @ @ @ O @ @ @
4   @ @ @ @ @ @ @
5     @ @ @ @ @
6       @ @ @

You then specify a move in the game with this syntax:

=j-i-direction

Which says to jump the marble at (i, j) in whatever direction
you gave. Thus =1-4-down will jump the marble at (4, 1) to down.
Thus:

  python run.py round -p =1-4-down

will leave you with this configuration

0 1 2 3 4 5 6 7 8
0       @ @ @
1     @ @ O @ @
2   @ @ @ O @ @ @
3   @ @ @ @ @ @ @
4   @ @ @ @ @ @ @
5     @ @ @ @ @
6       @ @ @

As you may have expected, there are a few game modes:
round and rect. You saw round already. Rect look like:

------------WELCOME--------------
  0 1 2 3 4 5 6 7 8
0       @ @ @
1       O @ @
2       @ @ @
3       @ @ @

To have the game solved for you, you can just enter

  python run.py round -s

And we brute force the answer.

(upon further inspection though, you can see that the round puzzle is impossible)
See clarification.txt for the proof
