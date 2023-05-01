import numpy as np
import matplotlib.pyplot as plt

# Set the dimensions and resolution of the plot
width, height = 1000, 1000
xmin, xmax = -2, 1
ymin, ymax = -1.5, 1.5
max_iter = 100
escape_radius = 2

# Create arrays to store the real and imaginary parts of the complex plane
x = np.linspace(xmin, xmax, width)
y = np.linspace(ymin, ymax, height)
X, Y = np.meshgrid(x, y)

# Create an array to store the number of iterations for each point in the complex plane
z = X + 1j*Y
c = z.copy()
iterations = np.zeros_like(z, dtype=int)

# Compute the Mandelbrot set
for n in range(max_iter):
    indices = np.abs(z) < escape_radius
    iterations[indices] = n
    z[indices] = z[indices]**2 + c[indices]

# Plot the Mandelbrot set
plt.imshow(iterations.T, cmap='inferno', extent=(xmin, xmax, ymin, ymax))
plt.xlabel('Real axis')
plt.ylabel('Imaginary axis')
plt.show()
