import cv2
import time
import mediapipe as mp

# Paths to input and output video files.
input_video_path = "P:/TCD/AR/Lab6/Scripts/videos/input-video-cartoon.mp4"   # Change as needed
output_video_path = "P:/TCD/AR/Lab6/Scripts/videos/annotated_output_cartoon.mp4"  # Output video file

# Prepare video capture from file.
cap = cv2.VideoCapture(input_video_path)
if not cap.isOpened():
    print("Error opening video file")
    exit()

# Get properties from the input video for VideoWriter.
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps_input = cap.get(cv2.CAP_PROP_FPS)
# Define the codec and create VideoWriter object.
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Alternatively, use 'XVID' for avi format.
out = cv2.VideoWriter(output_video_path, fourcc, fps_input, (frame_width, frame_height))

# Setup MediaPipe Face Mesh.
mp_drawing = mp.solutions.drawing_utils
mp_face_mesh = mp.solutions.face_mesh
drawingSpec = mp_drawing.DrawingSpec(color=(255, 255, 255), thickness=1, circle_radius=1)

face_mesh = mp_face_mesh.FaceMesh(
    max_num_faces=5,              # Supports multiple faces
    refine_landmarks=False,       # Set to False for multiple faces
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

previousTime = 0

while cap.isOpened():
    success, image = cap.read()
    if not success:
        break

    # Calculate FPS.
    currentTime = time.time()
    fps = 1 / (currentTime - previousTime) if previousTime != 0 else 0
    previousTime = currentTime
    cv2.putText(image, f"{int(fps)} FPS", (10, 70), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)

    # Convert the image to RGB before processing.
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb_image)

    # If faces are detected, draw the landmarks for each face.
    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            mp_drawing.draw_landmarks(
                image=image,
                landmark_list=face_landmarks,
                connections=mp_face_mesh.FACEMESH_TESSELATION,
                landmark_drawing_spec=drawingSpec,
                connection_drawing_spec=drawingSpec
            )

    # Write the annotated frame to the output video file.
    out.write(image)

    # Optionally display the annotated frame.
    cv2.imshow('Annotated Video', image)
    if cv2.waitKey(1) & 0xFF == 27:  # Exit on ESC key.
        break

# Clean up.
cap.release()
out.release()
cv2.destroyAllWindows()