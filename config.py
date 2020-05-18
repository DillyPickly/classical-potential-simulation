# This file defines all appriopriate parameters for the simulation



# Number of Iterations
iterations = 200

# The number of particles
N = 100

# The particle masses | can be given as a vector/list or a single value
m = 10

# The potential used to update the particle position and velocity
# The x and y is calculated from the particle in question to the particle being affected
potential = lambda x,y : G/(x**2 + y**2)

# Data Filename/graph visualization name
filename = 'data/gravity_sim_100.csv'
animation_name = 'graphs/gravity_sim_100.gif'

# Universal  Constants
G = 6.67408E-11 # m^3/kg/s^2
