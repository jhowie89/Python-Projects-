#PNZ Game
#create a random number generator for a string of 3 numbers to be in an array
#Create evaluate guess method that gives the rules of the PNZ method
#display rule results
"""
In the game of PNZ, one player thinks of a number consisting of three distinct digits. The other player repeatedly guesses the number and receives the following evaluation of the guess from the opponent:
• PPP means that each digit is in the correct position-the player has guessed the number.
Each P means that a digit is in the correct position, without saying which position that is.
Each N means that a digit occurs in the number, but it's not in the correct position.
A single Z means no digits are in the number.

Guess	Evaluation	Explanation
123	PPP	All digits correct and in the correct positions.
132	PNN	1 is in the correct position (P); 2 and 3 are correct digits but wrong positions (N).
145	PNZ	1 is correct and in the correct position (P); 2 is present but wrong position (N); 5 is not in the number (Z).
312	NNP	3 and 1 are in the number but wrong positions (N); 2 is in the correct position (P).
789	Z	None of the digits (7, 8, 9) are in 123.
124	PPZ	1 and 2 are correct and in the correct positions (PP); 4 is not in the number (Z).
231	NNP	2 and 3 are in the number but wrong positions (N); 1 is in the correct position (P).
"""
import random
print('Welcome to PNZ game')

def random_digits():
    #generate random digit
    return str(random.randint(0, 9))

def random_string():
    #generate random number as a string
    digits = []
    while len(digits) < 3:
        digit = random_digits()
        if digit not in digits:
            digits.append(digit)
    return "".join(digits)
    
def evaluateGuess(target, guess):
    p_count = 0 
    for number in range (3):
        if guess[number] == target[number]:
            p_count= p_count + 1
    n_count = 0 
    for number in range(3):
        if guess[number] in target and guess[number] != target[number]:
            n_count = n_count + 1
        
    if p_count == 3:
        return 'PPP'
    elif p_count > 0 or n_count > 0:
        return 'P' * p_count + 'N' * n_count 
    else:
        return 'Z'
        
print("Try to guess the 3-digit number (digits must be unique).")

target_number = random_string()

while True:
    guess = input("Enter your guess: ")
    
    result = evaluateGuess(target_number, guess)
    
    if result == "Invalid":
        print("Invalid input! Enter a 3-digit number with unique digits.")
    else:
        print(f"{guess} -> {result}")
        if result == "PPP":
            print("Congratulations! You guessed the correct number!")
            break


        
    
    

