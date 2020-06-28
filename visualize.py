import numpy as np
import matplotlib.pyplot as plt
import matplotlib.collections as clt
from matplotlib.animation import FuncAnimation
import config
import csv

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

    filename = config.data_folder + '/' + config.sim_name + '_radii.csv'
    with open( filename, 'r', newline='\n') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        for row in csvreader:
            sizes = (list(map(float, row)))

    return sizes


def plotter():
    # Set up the figure and axis
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set(xlim=(-10, 10), ylim=(-10, 10), xticks=([]), yticks=([]))

    patches = []
    for p in range(num_circles):
        circle = plt.Circle((x[0][p], y[0][p]),sizes[p])
        patches.append(circle)

    class UpdatablePatchCollection(clt.PatchCollection):
        def __init__(self, patches, *args, **kwargs):
            self.patches = patches
            clt.PatchCollection.__init__(self, patches, *args, **kwargs)

        def get_paths(self):
            self.set_paths(self.patches)
            return self._paths

    collection = UpdatablePatchCollection(patches, alpha=1.0)
    ax.add_collection(collection)

    def animate(frame):
        for p in range(num_circles):
            patches[p].center = x[frame][p], y[frame][p]

    anim = FuncAnimation(fig, animate, frames=num_steps, interval=1, blit=False,repeat=True)
    filename = config.animation_folder + '/' + config.sim_name + '.gif'
    anim.save(filename, writer='pillow')

      
if __name__ == '__main__':
    x, y = read_positions()
    # x = x[::2]
    # y = y[::2]
    sizes = read_areas()
    print('Finished Reading Data')
    
    if len(x) != len(y):
        print('Error: x and y are different lengths')
        
    num_steps = len(x)
    num_circles = len(x[0])

    plotter()
    print('Visualization Saved | ./{}'.format(config.animation_folder))
