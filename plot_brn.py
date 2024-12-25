import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.collections import PatchCollection
import matplotlib.patches as mpatches
import subprocess
import csv
import matplotlib.lines as mlines
import math
PdfFile='data_polygon\\brn.pdf'
CsvFile='data_polygon\\brn.csv'
ox=0
oy=0
n_sides=8
ndiscs=16
inc=(2*np.pi)/n_sides
theta=inc
a=1
b=0.1
gnd_via_radius=0.15
via_radius=0.1
patches=[]
plot_data=[]
for j in range(1, ndiscs+1):
    theta+=inc
    r=a*math.exp(b*theta)
    x = ox+r*np.cos(theta)
    y = oy+r*np.sin(theta)
    polygon=mpatches.RegularPolygon((x,y), n_sides, gnd_via_radius)
    patches.append(polygon)
    plot_data.append([x,y])
fig, ax=plt.subplots(figsize=(5, 5))
collection=PatchCollection(patches, cmap=matplotlib.cm.jet, alpha=1)
ax.add_collection(collection)
for patch in patches:
    ax.add_patch(patch)
origin_marker=mpatches.Circle((ox, oy), via_radius, color='red')
ax.add_patch(origin_marker)
ax.set_xlim([-10, 10])
ax.set_ylim([-10, 10])
ax.set_title('Bernuilli Spiral')
ax.set_xlabel('x coordinate [mm]', fontsize=11)
ax.set_ylabel('y coordinate [mm]', fontsize=11)
with open(CsvFile, 'w', newline='') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow(['x', 'y'])
    writer.writerows(plot_data)