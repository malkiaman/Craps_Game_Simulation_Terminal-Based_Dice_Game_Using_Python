import random

def roll_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1, die2

def craps_game():
    # First roll
    die1, die2 = roll_dice()
    sum_dice = die1 + die2
    print(f"First roll: {die1} + {die2} = {sum_dice}")
    
    # Check for immediate win or loss
    if sum_dice in (7, 11):
        return "You win!"
    elif sum_dice in (2, 3, 12):
        return "Craps! You lose!"
    
    # Establish the point
    point = sum_dice
    print(f"Point established: {point}")
    
    # Continue rolling until the point is made or a 7 is rolled
    while True:
        die1, die2 = roll_dice()
        sum_dice = die1 + die2
        print(f"Roll: {die1} + {die2} = {sum_dice}")
        
        if sum_dice == point:
            return "You win!"
        elif sum_dice == 7:
            return "You lose!"

# Run the game
result = craps_game()
print(result)
