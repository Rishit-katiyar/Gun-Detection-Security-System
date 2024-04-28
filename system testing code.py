import os
import cv2
import datetime
import numpy as np
import requests

# Specify the paths to the cascade classifier files
gun_cascade = cv2.CascadeClassifier('cascade.xml')

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

# Function to process image for detection
def process_image(image_path):
    # Read the image
    frame = cv2.imread(image_path)

    # Convert the frame to grayscale for detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect guns in the grayscale frame
    guns = gun_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(50, 50))

    # Check if guns are detected
    if len(guns) > 0:
        gun_detected = True
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
            save_video([frame])

    # Display the frame
    cv2.imshow("Detection Result", frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Function to save video when gun is detected
def save_video(frames):
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(f"{output_folder}/gun_detected_{timestamp}.avi", fourcc, 20.0, (640, 480))
    for frame in frames:
        out.write(frame)
    out.release()
    print(f"Video saved as gun_detected_{timestamp}.avi")

# Testing mode
def testing_mode():
    image_path = r"C:\Users\DELL\Documents\OpenCV\5b28052898acb_Shooting1.jpg"
    process_image(image_path)

# Run testing mode
testing_mode()
