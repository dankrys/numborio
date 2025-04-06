import sys
import random

print("Welcome to Numborio! You get 3 points for a good answer and minus 1 point for the wrong one. Good luck!")
print("Type q and press enter to exit the game.")

score = 0
goodAnswerScore = 3
badAnswerScore = -1

while True:
    a = random.randint(0, 9)
    b = random.randint(0, 9)
    result = a + b

    print(str(a) + " + " + str(b) + " = ")

    for answer in sys.stdin:
        answer = answer.strip()
        
        if answer == 'q':
            print("Your final score is " + str(score))
            sys.exit(0)
        elif answer.isdigit() and int(answer) == result:
            score += goodAnswerScore
            print("Good job. Your current score is " + str(score))
        else:
            if score > 0:
                score += badAnswerScore
            print("Wrong answer. Correct answer is " + str(result) + ". Your current score is " + str(score))
        break