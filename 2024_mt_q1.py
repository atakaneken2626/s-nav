import numpy as np
import random

def main():
    
   vector_1 = []
   vector_2 = []
   
   initalizeVector(vector_1)
   initalizeVector(vector_2)
   print("before vector_1: ",vector_1)
   print("before vector_2: ",vector_2)
   
   dot = dotProduct(vector_1, vector_2)
   print("dot: ",dot)
   
   orthogonalization(vector_1, vector_2)
   print("after vector_1",vector_1)
   print("after vector_2",["{:.1f}".format(x) for x in vector_2])
   
   result = check(vector_1,vector_2)
   if result == 1:
       print("yesss")
   elif result == 0:
       print("nooooo")
   else:
       print("idkkk")
       
   
def initalizeVector(v):
    for i in range(2):
        v.append(random.randint(2,8))

def dotProduct(v1, v2):
    
    dot = (v1[0] * v2[0]) + (v1[1] * v2[1])
    
    return dot

def orthogonalization(v1, v2):
    for i in range(2):
        v2[i] = (v2[i]-v1[i])* (dotProduct(v1,v2)/dotProduct(v1,v1))
        
def check(v1,v2):
    
    if(dotProduct(v1,v2)<1e-6):
        return True
    else:
        return False


main()