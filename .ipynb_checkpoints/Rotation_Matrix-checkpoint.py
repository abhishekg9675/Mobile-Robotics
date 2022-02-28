import numpy as np

def rotation_matrix(axis, angle, derivative = False):
    
    angle = angle * np.pi/180
    if derivative == False: 
        if axis == 'x':
            matrix = np.array([[1, 0, 0], 
                           [0, np.cos(angle), -np.sin(angle)],
                           [0, np.sin(angle), np.cos(angle)]])
        elif axis == 'y':
            matrix = np.array([[np.cos(angle), 0, np.sin(angle)], 
                           [0, 1, 0],
                           [-np.sin(angle), 0, np.cos(angle)]])
        elif axis == 'z':
            matrix = np.array([[np.cos(angle), -np.sin(angle), 0], 
                           [np.sin(angle), np.cos(angle), 0],
                           [0, 0, 1]])
        else:
            print('Pick Correct Axis')
    else:
        if axis == 'x':
            matrix = np.array([[1, 0, 0], 
                           [0, -np.sin(angle), -np.cos(angle)],
                           [0, np.cos(angle), -np.sin(angle)]])
        elif axis == 'y':
            matrix = np.array([[-np.sin(angle), 0, np.cos(angle)], 
                           [0, 1, 0],
                           [-np.cos(angle), 0, -np.sin(angle)]])
        elif axis == 'z':
            matrix = np.array([[-np.sin(angle), -np.cos(angle), 0], 
                           [np.cos(angle), -np.sin(angle), 0],
                           [0, 0, 1]])
        else:
            print('Pick Correct Axis')
    
    
    return np.around(matrix, 4)