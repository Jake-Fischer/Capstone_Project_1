"""
A quiz program. 
This program is designed to ask the user to choose a topic they would like to be quized on from a bank of topics and their respective questions and answers. 
The program then asks the stored questions and tracks the number of questions the user answers correctly (the case of the user answers does not matter).
This program will work if more topics are added too the question bank.
It will also work if more questions and answers are added to a topic already in the question bank
"""

def main():

    question_bank = {

        # Be consistent with spacing around operators/symbols, and whitespace before/after 
        # curly braces when using newlines. 
        # The : and , would have no space before, one space after. 
    
        'art': {
            'Who painted the Mona Lisa?': 'Leonardo Da Vinci',
            'What precious stone is used to make the artist\'s pigment ultramarine?': 'Lapiz lazuli',
            'Anish Kapoor\'s bean-shaped Cloud Gate scuplture is a landmark of which city?': 'Chicago',
        },
        
        'space': {
            'Which planet is closest to the sun?': 'Mercury',
            'Which planet spins in the opposite direction to all the others in the solar system?': 'Venus',
            'How many moons does Mars have?': '2'
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
        print(f'Your total score on {user_topic} questions was {score} out of {len(user_questions)}.')
        if score == len(user_questions): # Check if user entered all correct answers.
            print('You got all the answers correct!')
    else:
        print('Not a valid topic, restart the program to try again.')



def ask_questions(user_questions):
    """ A documentation string would be helpful here. 
    Describe this function does, what are the expected arguments, and what does it return? """

    score = 0
    for question in user_questions: # Loop through the dictionary of questions and answers
        answer = input(question + ': ') # Prompt the user with the question
        # Recommend converting both strings to lowercase here, so it's obvious that 
        # the lowercase version of both strings are used in the comparison. 
        # This also preserves the original form of the user's answer in case that is needed again in the program. 
        if answer.lower() == user_questions[question].lower(): # If the answer is correct, add one to score, if not display the correct answer.
            print('Correct!')
            score += 1
        else:
            print(f'Sorry, the correct answer is {user_questions[question]}')
            print('End of topic questions!') # This is being a little picky but a function shouldn't make assumptions about how it will
            # be used in a program. This function's job is to ask one set of questions and return the score for those questions. 
            # It doesn't know it's part of an entire quiz, and you could easily modify the rest of the program so the user 
            # can try more questions on another topic, and then the message would be misleading. 

    return score
    
main()


