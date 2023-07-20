import cv2


def unauthorised_person():
    # Connect to the camera device
    camera = cv2.VideoCapture(0)  # 0 represents the default camera index

    # Check if the camera connection is successful
    if not camera.isOpened():
        print("Failed to open camera")
        exit()

    # Capture a frame from the camera
    ret, frame = camera.read()

    # Check if the frame was read successfully
    if not ret:
        print("Failed to capture frame")
        exit()

    # Store the captured frame in a variable
    captured_frame = frame

    # Display the captured frame
    cv2.imshow("Captured Frame", captured_frame)
    cv2.waitKey(3000)
    cv2.destroyAllWindows()

    # Release the camera
    camera.release()

    # Now you can use the 'captured_frame' variable for further processing
    # For example, you can save it to a file using cv2.imwrite
    cv2.imwrite("captured_frame.jpg", captured_frame)
    
