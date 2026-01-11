"""Drawing module for visualizing hand landmarks and connections.

This module handles the visualization of detected hand landmarks, connections
between joints, FPS counter, and hand labels (left/right) on the video frame.
"""

from settings import *
from settings import CameraConfig as cam
from common import detection_result, detection_timestamp

# Variables for FPS calculation
last_time = time.time()
fps = 0

# Hand skeleton connections: tuples of (start_landmark_idx, end_landmark_idx)
# Defines which landmarks should be connected to form the hand structure
HAND_CONNECTIONS = frozenset([
    # Thumb
    (0,1), (1,2), (2,3), (3,4),
    
    # Index
    (0,5), (5,6), (6,7), (7,8),
    
    # Middle
    (0,9), (9,10), (10,11), (11,12),
    
    # Ring
    (0,13), (13,14), (14,15), (15,16),
    
    # Pinky
    (0,17), (17,18), (18,19), (19,20) 
])


def draw_landmarks_on_image(image, detection_result):
    """Draw hand landmarks, connections, and information overlays on the image.
    
    Args:
        image: numpy array representing the video frame (BGR format)
        detection_result: HandLandmarkerResult containing detected hand landmarks
    
    Returns:
        numpy array: The image with drawn landmarks and information overlays
    
    Features:
        - Draws 21 landmarks per hand as colored circles
        - Connects landmarks according to hand anatomy
        - Displays FPS counter
        - Shows number of detected hands
        - Labels each hand as Left/Right with confidence score
    """
    global last_time, fps
    
    # Calculate FPS
    current_time = time.time()
    fps = 1 / (current_time - last_time) if (current_time - last_time) > 0 else 0
    last_time = current_time
    
    num_hands = 0 if (detection_result is None or not detection_result.hand_landmarks) else len(detection_result.hand_landmarks)
    
    # Mostrar FPS y manos detectadas
    cv2.putText(image, f"FPS: {int(fps)}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
    
    cv2.putText(image, f"Hands detected: {num_hands}", (10, 70),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    # If no hands detected, return image with counter
    if detection_result is None or not detection_result.hand_landmarks:
        return image
    
    height, width, _ = image.shape
    
    for hand_idx, hand_landmarks in enumerate(detection_result.hand_landmarks):
        handedness = detection_result.handedness[hand_idx][0]
        hand_label = handedness.category_name
        hand_score = handedness.score
        
        for connection in HAND_CONNECTIONS:
            start_idx, end_idx = connection
            
            start_landmark = hand_landmarks[start_idx]
            end_landmark = hand_landmarks[end_idx]
            
            start_point = (int(start_landmark.x * width), int(start_landmark.y * height))
            end_point = (int(end_landmark.x * width), int(end_landmark.y * height))
            
            cv2.line(image, start_point, end_point, (0, 255, 0), 2)
            
        for landmark in hand_landmarks:
            x = int(landmark.x * width)
            y = int(landmark.y * height)
            
            cv2.circle(image, (x, y), 5, (255, 0, 0), -1)
            cv2.circle(image, (x, y), 6, (0, 255, 255), 2)
            
        label_text = f"{hand_label}: {hand_score:.2f}"
        wrist = hand_landmarks[0]
        wrist_pos = (int(wrist.x * width), int(wrist.y * height) - 20)
        
        cv2.putText(image, label_text, wrist_pos, 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    return image
