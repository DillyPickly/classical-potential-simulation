import numpy as np
import csv
import config

positions     = np.zeros((config.N,2))
velocities    = np.zeros((config.N,2))
accelerations = np.zeros((config.N,2))

def initialize_particles():
    return np.random.rand(config.N,2) #, np.random.rand(config.N)

def write_positions():
    with open( config.filename, 'a', newline='\n') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerow(positions[:,0])
        csvwriter.writerow(positions[:,1])

# central difference method
# the derivative of potential = acceleration
def derivative(func, x, y, h=1e-8):
    return (func(x + h,y) - func(x - h, y))/2*h, (func(x, y + h) - func(x, y - h))/2*h

def delta_position(t = 1):
    return velocities*t
    
def delta_velocity(t = 1):
    return accelerations*t
        
if __name__ == '__main__':
    positions = initialize_particles()
    write_positions()

    for i in range(config.iterations):
        
        # update accelerations
        for i in range(config.N):
            accelerations[i,:] = 0
            for j in range(config.N):
                if i == j:
                    continue
                x,y = positions[i,:] - positions[j,:]
                accelerations[i,:] += derivative(config.potential,x,y)

        accelerations = 1e18*accelerations

        # update velocities
        velocities = velocities+delta_velocity()

        # update positions
        positions = positions+delta_position()

        write_positions()

    



    
