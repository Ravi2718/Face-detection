# Face Recognition Attendance System

The Face Recognition  is a Python-based application that uses facial recognition to automate the process of taking attendance. By capturing video from a webcam, the system identifies and logs the presence of individuals based on pre-loaded images. This system is ideal for environments like classrooms or offices where quick and efficient attendance tracking is required.

## Features

- **Real-Time Face Recognition:** Uses a webcam to recognize faces in real-time.
- **Automatic Attendance Logging:** Records the names and timestamps of recognized individuals in a CSV file.
- **Daily Records:** Creates a new attendance log for each day, automatically naming the file with the current date.

## Prerequisites

Ensure you have Python 3.x installed, along with the following libraries:

- `face_recognition`
- `opencv-python`
- `numpy`

You can install the necessary libraries using pip:

```bash
pip install face_recognition opencv-python numpy
```

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/face-recognition-attendance.git
   cd face-recognition-attendance
   ```

2. **Add Images:**

   - Place the images of individuals to be recognized in the `photos` directory.
   - Ensure the images are named appropriately (e.g., `jobs_image.jpg` and `tesla.jpg`).

3. **Download Pre-trained Model (if required):**

   - Download the `shape_predictor_68_face_landmarks.dat` file from [Dlib's model repository](http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2) and place it in the project directory if you plan to use dlib for face recognition.

## Usage

1. **Run the Script:**

   ```bash
   python attendance_system.py
   ```

2. **Operation:**

   - The script will open your webcam and start detecting faces.
   - When a known face is detected, it will log the person's name and the time in a CSV file named after the current date.
   - The program continues to run until you press the 'q' key.

3. **Exiting:**

   - Press 'q' to stop the video feed and close the application.

## File Structure

```plaintext
face-recognition-attendance/
│
├── photos/                     # Directory containing images of individuals
│   ├── jobs.jpg
│   └── tesla.jpg
│
├── attendance_system.py         # Main script for the attendance system
├── README.md                    # This README file
└── 2023-08-20.csv               # Example of generated attendance file (date varies)
```

## How It Works

1. **Face Encoding:** The script loads images of individuals and computes facial encodings.
2. **Video Processing:** Captures live video, detects faces, and compares them to the known encodings.
3. **Attendance Logging:** If a face is recognized, it logs the name and time in a CSV file.

## Troubleshooting

- **Face Not Detected:** Ensure the images used are clear and well-lit. The webcam feed should also have good lighting.
- **CSV File Not Created:** Check for errors in the file path or permissions issues.



