# Dice Game of Chance: Python Implementation of Craps

## Overview
This Python project is a simulation of the classic **Craps** dice game. The program allows users to play a simple game of chance where two dice are rolled to determine a win, loss, or to establish a point that must be matched in subsequent rolls.

## Features
- Simulates dice rolls using Python's `random` module.
- Follows standard Craps rules:
  - Win on first roll with 7 or 11.
  - Lose on first roll with 2, 3, or 12.
  - Establishes a 'point' to match if no win/loss on first roll.
  - Continue rolling until the player either matches the point or rolls a 7 (which results in a loss).

## How It Works
1. On the first roll:
   - Win if the total is 7 or 11.
   - Lose if the total is 2, 3, or 12 (Craps).
   - Otherwise, the total becomes the “point”.
2. Roll continues:
   - If you roll the point again, you win.
   - If you roll a 7, you lose.
   - Otherwise, keep rolling until one of the two conditions is met.

## Sample Output
```
First roll: 3 + 4 = 7
You win!
```
Or:
```
First roll: 4 + 4 = 8
Point established: 8
Roll: 2 + 3 = 5
Roll: 6 + 2 = 8
You win!
```

## Requirements
- Python 3.x

## How to Run
Save the script as `craps_game.py` and run using:
```bash
python craps_game.py
```

## Use Cases
- Learn basic use of `random`, loops, and conditionals.
- Practice Python game logic and flow control.
- Fun mini-game to play in the terminal.

## Author
Malak Aman  
Email: itsmalkii@gmail.com  
