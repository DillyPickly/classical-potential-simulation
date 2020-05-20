import numpy as np
# This file defines all appriopriate parameters for the simulation


# Number of Iterations
iterations = 500

# The number of particles
N = 100

# The particle masses | can be given as a vector/list or a single value

# The potential used to update the particle position and velocity
# The x and y is calculated from the particle in question to the particle being affected
# m is the mass of the particle n question not the particle being affected.
potential = lambda x,y,m : -(G*m)/np.sqrt(x**2 + y**2)

# Data Filename/graph visualization name
data_folder  = 'data'
animation_folder = 'graphs'
sim_name     = 'gravity'

# Universal  Constants
G = 6.67408E-11 # m^3/kg/s^2

# Animation Frame Skipping
skip = 1 # uses everyframe

# collision coefficient of restitution
COR = .3