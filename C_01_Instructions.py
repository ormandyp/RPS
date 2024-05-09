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


# main routine
print()
print("Rock / Paper / Scissors game ")
print()

# ask user if they want to see the instructions
# them if requested
want_instructions = string_checker("Do you want to read the instructions? ")

if want_instructions == "yes":
    instruction()

print("program continues")
