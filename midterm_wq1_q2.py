import random
import numpy as np
import pandas as pd
pd.set_option('display.max_rows', None)  
pd.set_option('display.max_columns', None)  
pd.set_option('display.max_colwidth', None)  
pd.set_option('display.expand_frame_repr', False)

def main():
   
    NOP, thresh, K = getParameters()    
    
    num_arr = generatePointCloud(NOP)
    
    neighbors_dict = findKNeighbors(num_arr, K)
    
    for i in range(NOP):
        print(i,neighbors_dict[i])
    

    inlier, outlier = filterPC(num_arr, neighbors_dict, thresh)


def getParameters():
    
    NOP = int(input("enter NOP: "))
    thresh = int(input("enter thresh: "))
    K = int(input("enter K: "))
    
    print("NOP: ", NOP)
    print("thresh: ", thresh)
    print("K: ", K)
    
    return NOP, thresh, K

def generatePointCloud(NOP):
    
    num_arr = np.array(np.random.randint(100,200, size=(int(NOP), 3)))
    print("Numpy array: ", num_arr)
    
    return num_arr

def findKNeighbors(num_arr, K):
    
    neighbors = {}
    
    for i in range(len(num_arr)):
        distance = []
        
        for j in range(len(num_arr)):
            if i != j:
                dist = int(np.sqrt(((num_arr[i,0]-num_arr[j,0])**2 + (num_arr[i,1]-num_arr[j,1])**2 +(num_arr[i,2]-num_arr[j,2])**2 )))
                distance.append((dist))
        
        distance.sort()
        neighbors[i] = distance[:K]
        
    return neighbors
    
def filterPC(num_arr, neighbors, thresh):
    
    dataFrame = pd.DataFrame(neighbors)
    
    print(dataFrame)
    
    results_series = pd.Series(dataFrame.loc[:].mean())
    
    print(results_series)
    
    inlier = results_series.mask(results_series < thresh)
    outlier = results_series.mask(results_series >= thresh)
    
    inlier = inlier.dropna()
    outlier = outlier.dropna()
    print(inlier)
    print(outlier)
    
    
    return inlier, outlier
    

    
    
    
    
    



main()
    