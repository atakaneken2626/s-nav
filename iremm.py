import numpy as np
import pandas as pd
import random
def main():
    v1_list = []
    v2_list =[]
    initalizeVectors(v1_list)
    initalizeVectors(v2_list)
    print("V1:",v1_list)
    print("V2:",v2_list)

    dot = dotProduct(v1_list,v2_list)
    print("Dot Product:",dot)

    orthogonalization(v1_list,v2_list)
    print("After Coordinates for V1:",v1_list)
    print("After Coordinates for V2:",v2_list)

    result = check(v1_list,v2_list)
    if result == 1:
        print("Process is correct")
    else:
        print("Process is not correct")

def initalizeVectors(l):
    random.seed(10)
    for i in range(2):
        l.append(random.randint(2,8))
def dotProduct(v1,v2):
    dot = v1[0]*v2[0] + v1[1]*v2[1]
    return dot
def orthogonalization(v1,v2):
    for i in range(2):
        v2[i]=(v2[i] - v1[i] )* (dotProduct(v1,v2)/dotProduct(v1,v1))

    #v2xOrth = (v2[0] - v1[0] )* (dotProduct(v1,v2)/dotProduct(v1,v1))
    #v2yOrth = (v2[1] - v1[1]) * (dotProduct(v1, v2) / dotProduct(v1, v1))
    #return [v2xOrth, v2yOrth]
def check(v1,v2):
    if dotProduct(v1,v2)<1e-6:
        return 1
    else:
        return 0
main()