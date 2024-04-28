import os
import cv2
import datetime
import numpy as np
from collections import deque
import threading
import requests

# Specify the paths to the cascade classifier files
gun_cascade = cv2.CascadeClassifier('cascade.xml')

# Initialize the webcam
camera = cv2.VideoCapture(0)  # Use webcam (index 0)

# Create a new folder for saving images if it doesn't exist
output_folder = 'gun_detection_images'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Define constants
GUN_DETECTION_THRESHOLD = 3  # Minimum consecutive frames to consider gun detected
FACE_DETECTION_THRESHOLD = 5  # Minimum consecutive frames to consider face detected
UPLOAD_URL = "https://example.com/upload"  # URL to upload images
SAVE_VIDEO = True  # Option to save video when gun is detected
VIDEO_DURATION = 10  # Duration of saved video in seconds

# Flags to track detections
gun_detected = False
face_detected = False

# Initialize deque to store recent detection states
gun_detection_history = deque(maxlen=GUN_DETECTION_THRESHOLD)
face_detection_history = deque(maxlen=FACE_DETECTION_THRESHOLD)

# Function to upload image to server
def upload_image(image_path):
    try:
        with open(image_path, 'rb') as f:
            files = {'image': f}
            response = requests.post(UPLOAD_URL, files=files)
            if response.status_code == 200:
                print("Image uploaded successfully!")
            else:
                print("Failed to upload image:", response.text)
    except Exception as e:
        print("Error uploading image:", e)

# Function to save video when gun is detected
def save_video(frames):
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(f"{output_folder}/gun_detected_{timestamp}.avi", fourcc, 20.0, (640, 480))
    for frame in frames:
        out.write(frame)
    out.release()
    print(f"Video saved as gun_detected_{timestamp}.avi")

# Function to process frame
def process_frame(frame):
    global gun_detected, face_detected

    # Convert the frame to grayscale for detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame using deep learning-based method
    # Replace this with your preferred face detection method
    # face_rects = face_detection_function(frame)
    # For demonstration, we'll just use Haar cascade for simplicity
    face_rects = []

    # Detect guns in the grayscale frame
    guns = gun_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(50, 50))

    # Check if guns and faces are detected
    if len(guns) > 0:
        gun_detected = True
        gun_detection_history.append(True)
        for (gx, gy, gw, gh) in guns:
            # Save the frame as an image if gun is detected
            timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
            filename = f"{output_folder}/gun_{timestamp}.jpg"
            cv2.imwrite(filename, frame)
            print(f"Gun detected! Image saved as {filename}")

            # Draw rectangles around detected guns
            cv2.rectangle(frame, (gx, gy), (gx + gw, gy + gh), (0, 255, 0), 2)

        # Save video when gun is detected
        if SAVE_VIDEO:
            threading.Thread(target=save_video, args=(frames,)).start()

    # If no guns detected, reset gun detection history
    else:
        gun_detection_history.append(False)

    # Update face detection history
    face_detected = len(face_rects) > 0
    face_detection_history.append(face_detected)

    # Check if gun and face detected for consecutive frames
    if sum(gun_detection_history) == GUN_DETECTION_THRESHOLD and sum(face_detection_history) == FACE_DETECTION_THRESHOLD:
        print("Both gun and face detected")
    elif sum(gun_detection_history) == GUN_DETECTION_THRESHOLD:
        print("Only gun detected")
    elif sum(face_detection_history) == FACE_DETECTION_THRESHOLD:
        print("Only face detected")
    else:
        print("Neither gun nor face detected")

    # Display the frame
    cv2.imshow("Security Feed", frame)

    # Check for user input to quit the application
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        camera.release()
        cv2.destroyAllWindows()

# Function to read frames from the camera
def capture_frames():
    frames = []
    while True:
        (grabbed, frame) = camera.read()
        if not grabbed or frame is None:
            break
        frames.append(frame)
        process_frame(frame)
        # Clear frames list after VIDEO_DURATION seconds
        if SAVE_VIDEO and len(frames) > 20 * VIDEO_DURATION:
            frames.clear()

# Start capturing frames in a separate thread
threading.Thread(target=capture_frames).start()
