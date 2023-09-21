import gpsd
import cv2


def main():
    # Open the default camera (usually the first camera connected)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not access the camera.")
        return

    try:
        while True:
            # Read a frame from the camera
            ret, frame = cap.read()

            if not ret:
                print("Error: Could not read a frame from the camera.")
                break








            # Display the frame
            cv2.imshow("Camera", frame)

            # Press 'q' to exit the loop and close the window
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    finally:
        # Release the camera and close the OpenCV window
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()


def main():
    # Connect to the local GPSD service (usually on localhost:2947)
    gpsd.connect()

    try:
        # Loop to continuously receive GPS data
        while True:
            # Get the latest GPS data
            packet = gpsd.get_current()
            
            # Check if the GPS data is valid
            if packet.mode >= 2:
                print("Latitude: {0:.6f}, Longitude: {1:.6f}".format(packet.lat, packet.lon))
                print("Speed (m/s):", packet.hspeed)
                print("Altitude (m):", packet.alt)
            else:
                print("No GPS fix")

    except KeyboardInterrupt:
        print("GPS data retrieval stopped by user.")

if __name__ == "__main__":
    main()


