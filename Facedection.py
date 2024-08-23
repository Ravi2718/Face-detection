import face_recognition
import cv2
import numpy as np
import csv
import os
from datetime import datetime

video_capture = cv2.VideoCapture(0)

jobs_image = face_recognition.load_image_file("photos/jobs_image")
jobs_encoding = face_recognition.face_encodings(jobs_image)[0]

tesla_image = face_recognition.load_image_file("photos/tesla.jpg")
tesla_encoding = face_recognition.face_encodings(tesla_image)[0]

Known_face_encoding = [
    jobs_encoding,
    tesla_encoding
]

known_face_names = [
    "jobs",
    "tesla"
]

students = known_face_names.copy()

face_location = []
face_encodings = []
face_name = []
s = True

now = datetime.now()
current_date = now.strftime("%Y-%m-%d")

f = open(current_date + '.csv', 'w+', newline='')
lnwriter = csv.writer(f)

while True:
    ret, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = small_frame[:, :, ::-1]

    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
    face_names = []
    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(Known_face_encoding, face_encoding)
        face_distance = face_recognition.face_distance(Known_face_encoding, face_encoding)
        best_match_index = np.argmin(face_distance)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]
            face_names.append(name)
            if name in students:
                students.remove(name)
                print(students)
                current_time = now.strftime("%H-%M-%S")
                lnwriter.writerow([name, current_time])

    cv2.imshow("attendance system", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
f.close()
