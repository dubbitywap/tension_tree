import numpy as np
import matplotlib.pyplot as plt
import sympy

def chord_length (theta):
    '''theta: angle between top of circle and vertical in degrees'''
    return 2*np.cos(np.radians(theta)) 

def number_of_vertices(theta):
    '''theta: angle between top of circle and vertical in degrees'''

    center_angle = 180 - 2*theta

    return sympy.lcm(center_angle.as_integer_ratio()[0],360*center_angle.as_integer_ratio()[1]) / center_angle
    
def dissonance (theta):
    '''theta: angle between top of circle and vertical in degrees
    returns the total length of the reflections'''

    return chord_length(theta)*number_of_vertices(theta)

if __name__ == "__main__" :
    angles = np.arange(0,90,1) 
    dissonances = np.zeros(len(angles))
    for i in range(len(angles)):
        dissonances[i] = dissonance(angles[i])
    plt.plot(angles,dissonances,'.')
    plt.show()
