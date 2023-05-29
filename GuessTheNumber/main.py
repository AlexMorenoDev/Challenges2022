import random

if __name__ == '__main__':
    guess = None
    target = random.randint(1, 100)
    score = 100
    next_clue = "The number is between 1 and 100 (both included)."
    i = 1

    input("Welcome to 'Guess the number' game! Press 'Enter' to start...")
    while guess != target and score > 0:
        print("Round " + str(i))
        print("Clue: " + next_clue)
        print("Score: " + str(score))
        try:
            guess = int(input("Guess the number: "))
        except:
            print("# Incorrect format! Please, enter a number.")
            continue
        
        if guess != target:
            score -= 5
            if guess < target:
                next_clue = "The number is greater than " + str(guess) + "."
            else:
                next_clue = "The number is smaller than " + str(guess) + "."
            i += 1
            
        print("----------------------------")

    if score > 0:
        print("Congratulations! You won, the number was " + str(target) + ". :)")
        print("Final score: " + str(score))
    else:
        print("Sorry! You lost. Your score is 0. :(")