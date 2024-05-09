# checks user enter yes (y) or no (n)
def yes_no(question):
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("you did not choose a valid response")


def instruction():
    print('''
    
**** instructions ****

To begin, decide the overall score needed to be crowned the winner of the game 
(eg: first person to get a score of 50 or more).

At the start of each round, the user and the computer each roll two dice. 
The initial number of points for each player is the total shown by the dice. Then, taking turns,
the user and computer each roll a single die and add the result to their points.
The goal is to get 13 points (or slightly less) for a given round. 
Once you are happy with your number of points, you can ‘pass’.
    
    ''')


# main routine
print()
print("🎲🎲 Roll it 13 🎲🎲")
print()

# loop for testing purposes


want_instructions = yes_no("Do you want to read the instructions? ")

if want_instructions == "yes":
    instruction()

print("program continues")
