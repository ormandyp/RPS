# Check that users have entered a valid
# option based on a list
def string_checker(question, valid_ans=('yes', 'no')):

    error = f"Please enter a valid option from the list: {valid_ans}"

    while True:

        # get user response and make sure its lowercase
        user_response = input(question).lower()

        for item in valid_ans:
            # check if the user response is a word in the list
            if item == user_response:
                return item

            # check if the user response is the same as
            # the first letter of an item in the list
            elif user_response == item[0]:
                return item

        # print error if user does not enter somthing that is valid
        print(error)
        print()


def instruction():
    print('''

**** instructions ****

To begin, choose the numbers of rounds (or press <enter> for
infinite mode).

Then play against the computer. You need to choose R (rock),
P (paper) or S (scissors.

The rules are as follows:
o Paper beats rock
o Rock beats scissors
o Scissors beats paper

press <xxx> to end the game at anytime

Good luck!

    ''')


def int_check(question):
    while True:
        error = "Please enter an integer that is 1 or more."

        to_check = input(question)

        # check for infinite mode
        if to_check == "":
            return "infinite"

        try:
            response = int(to_check)

            if response < 1:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# Main routine stats here

# Intialise game variables
mode = "regular"
rounds_played = 0


rps_list = ["rock", "paper", "scissors", "xxx"]


print("Rock / Paper / Scissors Game")
print()

# ask user if they want to see the instructions
# them if requested
want_instructions = string_checker("Do you want to read the instructions? ")

if want_instructions == "yes":
    instruction()


# Ask user for number of rounds / infinite mode
num_rounds = int_check("How many rounds would you like? Push <enter> for infinite mode: ")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5


# game loop starts here
while rounds_played < num_rounds:

    # rounds headings
    if mode == "infinite":
        rounds_heading = f"\n Round {rounds_played + 1} (Infinite Mode) "
    else:
        rounds_heading = f"\n Round {rounds_played + 1} of {num_rounds} "

    print(rounds_heading)
    print()

    # get user choice
    user_choice = string_checker("choose : ", rps_list)
    print("you chose", user_choice)

    if user_choice == "xxx":
        break

    rounds_played += 1
    print("rounds played: ", rounds_played)

    # if user are in infinite mode, increase number of rounds!
    if mode == "infinite":
        num_rounds += 1


# Game loop ends here

# Game history / Statistics area
