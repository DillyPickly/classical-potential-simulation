import numpy as np
# This file defines all appriopriate parameters for the simulation


# Number of Iterations
iterations = 15

# The number of particles
N = 121
# N = 20

# The particle masses | can be given as a vector/list otherwise they are automatically created
masses = 3e18*np.ones(N)
masses[57] = 1e25
masses[63] = 1e25


# masses = 3e10*np.ones(N)
# masses[60] = 1e20

# masses = 3e10*np.ones(N)
# masses[0] = 1e20

# Specify the radii
radii = .5e-1*np.ones(N)
radii[57] = 3e-1
radii[63] = 3e-1

# radii = .5e-1*np.ones(N)
# radii[60] = 3e-1

# radii = .5e-1*np.ones(N)
# radii[0] = 3e-1

# specifiy the positions
positions = np.zeros((N,2))
index = 0
for i in range(-5,6):
    for j in range(-5,6):
        
        positions[index,:] = np.array([i,j])
        index+=1


# positions = np.zeros((N,2))
# index = 0
# for i in range(-5,6):
#     for j in range(-5,6):
        
#         positions[index,:] = np.array([i,j])
#         index+=1

# positions = np.zeros((N,2))
# for i in range(1,N):
#     positions[i,1] = i/2

# specify the velocities
velocities = np.zeros((N,2))
velocities[57] = 6e-4*np.array([-1,0])
velocities[63] = 6e-4*np.array([1,0])

# velocities = np.zeros((N,2))
# index = 0
# for i in range(-5,6):
#     for j in range(-5,6):
#         if i == 0 and j == 0:
#             index+=1
#             continue
#         velocities[index,:] = 5e-3*np.array([j,-i])/(np.sqrt(i**2 + j**2))
#         index+=1


# velocities = np.zeros((N,2))
# for i in range(1,N):
#     velocities[i,0] = 3e-2/i


# The potential used to update the particle position and velocity
# The x and y is calculated from the particle in question to the particle being affected
# m is the mass of the particle n question not the particle being affected.
potential = lambda x,y,m : -(G*m)/np.sqrt(x**2 + y**2)

# Data Filename/graph visualization name
data_folder  = 'data'
animation_folder = 'graphs'
sim_name     = 'gravity'

# Universal  Constants
# G = 6.67408E-11 # m^3/kg/s^2
G = 1e-8

# Animation Frame Skipping
# skip = 1 # uses everyframe

# collision coefficient of restitution
COR = .6