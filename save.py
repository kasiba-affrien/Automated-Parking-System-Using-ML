import cv2

# Open the camera (0 represents the default camera; change it if you have multiple cameras)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open camera.")
else:
    while True:
        # Read a frame from the camera
        ret, frame = cap.read()

        if not ret:
            print("Error: Could not read a frame.")
            break

        # Display the frame in a window
        cv2.imshow('Camera', frame)

        # Press 's' to save the image
        if cv2.waitKey(1) & 0xFF == ord('s'):
            # Save the image with a unique filename (you can customize the filename)
            image_filename = 'new_car.jpg'
            cv2.imwrite(image_filename, frame)
            print(f"Image saved as {image_filename}")
            break

        # Press 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close the OpenCV window
    cap.release()
    cv2.destroyAllWindows()
