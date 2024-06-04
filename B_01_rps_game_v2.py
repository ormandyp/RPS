import random

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


# compares user / computer choice and returns
# result (win / lose / tie)
def rps_compare(user, comp):

    # if the user and the computer choice is the same, it's a tie
    if user == comp:
        round_result = "tie"

    # there are three ways to win
    elif user == "paper" and comp == "rock":
        round_result = "win"
    elif user == "scissors" and comp == "paper":
        round_result = "win"
    elif user == "rock" and comp == "scissors":
        round_result = "win"

    # if it's not a win / tie, then it's a loss
    else:
        round_result = "lose"

    return round_result


# Main routine stats here

# Initialise game variables
mode = "regular"

rounds_played = 0
rounds_tied = 0
rounds_lost = 0

rps_list = ["rock", "paper", "scissors", "xxx"]
game_history = []


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

    # randomly choose from the rps list (excluding the exit code)
    comp_choice = random.choice(rps_list[:-1])
    print("Computer choice", comp_choice)

    # get user choice
    user_choice = string_checker("choose : ", rps_list)
    print("you chose", user_choice)

    if user_choice == "xxx":
        break

    result = rps_compare(user_choice, comp_choice)

    # Adjust game Lost / game tied counters and add results to game history
    if result == "tie":
        rounds_tied += 1
        feedback = "It's a tie"
    elif result == "lose":
        rounds_lost += 1
        feedback = "😥😥 You lose. 😥😥"
    else:
        feedback = "🥳🥳Yon Won."

    # Set up round feedback and output it user.
    # Add it to the game history list (include the round number)
    round_feedback = f"{user_choice} vs {comp_choice}, {feedback}"
    history_item = f"Round: {rounds_played} - {round_feedback}"

    print(round_feedback)
    game_history.append(history_item)

    rounds_played += 1

    # if user are in infinite mode, increase number of rounds!
    if mode == "infinite":
        num_rounds += 1


    # Game loop ends here

    # Game history / Statistics area

if rounds_played > 0:
    # Calculate Stataistics
    rounds_won = rounds_played - rounds_tied - rounds_lost
    percent_won = rounds_won / rounds_played * 100
    percent_lost = rounds_lost / rounds_played * 100
    percent_tied = 100 - percent_won - percent_lost

    # Output Game Statistics
    print(" Game Statistics ")
    print(f"👍 Won: {percent_won:.2f} \t "
          f"😥 lost: {percent_lost:.2f} \t "
          f" Tied: {percent_tied:.2f}")

    # ask user if thay want to see their game history and output it if requested.
    see_history = string_checker("\nDo you want to see your game history? ")
    if see_history == "yes":
        for item in game_history:
            print(item)

    print()
    print("Thanks for playing.")

else:
    print("oops - You chickened out!")
