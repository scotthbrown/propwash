# Import the necessary packages and modules
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import math
import matplotlib.cm as cm

# Prepare the data
C3 = 1.48
Pdb = 0.35
Pd = 3460.
x = np.arange(1,41,1.)
y = np.arange(-10,11,1)
Dp = 4.
Vo = C3*(((Pdb*Pd*1000)/(1029*Dp*Dp))**(0.333333333))
q = x/Dp
s = np.size(q)
b = np.arange(1,s+1,1.)


# Calculate Vo based on x/dp

for a in range(0, 10,):
	b[a] = Vo

for a in range(10,40,):
	b[a] = 2.6*Vo*(q[a])**(-1)

xs = np.size(x)
ys = np.size(y)

z = [[0 for col in range(xs)] for row in range(ys)]
za = np.array(z,dtype=float)

for xx in np.arange(1,41,1):
	for yy in np.arange (0,21,1):
	 	za[yy,xx-1] = b[xx-1]*math.exp((-22.2*y[yy]*y[yy])/(xx*xx)) 

import os
os.chdir ("C:/Users/G3ECHSHB/Desktop/PYthon")
np.savetxt('za.txt', za)



# Plot the data
plt.figure()
CS = plt.contourf(x,y,za)
plt.clabel(CS, inline=0, fontsize=12, colors = 'k')
plt.title('Velocities from Unducted Propeller, M/s')
plt.xlabel('Horizontal Distance From Propeller, M')
plt.ylabel('Vertical Distance From Propeller Centerline, M')

# Show the plot
plt.show()

