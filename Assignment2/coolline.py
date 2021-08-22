import numpy as np
import matplotlib.pyplot as plt

# evenly sampled time at 200ms intervals
x = np.arange(0., 10.0, 0.2)

# red dashes
import math
plt.plot(x,math.e**(2*x) + 10*x - 100*x**2,'g--')
plt.xlabel("My Inputs")
plt.ylabel("My Outputs")
plt.title("Best Graph")
plt.show()