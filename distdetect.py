import cv2
import numpy as np

# Function to calculate distance between two points in real-world coordinates
def calculate_distance(point1, point2):
    # Assuming known physical size of an object or a reference object
    known_size = 10.0  # Size of the object in the same unit as real-world coordinates (e.g., centimeters)
    
    # Euclidean distance formula
    distance = np.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)
    
    # Calculate real-world distance
    real_distance = (known_size * focal_length) / (2 * object_size)
    
    return real_distance

# Open a video capture stream from the camera (0 represents the default camera)
cap = cv2.VideoCapture(0)

# Define the known size of the object in the same unit as real-world coordinates
known_size = 10.0  # e.g., in centimeters

# Define the focal length of the camera (you need to calibrate your camera for accurate results)
focal_length = 1000.0  # Focal length in pixels

while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    if not ret:
        break

    # Convert the frame to grayscale for processing
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply a threshold or other processing to isolate objects if needed
    # ...

    # Find contours in the processed image
    contours, _ = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Iterate over detected contours and calculate distances
    for contour in contours:
        # Get the bounding box of the contour
        x, y, w, h = cv2.boundingRect(contour)
        
        # Assuming object size is the width of the bounding box
        object_size = w

        # Calculate the distance between objects
        distance = calculate_distance((x, y), (x + w, y + h))

        # Draw the distance on the frame
        cv2.putText(frame, f'Distance: {distance:.2f} cm', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    # Display the frame with distances
    cv2.imshow('Distance Measurement', frame)

    # Exit when the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
