# Augmented Reality Face Detection

## Project Overview

This project implements a face detection and landmark annotation system using MediaPipe's FaceMesh technology. The system processes video files to detect multiple human faces simultaneously, annotating facial landmarks in real-time. Performance metrics are displayed as an FPS (Frames Per Second) overlay on the processed video.

## Features

- Multiple face detection (up to 5 faces simultaneously)
- Facial landmark annotation using MediaPipe FaceMesh
- Real-time FPS display
- Video processing and saving capabilities
- Support for various human faces across different age groups

## System Requirements

- Python 3.7 or higher
- Conda environment management system
- Webcam (for live capture, if needed)
- Sufficient processing power for real-time video analysis

## Installation Instructions

### Step 1: Clone the Repository

```bash
git clone [repository-url]
cd [repository-name]
```

### Step 2: Create and Activate Conda Environment

```bash
conda create -n augmented_reality python=3.8
conda activate augmented_reality
```

### Step 3: Install Required Dependencies

```bash
conda install -c conda-forge opencv
pip install mediapipe
```

## Usage Guide

### Preparing Your Input Video

1. Place your input video file in an accessible directory
2. Note the full path to this file

### Configuring the Script

Open `capture.py` in your preferred text editor and modify the following variables:

```python
input_video_path = "PATH/TO/YOUR/INPUT/VIDEO.mov"  # Change to your input video path
output_video_path = "PATH/TO/YOUR/OUTPUT/VIDEO.mp4"  # Change to desired output location
```

### Running the Face Detection

With your conda environment activated, run:

```bash
python capture.py
```

The script will:
1. Load your input video
2. Process each frame to detect and annotate facial landmarks
3. Display the processed video in real-time with FPS information
4. Save the annotated video to your specified output path

### Controlling the Process

- Press the ESC key to stop the processing early
- The output video will be saved automatically upon completion

## Technical Details

### How the Face Detection Works

The system utilizes MediaPipe's FaceMesh solution to detect and annotate facial landmarks:

1. **Video Frame Acquisition**: Each frame is extracted from the input video
2. **Color Space Conversion**: Frames are converted from BGR to RGB color space for MediaPipe processing
3. **Face Detection and Landmark Extraction**: The FaceMesh model identifies facial regions and extracts landmark points
4. **Landmark Annotation**: Detected landmarks are visualized on the original frame
5. **Performance Monitoring**: FPS calculation provides real-time performance feedback

```python
# Pseudocode for the core face detection process
while video_is_playing:
    current_frame = get_next_frame()
    
    if frame_exists:
        calculate_and_display_fps()
        
        rgb_frame = convert_to_rgb(current_frame)
        face_detection_results = face_mesh.process(rgb_frame)
        
        if faces_detected:
            for each_face in detected_faces:
                draw_facial_landmarks(current_frame, face_landmarks)
        
        save_frame_to_output_video(current_frame)
        display_frame()
```

### Key Parameters

- `max_num_faces=5`: Configures the system to detect up to 5 faces simultaneously
- `refine_landmarks=False`: Optimizes for multiple face detection
- `min_detection_confidence=0.5`: Sets the threshold for face detection
- `min_tracking_confidence=0.5`: Sets the threshold for landmark tracking

## Performance and Limitations

As noted in the lab report:

- **Human Faces**: The system performs well on human faces across different age groups, though there may be slight variations in landmark precision for very young children or elderly subjects.
- **Cartoon Faces**: The current implementation has limited effectiveness with stylized or exaggerated cartoon faces, as the underlying model is primarily trained on human facial data.

## Future Improvements

Potential enhancements to the system could include:

- Retraining or fine-tuning the model with cartoon imagery for improved detection of stylized faces
- Implementing additional facial analysis features (e.g., emotion detection, age estimation)
- Optimizing performance for higher frame rates on resource-constrained devices

## Troubleshooting

### Common Issues and Solutions

- **Error opening video file**: Ensure the input file path is correct and the file exists
- **Low FPS**: Consider reducing video resolution or closing other resource-intensive applications
- **No faces detected**: Check lighting conditions and ensure faces are clearly visible in the frame

## Credits

- Student: Archit Biswas (ID: 24361821)
- MediaPipe by Google
- OpenCV Library
