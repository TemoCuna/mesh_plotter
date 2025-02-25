#!/usr/bin/env python
# coding: utf-8

# ## Tecplot Mesh Plotter

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

#get_ipython().run_line_magic('matplotlib', 'widget')

# node_data = np.genfromtxt("inv_wing_tec_boundary.dat",usecols=(0,1,2),max_rows=432,skip_header=3)
node_data = np.genfromtxt("inv_wing_tec_boundary.dat",usecols=(0,1,2),max_rows=216,skip_header=1160)

node_xdata=node_data[:,0]
node_ydata=node_data[:,1]
node_zdata=node_data[:,2]

# connectivity_data = np.genfromtxt("inv_wing_tec_boundary.dat",usecols=(0,1,2),skip_header=435,max_rows=724)
connectivity_data = np.genfromtxt("inv_wing_tec_boundary.dat",usecols=(0,1,2),skip_header=1376,max_rows=312)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

count =0
for x, y, z in node_data:

    count=count
    ax.scatter(x, y, z)
    ax.text(x, y, z, str(count), zdir='z') # zdir can be 'x', 'y' or a tuple
    count=count+1

ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')

plt.show()













# In[ ]:





# In[ ]:




