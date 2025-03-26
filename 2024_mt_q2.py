import numpy as np
import random
import pandas as pd
import matplotlib.pyplot as plt

def main():
    np.random.seed(50)

    arrXYZ = generatePointCloud()
    np.savetxt("point_cloud_atakan_eken.csv", arrXYZ, delimiter='*')

    df = convertPCToDataFrame(arrXYZ)

    maxB, minB = generateBoundaries()
    list_irem = findIndicesOfInnerPoints(df, maxB, minB)

    findPoints(arrXYZ, list_irem)
    plotFilteredPoints(arrXYZ, "inner_points_atakan_eken.csv", "outer_points_atakan_eken.csv")

def generateBoundaries():
    max_bound = np.array(np.random.randint(16, 19, size=3))
    min_bound = np.array(np.random.randint(2, 5, size=3))
    return max_bound, min_bound

def generatePointCloud():
    arrXYZ = np.array(np.random.randint(0, 20, size=(15, 3)))
    return arrXYZ

def convertPCToDataFrame(arr):
    sX = pd.Series(data=arr[:, 0])
    sY = pd.Series(data=arr[:, 1])
    sZ = pd.Series(data=arr[:, 2])
    df = pd.DataFrame({"axis_1": sX, "axis_2": sY, "axis_3": sZ})
    df.to_csv('point_cloud.csv', index=None, sep='/')
    return df

def findIndicesOfInnerPoints(df, maxb, minb):
    filtered = df[(df["axis_1"] >= minb[0]) & (df["axis_1"] <= maxb[0]) &
                  (df["axis_2"] >= minb[1]) & (df["axis_2"] <= maxb[1]) &
                  (df["axis_3"] >= minb[2]) & (df["axis_3"] <= maxb[2])]
    return filtered.index.tolist()

def findPoints(arr, indices):
    inner = arr[indices]
    outer = np.delete(arr, indices, axis=0)

    np.savetxt("inner_points_atakan_eken.csv", inner, delimiter='*')
    np.savetxt("outer_points_atakan_eken.csv", outer, delimiter='*')

def plotFilteredPoints(original, inner_file, outer_file):
    inner = np.loadtxt(inner_file, delimiter='*')
    outer = np.loadtxt(outer_file, delimiter='*')

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.scatter(inner[:, 0], inner[:, 1], inner[:, 2], c='red', label='Inner')
    ax.scatter(outer[:, 0], outer[:, 1], outer[:, 2], c='green', label='Outer')

    for i, point in enumerate(original):
        ax.text(point[0], point[1], point[2], str(i), fontsize=8)

    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')
    ax.legend()
    plt.show()

main()
