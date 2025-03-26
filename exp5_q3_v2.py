import numpy as np
import random

def main():
    
    dict = {2:("A","B","C"), 3:("D","E","F"), 
            4:("G","H","I"), 5:("J","K","L"),
            6:("M","N","O"), 7:("P","Q","R"),
            8:("T","U","V"), 9:("W","X","Y","Z")}
    
    num = input("enter num: ")
    
    num_list = list(num)
    
    print(num_list)
    
    first_part = num_list[0:3]
    second_part = num_list[4:8]
    third_part = num_list[9:12]
    
    print(first_part)
    print(second_part)
    print(third_part)
    
    second = []
    for k in second_part:
        for key,value in dict.items():
            if k in value:
                second.append(key)
                
    third = []
    for k in third_part:
        for key,value in dict.items():
            if k in value:
                third.append(key)  
            
    print("second: ",second)
    print("third: ",third)
            
    phone_number = [first_part, "-", second, "-", third]
    
    print("phone number ", phone_number)
    
    
main()