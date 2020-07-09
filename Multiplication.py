"""Imports"""
from random import randrange as r
import time
from time import time as t
import csv

"""Numbers of questions and the highest number used in """
print('Math Tutor - MULTIPLICATION')
quests = int(input('How many questions do you want?: '))
high_num = int(input('Highest number used in practice?: '))
"""Countdown"""
input('Hit any key to Start:\n')
print('Get ready in: ')
for i in range(1, 3):
    print(i)
    time.sleep(1)
print('GO!\n<<<<<<<<<<<<<<<<<<<<<<<')
"""Reset Score"""
score = 0
answer_list = []
"""Timer start"""
start_time = t()
"""Loop"""
for no in range(quests):
    num1, num2 = r(1, high_num + 1), r(1, high_num + 1)
    ans = num1 * num2
    try:
        u_ans = int(input(f'{num1} X {num2} = '))
    except:
        print('Error: Answer not an Integer')
    else:
        pass
    finally:
        answer_list.append(f'Answer: {num1} X {num2} = {ans}. Your answer: {u_ans}')
    if u_ans == ans:
        score += 1
    """Timer Ends"""
    end_time = t()

print(
    f'<<<<<<<<<<<<<<<<<<<<<<<\n> Thanks for playing! <\n<<<<<<<<<<<<<<<<<<<<<<<\n'
    f'Your results:\nYou got {score} out of {quests} - ({round(score / quests * 100)}%) '
    f'correct in {round(end_time - start_time,1)} seconds.\n'
    f'(Speed: {round((end_time - start_time) / quests,1)} seconds/question)\n'
    f'<<<<<<<<<<<<<<<<<<<<<<<')
for result in answer_list:
    print(result)

fields = ['Question:', 'Answer:']
rows1 = answer_list

filename = "math_tutor.csv"

with open(filename, 'w+') as math_tutor:
    write = csv.writer(math_tutor)
    rows1 = [s.strip('Answer: ') for s in rows1]
    try:
        for quests in rows1:
            rows1 = [k.split('.') for k in rows1]
            rows1 = [k.split(',') for k in rows1]
    except:
        pass
    else:
        rows1 = [i.split(',') for i in rows1]
        print(f'Ln: 74')
    finally:
        write.writerow(fields)
        write.writerows(rows1)