import sys, random, time, os

#--- The reason I use classes instead of global variables is because they are easier to use inside of functions and it is simpler. ---#
class global_variable:
    def __init__(self, number_list: list, score: int):
        self.number_list = number_list
        self.score = score

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
global_variable = global_variable(number_list = numbers, score = 0)

def loading():
    os.system("clear")
    print("loading.")
    time.sleep(0.7)
    os.system("clear")
    print("loading..")
    time.sleep(0.7)
    os.system("clear")
    print("loading...")
    time.sleep(0.7)
    os.system("clear")


def entry_point():
    os.system("clear")
    print("Welcome to number gusser!")
    print("============================")
    print("[1] Play the game")
    print("[2] Exit the program")
    print("[3] See your score")
    match input('Choose: '):
        case '1':
            loading()
            active_game()
        case '2':
            input("You have terminated the program")
            sys.exit()
        case '3':
            loading()
            players_score()
        case _:
             input("Invalid entry")
             entry_point()

def active_game():
    os.system("clear")
    #--- Generatse a random number once ---#
    random_number = random.choice(global_variable.number_list)
    
    while True:
        try:
            guess = int(input("Choose a number: "))
            
            if guess == random_number:
                input(f"Your answer is correct. The number was {random_number}!\nScore +1")
                global_variable.score += 1
                os.system("clear")
                break
            elif guess > random_number:
                input(f"Your guess {guess} was MORE THAN the random number")
                os.system("clear")
            elif guess < random_number:
                input(f"Your guess {guess} was LESS THAN the random number")
                os.system("clear")
            else:
                input("Unknown error has occurred")
                os.system("clear")

        except ValueError:
            input("Your guess has to be a number!.")
            os.system("clear")
            
    entry_point()
    
def players_score():
    os.system("clear")
    print("_*_*_*_*_*_*_*_*_*_*_*_*_*_*_")
    print(f"Players current score: {global_variable.score}")
    print("_*_*_*_*_*_*_*_*_*_*_*_*_*_*_")
    input("Press 'ENTER' to go back to main menu.")
    entry_point()
 
    
    
entry_point()
