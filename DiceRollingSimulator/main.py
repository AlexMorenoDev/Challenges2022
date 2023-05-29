import random

def roll_dice():
    print("Number: " + str(random.randint(1, 6)) + "")

def main():
    print("Welcome to Dice Rolling Simulator!")
    while True:
        user_input = input("Do you want to roll the dice? (y/n)")
        if user_input == 'n' or user_input == 'N':
            break

        if user_input != 'y' and user_input != 'Y':
            print("# ERROR: Invalid input! Try again!")
            continue
        
        roll_dice()

    print("Finishing Dice Rolling Simulator... See you soon!")

if __name__ == "__main__":
    main()