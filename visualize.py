import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import config
import csv
import utils

# Use matplotlib ggplot stylesheet if available
try:
    plt.style.use('ggplot')
except:
    pass

def read_positions():
    x = []
    filename = config.data_folder + '/' + config.sim_name + '_x.csv'
    with open( filename, 'r', newline='\n') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        for row in csvreader:
            x.append(list(map(float, row)))

    y = []
    filename = config.data_folder + '/' + config.sim_name + '_y.csv'
    with open( filename, 'r', newline='\n') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        for row in csvreader:
            y.append(list(map(float, row)))

    return x, y
    
def read_areas():
    sizes = []

    filename = config.data_folder + '/' + config.sim_name + '_areas.csv'
    with open( filename, 'r', newline='\n') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        for row in csvreader:
            sizes.append(list(map(float, row)))

    return sizes


def plotter():
    # Set up the figure and axis
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set(xlim=(-1, 2), ylim=(-1, 2) ) #, xticks=([]), yticks=([]))
    # scat = utils.circles(x[0], y[0], s=sizes, edgecolors='none', animated=True) # size is the radius of the circle
    # ax.add_collection(scat)
    scat = ax.scatter(x[0], y[0], s=sizes)
    def animate(i):
        scat.set_offsets(np.c_[x[i], y[i]])

    anim = FuncAnimation(fig, animate, interval=10, frames=num_steps, repeat=True)
    filename = config.animation_folder + '/' + config.sim_name + '.gif'
    anim.save(filename, writer='pillow')

      
if __name__ == '__main__':
    x, y = read_positions()
    sizes = read_areas()
    print('Finished Reading Data')
    
    if len(x) != len(y):
        print('Error: x and y are different lengths')
        
    num_steps = len(x)

    plotter()
    print('Visualization Saved | ./{}'.format(config.animation_folder))
