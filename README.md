# Hand Landmarker - MediaPipe

Real-time hand detection and tracking system using MediaPipe and OpenCV.

## Description

This project implements a real-time hand detector that uses Google's MediaPipe technology to identify and track up to 4 hands simultaneously through the webcam. The system draws the landmarks and connections between them, showing additional information such as FPS and the type of hand detected (left/right).

## Features

- ✋ Detection of up to 4 hands simultaneously
- 🎯 21 landmarks per hand
- 🔄 Real-time processing with LIVE_STREAM mode
- 📊 Real-time FPS visualization
- 🎨 Drawing of landmarks and connections between joints
- 👆 Left/right hand identification with confidence level
- ⚙️ Customizable camera and detector configuration

## Requirements

- Python 3.8+
- Webcam

## Installation

1. Clone or download this repository

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Make sure you have the model file `hand_landmarker.task` in the project root directory

## Usage

Run the main program:

```bash
python main.py
```

### Controls

- **Q** or **ESC**: Exit the program

## Project Structure

```
mediapipeHandLandmarker/
│
├── main.py              # Main program entry point
├── settings.py          # Camera and detector configuration
├── drawer.py            # Landmark drawing functions
├── common.py            # Shared global variables
├── hand_landmarker.task # MediaPipe model (required)
├── requirements.txt     # Project dependencies
└── README.md           # This file
```

## Configuration

### Camera Configuration (`CameraConfig` in [settings.py](settings.py))

```python
WIDTH = 680         # Resolution width
HEIGHT = 460         # Resolution height
FPS = 30              # Frames per second
```

### Detector Configuration (`HandDetectorConfig` in [settings.py](settings.py))

```python
NUM_HANDS = 4                        # Maximum number of hands to detect
MIN_DETECTION_CONFIDENCE = 0.5       # Minimum confidence for detection
MIN_PRESENCE_CONFIDENCE = 0.5        # Minimum presence confidence
MIN_TRACKING_CONFIDENCE = 0.5        # Minimum confidence for tracking
```

## Main Components

### main.py
- Initializes the camera and MediaPipe detector
- Manages the main capture and processing loop
- Handles asynchronous detection mode (LIVE_STREAM)

### drawer.py
- Draws the 21 landmarks of each detected hand
- Connects landmarks according to hand anatomy
- Displays FPS information and number of hands detected
- Labels each hand as left/right with its confidence level

### settings.py
- Centralizes all project configurations
- Defines camera and detector parameters
- Imports necessary classes from MediaPipe

### common.py
- Global variables for sharing detection results
- Manages state between asynchronous callbacks

## Main Dependencies

- **mediapipe** (0.10.31): ML framework for hand detection
- **opencv-python** (4.12.0.88): Image and video processing
- **numpy** (2.2.6): Numerical operations

## Hand Landmarks

The system detects 21 reference points per hand:

- **0**: Wrist
- **1-4**: Thumb
- **5-8**: Index
- **9-12**: Middle
- **13-16**: Ring
- **17-20**: Pinky

## Technical Notes

- The system operates in **LIVE_STREAM** mode for asynchronous processing
- Uses callbacks to handle detection results without blocking the flow
- Timestamps are handled in milliseconds for synchronization
- Detection works best with good lighting and contrasting background

## Troubleshooting

### Camera doesn't start
- Verify that your webcam is connected and not being used by another application
- Try changing the camera index in `cv2.VideoCapture(0)` to `1` or `2`

### Low performance (low FPS)
- Reduce resolution in `CameraConfig`
- Decrease `NUM_HANDS` if you don't need to detect so many hands
- Close other resource-consuming applications

### Hands not detected
- Adjust confidence values in `HandDetectorConfig`
- Make sure you have good lighting
- Keep hands within the camera's field of view

## License

This project uses Google's MediaPipe, which is under the Apache 2.0 license.

## Author

Developed with MediaPipe and OpenCV

## Contributions

Contributions are welcome. Please open an issue or pull request for suggestions or improvements.
