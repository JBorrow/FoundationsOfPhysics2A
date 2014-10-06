'''This script creates an image of three waves and their superposition'''

import numpy as N
import matplotlib.pyplot as plt

# First we make the arrays

x = N.arange(0,10,0.01)
y1 = N.sin(2*x)
y2 = N.sin(1.22*x)
y3 = N.sin(x)

ySuper = y1 + y2 + y3

# We will display them one above another. The maximum for the first 3 is +-1

y1 += 10
y2 += 7
y3 += 4

ax = plt.figure()
figure = ax.add_subplot(111)

figure.plot(x,y1, label="Wave 1")
figure.plot(x,y2, label="Wave 2")
figure.plot(x,y3, label="Wave 3")
figure.plot(x,ySuper, label="Superposition")

legend = figure.legend(loc=2)
# Make transparent
legend.get_frame().set_alpha(0.5)

#remove axes
figure.xaxis.set_visible(False)
figure.yaxis.set_visible(False)

#tight makes the margins smaller
ax.savefig("WaveFunctionSuperpositionLecture1.pdf", bbox_inches='tight')

