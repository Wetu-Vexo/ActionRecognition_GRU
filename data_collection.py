import cv2


camera = "rtsp://pangocv:pango@2023@192.168.8.26/stream1"

cap = cv2.VideoCapture(camera)

# Define the codec and create a video writer object
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Or a suitable codec of your choice
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))  # Adjust resolution if needed

# Loop until you hit 'q' to quit
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Check if the frame was successfully captured
    if not ret:
        print("Can't receive frame. Exiting...")
        break

    # Write the frame to the video file
    out.write(frame)

    # Display the resulting frame 
    cv2.imshow('Webcam Recording', frame)

    # Exit on pressing 'q'  
    if cv2.waitKey(1) == ord('q'):
        break

# Release resources
cap.release()
out.release()
cv2.destroyAllWindows()
