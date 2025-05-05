import matplotlib.pyplot as plt

import numpy as np
from matplotlib import cm
from matplotlib.colors import Normalize
from mpl_toolkits.mplot3d import Axes3D

fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))
norm = Normalize(vmin=Z.min(), vmax=Z.max())
cmap = cm.viridis
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, facecolors=cmap(norm(Z)), linewidth=0, antialiased=False)
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
plt.title('3D Surface Plot with Custom Colormap')
plt.show()