# Dice Game Project

This is my solution for the Dice Game problem.

## Description

Given a set of 6-side dices (and given the numbers on each face of each dice),
find the dice whose probability of winning is higher against all other dices.

If there isn't such best dice, then find the best rival for each dice.

Also, determine if the player should choose the dice first or second in order
to have the best probability to win.

## Tasks

### First task: Compare two dices

Implement a function that takes two dices as input and computes two values: the
first value is the number of times the first dice wins (out of all possible 36
choices), the second value is the number of times the second dice wins. We say
that a dice wins if the number on it is greater than the number on the other
dice.

To debug your implementation, use the following test cases:

**Sample 1**

*Input:* `dice1 = [1, 2, 3, 4, 5, 6], dice2 = [1, 2, 3, 4, 5, 6]`

*Output:* `(15, 15)`

**Sample 2**

*Input:* dice1 = [1, 1, 6, 6, 8, 8], dice2 = [2, 2, 4, 4, 9, 9]

*Output:* `(16, 20)`
