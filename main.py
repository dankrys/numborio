import sys
import random

print("Welcome to Numborio!")

currentQuestionNo = 0
maxQuestions = 3

while currentQuestionNo < maxQuestions:
    a = random.randint(0, 9)
    b = random.randint(0, 9)
    result = a + b

    print(str(a) + " + " + str(b) + " = ")

    for answer in sys.stdin:
        if (int(answer) == result):
            print("Good job")
        else:
            print("Wrong answer. Correct answer is " + str(result))
        break

    currentQuestionNo += 1