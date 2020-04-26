import json
import requests
import random
import html

play = True
correct_answers = 0
wrong_answers = 0
while play == True:
    r = requests.get("https://opentdb.com/api.php?amount=1&category=12&difficulty=easy&type=multiple")
    if (r.status_code != 200):
        print("sorry, there was no answer from a provider"+ "\n")
        quit_game = input("do you want to play again? type no to quit game or just press enter to continue "+ "\n")
        if (quit_game == "no"):
            play = False
    else:
        answer_number = 1
        response_text = r.text
        question = json.loads(response_text)

        options = []
        for x in question['results'][0]['incorrect_answers']:
            options.append(x)

        options.append(question['results'][0]['correct_answer'])
        random.shuffle(options)
        
        print("===========================================")
        print("The question is: " + html.unescape(question['results'][0]['question']) + "\n")
        
        for option in options:
            print(str(answer_number) + "- " +  html.unescape(option) )
            answer_number += 1
        user_answer = int(input("Please type the number of you answer: " + "\n"))
        correct_answer = str(question['results'][0]['correct_answer'])
        if (options[user_answer-1] ==  correct_answer):
            correct_answers += 1
            print("your answer is correct :) ")
            quit_game = input("do you want to play again? type no to quit game or just press enter to continue " + "\n")
            if (quit_game == "no"):
                play = False
        else:
            print("OUCH!! Sorry your answer " + str(user_answer) + " is wrong"+ "\n")
            wrong_answers += 1
            print("The correct answer was " + str(question['results'][0]['correct_answer']) )
            quit_game = input("do you want to play again? type no to quit game or just press enter to continue "+ "\n")
            if (quit_game == "no"):
                play = False

print("===========================================")
print("Your final score is: ")
print("  Correct answers = " + str(correct_answers))
print("  Wrong answers = " + str(wrong_answers))
print("  Thanks for playing the game")
print("===========================================")
