'''This script creates an image of a gaussian'''

import numpy as N
import matplotlib.pyplot as plt

# First we make the arrays

x = N.arange(-2,2,0.01)
y = N.exp(-x**2)

# We will display them one above another. The maximum for the first 3 is +-1

ax = plt.figure()
figure = ax.add_subplot(111)

figure.plot(x,y, label="Gaussian")

#remove axes
figure.xaxis.set_visible(False)
figure.yaxis.set_visible(False)
figure.set_ylim((0,1.05))

#tight makes the margins smaller
ax.savefig("GaussianForLecture2.pdf", bbox_inches='tight')

