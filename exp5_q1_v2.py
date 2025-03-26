import numpy as np
import random

def main():
    
    correct_answers =[]
    
    student_answers = []
    
    for i in range(20):
        student_answers.append(random.choice('ABCD'))
        correct_answers.append(random.choice('ABCD'))
    print("student: ",student_answers)
    print("\ncorrect: ",correct_answers)

    trues = 0
    falses = 0
    for i in range(20):
        if(student_answers[i] == correct_answers[i] ):
            trues = trues + 1
        else:
            falses = falses + 1
        i = i + 1
        
    print("trues: ",trues)
    print("falses: ",falses)
    
    if (trues > 15):
        print("helal aga")
    else:
        print("aga kafanı sikim")
main()
