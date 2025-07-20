import cv2
from matplotlib import pyplot as plt

# Load a sample image from OpenCV, for demonstration since we don't have image upload functionality here.
image = cv2.imread(cv2.samples.findFile('anh-sex-0622-28182316-006.jpg'))

# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Invert the grayscale image
inverted_image = 255 - gray_image

# Apply Gaussian Blur
blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)

# Invert the blurred image
inverted_blurred = 255 - blurred

# Create the sketch by dividing the grayscale image by the inverted blurred image
sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)

# Plot original and sketch images using matplotlib
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Original Image")
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(sketch, cmap='gray')
plt.title("Sketch Image")
plt.axis('off')

plt.show()