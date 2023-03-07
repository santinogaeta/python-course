# Quiz game that presents four questions for player to input their answers, and displays score and answers at the end

# Use a dictionary to contain key value pairs where <Question:Answer> pairs
questions = {
    'What year was the very first model of the iPhone released?':'A',
    'Who lives in a pineapple under the sea?':'B',
    'What is the longest running Broadway show?':'C',
    'What is the primary ingredients in hummus?':'D'
}

# Use 2D list to contains lists of answer-options to choose from for each question 
options = [
    ['A. 2007', 'B. 2008', 'C. 2009', 'D. Huh?'],
    ['A. Fish', 'B. SpongeBob Squarepants', 'C. People', 'D. That is absurd!'],
    ['A. Hamilton', 'B. Hadestown', 'C. Phantom of the Opera', 'D. Romeo and Juliet?'],
    ['A. Hummans', 'B. Garlic', 'C. Maize', 'D. Chickpeas'],
]

# how a new game is started and run throughout the game
def new_game():
    # empty list of guesses to start with
    guesses = []
    correct_guesses = 0
    question_num = 1

    # loops through each key (question) in dictionary, and loops through to display options for player to choose answer from
    for q in questions.keys():
        print('----------------------------')    
        print(q)
        for o in options[question_num-1]:
            print(o)
        # Awaits answer from player before checking it against correct answer and adds to score accordingly    
        current_guess = input('Is the answer A, B, C or D?: ').upper()
        guesses.append(current_guess)
        correct_guesses += check_answer(questions.get(q), current_guess)
        question_num += 1    
    # display the final score once all questions have been answered
    display_score(correct_guesses, guesses)

# checks player's answer against the correct answer for specific question
def check_answer(correct_answer, player_answer):
    # returns one point to score if correct
    if correct_answer == player_answer:
        print('\nCORRECT')
        return 1
    # no points scored if guess is incorrect
    else:
        print('INCORRECT')
        return 0

# Displays all correct answers, the player's answers and the player's score as a percentage at end of the game
def display_score(correct_guesses, player_guesses):
    print('----------------------------')
    print('Correct Answers:', end=" ")
    for answer in questions.values():
        print(answer, end=' ')
    print('\nPlayer Answers:', end=" ")
    for guess in player_guesses:
        print(guess, end=' ')
    percentage = int((correct_guesses/len(player_guesses))*100)
    print('\nYou got '+str(percentage)+'%')

# Takes a response from player to start a new game, or ends the session
def play_again():
    player_response = input('Would you like to try again? (yes/no): ').lower()
    # False causes the Quiz session to end
    if player_response != 'yes':
        return False
    # Returning True will continue the loop of new games until player opts out the next time
    else:
        return True


# start a new game to play
new_game()
# if play_again() return True, new games will continue to start until play_again() returns False
while play_again():
    new_game()
# message displayed when player opts out and ends the Quiz game session
print("Game Over! Thanks for playing!")

