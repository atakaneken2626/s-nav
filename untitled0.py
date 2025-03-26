import random
import numpy as np
import pandas as pd

def main():
    
    
    lenght_cube, step_size = getParameters()
    
    numpy_array = generatePointCloud(lenght_cube)
    print("numpy_array:\n",numpy_array)
    
    dataFrame = writePCToDataFrameAndFile(numpy_array)

    print("data frame:\n",dataFrame)
    
    voxel = findPointsInAVoxel(numpy_array, lenght_cube, step_size)
    
    calculateVoxelMeans(voxel,lenght_cube,step_size)
    
def getParameters():
    
    lenght_cube = int(input("lenght cube: "))
    step_size = int(input("step size: "))
    
    return lenght_cube, step_size

def generatePointCloud(lc):
    
    coordinates = np.array(np.random.randint(0,lc, size=(5,3)))
              
    return coordinates
                

def writePCToDataFrameAndFile(array):
    
    seriesX = pd.Series(array[:,0])
    seriesY = pd.Series(array[:,1])
    seriesZ = pd.Series(array[:,2])
    
    print("ser:\n",seriesX)
    
    seri_df = pd.DataFrame()
    
    seri_df = seri_df.assign(x = seriesX, y = seriesY, z = seriesZ)
    
    seri_df.to_csv('file.csv', index=True)
    
    return seri_df

def findPointsInAVoxel(arr, lc, ss):
    
    voxels={}
    for i in range (0,lc,ss):
        for j in range (0,lc,ss):
            for k in range (0,lc,ss):
                voxels[(i,j,k)]=arr[((arr[:,0]>=i) & (arr[:,0]<=i+ss-1)) & \
                   ((arr[:,1]>=j) & (arr[:,1]<=j+ss-1)) & \
                   ((arr[:,2]>=k) & (arr[:,2]<=k+ss-1))]
    return voxels


def calculateVoxelMeans(voxel,lc,ss):
    
    arr = np.array(np.zeros(0,0, size=len(voxel)))
    
    i = 0
    for key,value in voxel.items():
        arr[i] = np.mean(value)
        i=i+1
        
    











main()
