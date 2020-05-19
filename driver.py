import numpy as np
import csv
import config

positions     = np.zeros((config.N,2))
velocities    = np.zeros((config.N,2))
accelerations = np.zeros((config.N,2))
masses        = np.zeros((config.N))

def initialize_particles():
    return np.random.rand(config.N,2)

def initialize_masses():
    # uniform distribution
    return np.random.rand(config.N)*100+1e20

def clear_data():
    with open( config.filename, 'w', newline='\n') as csvfile:
        pass

def write_positions():
    with open( config.filename, 'a', newline='\n') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerow(positions[:,0])
        csvwriter.writerow(positions[:,1])

# central difference method
# the derivative of potential = acceleration
def derivative(func, x, y, m, h=1e-8):
    return (func(x + h, y, m) - func(x - h, y, m))/2*h, (func(x, y + h, m) - func(x, y - h, m))/2*h

def delta_position(t = 1):
    return velocities*t
    
def delta_velocity(t = 1):
    return accelerations*t
        
if __name__ == '__main__':
    clear_data()

    positions = initialize_particles()
    masses = initialize_masses()
    write_positions()

    for i in range(config.iterations):

        # update accelerations
        for i in range(config.N):
            accelerations[i,:] = 0
            for j in range(config.N):
                if i == j:
                    continue
                x,y = positions[i,:] - positions[j,:]
                m = masses[i]
                accelerations[i,:] -= derivative(config.potential,x,y,m)

        # update velocities
        velocities = velocities+delta_velocity()

        # update positions
        positions = positions+delta_position()

        write_positions()

    print('data saved | ./{}'.format(config.filename))
    



    
