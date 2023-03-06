# 

# 
def new_game():
    # empty list of guesses to start with
    # create tally for correct guesses
    # count for what question we're up to

    # for loop through each key (question) in dictionary 'questions'
      # print divider followed by the question
        # nested loop to print options for that q, using starting index for list (options[questionnumber-1])
        # After displaying options, increase question number    
      # get user input before moving to next question
      # add current guess to the list of guesses above
      # check_answer(), passing in questions.get(key) - question answer - and the current guess
        # this will return a value so add to correct guess tally
        # increase question number

    # display the final score (number of correct guesses, list of guesses)


# need to adjust for two parameters being passed through (question's answer and current guess)
def check_answer():
    # check if key (question's answer) is equal to the current guess
    # print whether they're correct or wrong and return point value accordingly


# need to adjust for two parameters being passed through (number of correct guesses, list of guesses)
def display_score():
    # loop through disctionary's keys to display the correct answers
    # loop through player's guesses to display the player's guesses
    # display final score

# 
def play_again():
    # take a response from player of yes or no?
    # check response and start new game accordingly

# Use a dictionary to contain key value pairs where <Question : Answer> pairs
# Try load in via file?
questions = {
    
}

# Use 2D list to contains lists of answer-options to choose from for each question 
options = [
    
]

# start a new game to play
new_game()

while play_again():
    new_game()

print("Game Over! Thanks for playing!")