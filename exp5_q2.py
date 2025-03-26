import numpy as np
import random

def main():
    
    LSMS = generate()
    
    if check(LSMS):
        print("yes magic numberss")
    else:
        print("no its nottt")
    
def check(grid):
    
    totals = np.zeros(8, dtype = 'int32')
    
    totals[0 : 3] = list(map(sum, grid))
    totals[3 : 6] = list(map(sum, zip(*grid)))
                         
    totals[6] = np.trace(grid)
    totals[7] = np.trace(grid[ : : -1])
    
    unique_values,occurence_count = np.unique(totals,return_counts=True)
    
    return occurence_count[0]==8

def generate():
    
    number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    random_number_list = np.array(random.sample(number_list, k = 9))
    
    matris_number = random_number_list.reshape(3, 3)
    
    print("3X3 MATRIS")
    print(matris_number)
    
    return matris_number
    
main()