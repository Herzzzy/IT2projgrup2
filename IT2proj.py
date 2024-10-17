import matplotlib.pylab as plt
import numpy as np
#testing...
xverdier = np.linspace(1,100,100)

yverdier = 0.5*xverdier**2
plt.subplot(2, 1, 1)
plt.plot(xverdier, yverdier)
plt.grid()

yverdier = -0.3*xverdier**3
plt.subplot(2,1,2)
plt.plot(xverdier, yverdier)
plt.grid()

plt.show()
