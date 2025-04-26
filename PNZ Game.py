#PNZ Game
#create a random number generator for a string of 3 numbers to be in an array
#Create evaluate guess method that gives the rules of the PNZ method
#display rule results
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


        
    
    

