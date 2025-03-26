import numpy as np

QUESTION_NUMBER = 20

correct_answers = np.array(['A', 'C', 'A', 'A', 'D', 'B', 'C', 'A', 'C', 'B',
                 'A', 'D', 'C', 'A', 'D', 'C', 'B', 'B', 'D', 'A'])

student_answers = np.random.choice(['A', 'B', 'C', 'D'], QUESTION_NUMBER)

i = 0

print(correct_answers)
print(student_answers)

incorrect_answers=np.array(np.where((correct_answers != student_answers) == True))

print(incorrect_answers)
print(incorrect_answers.size)

if incorrect_answers.size < 15:
    print("cant pass exam")
    
else:
    print("congsss")