import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import config
import csv

# Use matplotlib ggplot stylesheet if available
try:
    plt.style.use('ggplot')
except:
    pass

def read_positions():
    positions = []
    with open( config.filename, 'r', newline='\n') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        for row in csvreader:
            positions.append(list(map(float, row)))
    return positions

def plotter():
    # Set up the figure and axis
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set(xlim=(-1, 2), ylim=(-1, 2), xticks=([]), yticks=([]))
    scat = ax.scatter(x[0], y[0])

    def animate(i):
        scat.set_offsets(np.c_[x[i], y[i]])

    anim = FuncAnimation(fig, animate, interval=10, frames=num_steps, repeat=True)
    anim.save(config.animation_name, writer='pillow')

      
if __name__ == '__main__':
    positions = read_positions()
    print('Finished Reading Data')

    x = positions[::2*config.skip]
    y = positions[1::2*config.skip]
    
    if len(x) != len(y):
        print('Error: x and y are different lengths')
        
    num_steps = len(x)

    plotter()
    print('Visualization Saved | ./{}'.format(config.animation_name))
