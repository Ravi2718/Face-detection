#!/usr/bin/env python3
import face_recognition
import cv2
import numpy as np
import csv
import os
from datetime import datetime

# Start webcam capture
video_capture = cv2.VideoCapture(0)

# Load known images
jobs_image = face_recognition.load_image_file("photos/jobs.jpg")
jobs_encoding = face_recognition.face_encodings(jobs_image)[0]

tesla_image = face_recognition.load_image_file("photos/tesla.jpg")
tesla_encoding = face_recognition.face_encodings(tesla_image)[0]

# Store encodings and names
known_face_encodings = [
    jobs_encoding,
    tesla_encoding
]

known_face_names = [
    "Steve Jobs",
    "Nikola Tesla"
]

# Students list to mark attendance only once
students = known_face_names.copy()

# Get current date and time
now = datetime.now()
current_date = now.strftime("%Y-%m-%d")

# Create/open attendance CSV file
if not os.path.exists("attendance"):
    os.makedirs("attendance")
file_path = os.path.join("attendance", f"{current_date}.csv")
f = open(file_path, 'w+', newline='')
lnwriter = csv.writer(f)

print("Face recognition attendance system started. Press 'q' to quit.")

while True:
    ret, frame = video_capture.read()
    if not ret:
        print("Failed to grab frame.")
        break

    # Resize frame for faster processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = small_frame[:, :, ::-1]  # BGR to RGB

    # Find all face locations and encodings
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
    face_names = []

    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)

        if matches[best_match_index]:
            name = known_face_names[best_match_index]
            face_names.append(name)

            # Mark attendance if student not already marked
            if name in students:
                students.remove(name)
                current_time = now.strftime("%H:%M:%S")
                lnwriter.writerow([name, current_time])
                print(f"Marked present: {name} at {current_time}")

    # Display frame
    cv2.imshow("Attendance System", frame)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
video_capture.release()
cv2.destroyAllWindows()
f.close()
print("Attendance system closed.")
