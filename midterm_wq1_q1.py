import random
import numpy as np

M_PI = np.pi

def main():
    #empyt lists
    p1_list = []
    p2_list = []
    p3_list = []
    
    #listeleri initialize edecek
    initializeCoordinates(p1_list, p2_list, p3_list)
    
    print("P1_list: ", p1_list)
    print("P2_list: ", p2_list)
    print("P3_list: ", p3_list)
    
    #initialize edilen listeleri normal vectore çevirecek
    vector_list = calculateNormals(p1_list, p2_list, p3_list)
    
    print("normal vector: ", vector_list)

    # vektörün açılarını hesaplayacak
    angle_list = calculateAngles(vector_list)
    angle_list = [round(angle, 2) for angle in angle_list]
    print("angles: ", angle_list)
    
    #aynı düzlemde olup olmadıgını karşılaştır
    if isSameSurface(angle_list):
        print("agalar aynı düzlemde")
    else:
        print("agalar aynı düzlemde değil")
    
    
def initializeCoordinates(p1, p2, p3):
    
    for i in range(3):
        p1.append(random.randint(7, 15))
        p2.append(random.randint(7, 15))
        p3.append(random.randint(7, 15))
        
def calculateNormals(p1, p2, p3):
        
    nx = ((p2[1] - p1[1]) * (p3[2] - p1[2])) - ((p2[2] - p1[2]) * (p3[1] -p1[1]))
    ny = ((p2[2] - p1[2]) * (p3[0] - p1[0])) - ((p2[0]- p1[0]) * (p3[2] - p1[2]))
    nz = ((p2[0] - p1[0]) * (p3[1] - p1[1])) - ((p2[1] - p1[1]) * (p3[0] - p1[0]))
        
    return [nx, ny, nz]
    
def calculateAngles(v):
    
    angX = np.arccos(v[0] / np.sqrt(v[0]**2 + v[1]**2 + v[2]**2)) * (180 / M_PI)
    angY = np.arccos(v[1] / np.sqrt(v[0]**2 + v[1]**2 + v[2]**2)) * (180 / M_PI)
    angZ = np.arccos(v[2] / np.sqrt(v[0]**2 + v[1]**2 + v[2]**2)) * (180 / M_PI)
    
    return [angX, angY, angZ]

def isSameSurface(a):
    
    thres = 5
    
    if (np.absolute(a[0] - a[1]) < thres) & (np.absolute(a[0] - a[2]) < thres) & (np.absolute(a[2] - a[1]) < thres):
        return True
    else:
        return False
    



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
main()