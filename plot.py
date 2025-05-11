import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0,2*np.pi,100)
y_sinx=np.sin(x)
y_cosx=np.cos(x)
plt.plot(x,y_sinx,label="sinx",linestyle="solid")
plt.plot(x,y_cosx,label="cosx",linestyle="dashed")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Sin and cos x functions")
plt.legend()
plt.grid()
plt.show()
