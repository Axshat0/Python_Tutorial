#Random mudule
import random

# Generate a random integer between 1 and 9 (inclusive) and store it in 'x'.
x = random.randint(1, 9)
print(x)

# Generate a random float between 0 and 1 (exclusive) and store it in 'y'.
y = random.random()
print(y)

game = ['rock', 'paper', 'scissors']

# Choose a random item from the 'game' list and store it in 'z'.
z = random.choice(game)
print(z)

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'J', 'Q', 'K', 'A']

# Shuffle the 'cards' list randomly.
random.shuffle(cards)

# Print the shuffled 'cards' list.
print(cards)
