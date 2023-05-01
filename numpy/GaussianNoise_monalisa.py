import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image of the Mona Lisa
img = cv2.imread('mona_lisa.jpg', cv2.IMREAD_COLOR)

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Set the dimensions of the noise array
nrows, ncols = gray.shape

# Generate a 2D array of Gaussian noise with mean 0 and standard deviation 25
noise = np.random.normal(0, 25, (nrows, ncols))

# Blend the noise with the grayscale image
blended = cv2.addWeighted(gray.astype('float'), 0.5, noise, 0.5, 0)

# Plot the blended image
plt.imshow(blended, cmap='gray')
plt.axis('off')
plt.show()
