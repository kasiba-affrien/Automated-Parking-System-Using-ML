import cv2
import numpy as np

# Load the image containing the parking lot
image = cv2.imread('new/images/pklot4.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to reduce noise
blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

# Apply Canny edge detection
edges = cv2.Canny(blurred_image, 50, 150)

# Find contours in the edge-detected image
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Define a list to store parking space rectangles
parking_spaces = []

# Iterate through the contours and filter out potential parking spaces
for contour in contours:
    # Filter based on contour area (adjust the threshold as needed)
    if cv2.contourArea(contour) > 100:
        # Fit a rotated rectangle around the contour
        rect = cv2.minAreaRect(contour)
        box = cv2.boxPoints(rect)
        box = np.int0(box)

        # Calculate the width and height of the rectangle
        width = int(rect[1][0])
        height = int(rect[1][1])

        # Filter out rectangles that are approximately square (adjust the aspect ratio as needed)
        aspect_ratio = width / float(height)
        if 0.5 < aspect_ratio < 2.0:
            parking_spaces.append(box)

# Draw rectangles around the detected parking spaces
for space in parking_spaces:
    cv2.drawContours(image, [space], 0, (0, 255, 0), 2)

# Display the image with parking spaces highlighted
cv2.imshow('Parking Spaces', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

