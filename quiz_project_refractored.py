""" A quiz program. 
This program is designed to ask the user for a topic. 
The program then asks a series of questions about the topic and tracks the number of questions the user got correct.
The case of the user answers does not matter."""

def main():

    question_bank = {
        'art' : {
            'Who painted the Mona Lisa?': 'Leonardo Da Vinci',
            'What precious stone is used to make the artist\'s pigment ultramarine?': 'Lapiz lazuli',
            'Anish Kapoor\'s bean-shaped Cloud Gate scuplture is a landmark of which city?' : 'Chicago'
            },
        
        'space' : {
            'Which planet is closest to the sun?': 'Mercury',
            'Which planet spins in the opposite direction to all the others in the solar system?': 'Venus',
            'How many moons does Mars have?' : '2'
            }
            }

    # Print each question topic, prompt the user for topic, and convert the topic to lowercase
    print("Here are the available quiz topics:\n")
    for topic in question_bank:
        print(topic)
    user_topic = input('\nPlease type which topic you would like to be quizzed on: ').lower()

    # Check to see if topic chosen is in question_bank. If it is, send the topic's questions to the ask_questions function.
    if user_topic in question_bank:
        user_questions = question_bank[user_topic]
        score = ask_questions(user_questions) # ask_questions returns an integer representing the score.
        print(f'Your total score on {user_topic} questions was {score} out of 3.')
        if score == len(user_questions): # Check if user entered all correct answers.
            print('You got all the answers correct!')
    else:
        print('Not a valid topic, restart the program to try again.')



def ask_questions(user_questions):
    score = 0
    for question in user_questions: # Loop through the dictionary of questions and answers
        answer = input(question + ': ').lower() # Prompt the user with the question
        if answer == user_questions[question].lower(): # If the answer is correct, add one to score, if not display the correct answer.
            print('Correct!')
            score += 1
        else:
            print(f'Sorry, the correct answer is {user_questions[question]}')
    print('End of quiz!')
    return score
    
main()


