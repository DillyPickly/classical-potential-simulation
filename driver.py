import numpy as np
import csv
import config

positions     = np.zeros((config.N,2))
velocities    = np.zeros((config.N,2))
accelerations = np.zeros((config.N,2))
old_positions     = np.zeros((config.N,2))
old_velocities    = np.zeros((config.N,2))
old_accelerations = np.zeros((config.N,2))
masses        = np.zeros((config.N))
radii         = np.zeros((config.N))

def initialize_particles():
    return np.random.rand(config.N,2)

def initialize_masses():
    # uniform distribution
    return np.random.rand(config.N)*1e21

def initialize_radii():
    return np.ones((config.N))/60

def initialize_radii_prop_mass():
    return masses/(30*np.nanmax(masses))

def clear_data():
    filename = config.data_folder + '/' + config.sim_name + '_x.csv'
    with open( filename, 'w', newline='\n') as csvfile:
        pass
    filename = config.data_folder + '/' + config.sim_name + '_y.csv'
    with open( filename, 'w', newline='\n') as csvfile:
        pass
    filename = config.data_folder + '/' + config.sim_name + '_radii.csv'
    with open( filename, 'w', newline='\n') as csvfile:
        pass
    

def write_positions():
    filename = config.data_folder + '/' + config.sim_name + '_x.csv'
    with open( filename, 'a', newline='\n') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerow(positions[:,0])

    filename = config.data_folder + '/' + config.sim_name + '_y.csv'
    with open( filename, 'a', newline='\n') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerow(positions[:,1])

def write_radii():
    filename = config.data_folder + '/' + config.sim_name + '_radii.csv'
    with open( filename, 'a', newline='\n') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerow(radii)


def collision(i, j):
    # returns the new velocity of particle 
    # first I need to make the change in velocity be normal to the collision

    # project the vectors  (normal goes from j -> i)

    normal = old_positions[i,:] - old_positions[j,:]
    normal_hat = normal/np.sqrt(normal.dot(normal))
    parallel_hat = np.array([-normal_hat[1], normal_hat[0]])

    normal_velocity_i = old_velocities[i,:].dot(normal_hat)
    normal_velocity_j = old_velocities[j,:].dot(normal_hat)
    parallel_velocity_i = old_velocities[i,:].dot(parallel_hat)
    parallel_velocity_j = old_velocities[j,:].dot(parallel_hat)

    
    new_normal = (masses[i]*normal_velocity_i+masses[j]*normal_velocity_j+masses[j]*config.COR*(normal_velocity_j-normal_velocity_i))/(masses[i]+masses[j])


    return parallel_velocity_i*parallel_hat + new_normal*normal_hat


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

    try:
        masses = config.masses
    except:
        masses = initialize_masses()    


    try:
        radii = config.radii
    except:
        radii = initialize_radii_prop_mass()
    
    try:
        positions = config.positions
    except:
        positions = initialize_particles()

    try:
        velocities = config.velocities
    except:
        pass


    
    write_positions()
    write_radii()

    for i in range(config.iterations):
        old_positions     = np.copy(positions)
        old_velocities    = np.copy(velocities)
        old_accelerations = np.copy(accelerations)

        # update accelerations
        for i in range(config.N):
            accelerations[i,:] = 0
            for j in range(config.N):
                if i == j:
                    continue
                x,y = old_positions[i,:] - old_positions[j,:]
                m = masses[j]
                accelerations[i,:] -= derivative(config.potential,x,y,m)

        # update velocities
        velocities = old_velocities+delta_velocity()

        # update positions
        positions = old_positions+delta_position()

        # search for collisions
        for i in range(config.N):
            for j in range(config.N):
                if i == j:
                    continue
                diff = np.sum((positions[i,:] - positions[j,:])**2)
                if np.sqrt(diff) < (radii[i] + radii[j]):
                    velocities[i,:] = collision(i,j)

        # re-update the positions from the collisions
        positions = old_positions+delta_position()

                
            

        write_positions()

    print('data saved | ./{}'.format(config.data_folder))
    



    
