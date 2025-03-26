import random
import numpy as np

def main():
    
    newArr = generates()
    
    print("3x3 matris: \n",newArr)
    
    result = check(newArr)
    
    print(result)
    
def generates():
    
    arr = np.array([1,2,3,4,5,6,7,8,9])
    
    random.shuffle(arr)
    
    newArr = arr.reshape(3,3)
    
    return newArr

def check(arr):
    
    check_list = []
    
    for i in range (8):
        check_list.append(0)
    
    for i in range(3): #satırları topladık
        check_list[i] = int(np.sum([arr[i]]))
        
    check_list[3:6] = list(map(sum, zip(*arr)))
# =============================================================================
#     check_list[3] = int(np.sum([arr[:, 0]]))
#     check_list[4] = int(np.sum([arr[:, 1]]))
#     check_list[5] = int(np.sum([arr[:, 2]]))
# =============================================================================
    
    check_list[6] = int(np.trace(arr))
    check_list[7] = int(np.trace(arr[::-1]))
    
        

        
    
    
    
    return check_list
main()