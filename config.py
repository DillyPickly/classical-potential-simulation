import numpy as np
# This file defines all appriopriate parameters for the simulation


# Number of Iterations
iterations = 1000

# The number of particles
N = 100

# The particle masses | can be given as a vector/list or a single value
m = 10

# The potential used to update the particle position and velocity
# The x and y is calculated from the particle in question to the particle being affected
# m is the mass of the particle n question not the particle being affected.
potential = lambda x,y,m : -(G*m)/np.sqrt(x**2 + y**2)

# Data Filename/graph visualization name
filename = 'data/gravity_sim.csv'
animation_name = 'graphs/gravity_sim.gif'

# Universal  Constants
G = 6.67408E-11 # m^3/kg/s^2

# Animation Frame Skipping
skip = 1 # uses everyframe