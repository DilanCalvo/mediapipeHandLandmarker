"""Configuration module for hand detector settings.

This module contains all configuration classes for camera settings,
hand detection parameters, and MediaPipe base settings.
"""

import cv2
import mediapipe as mp
import time

class BaseSettings:
    """Base settings and MediaPipe class references.
    
    Contains references to MediaPipe vision task classes for hand detection.
    """
    BaseOptions = mp.tasks.BaseOptions
    HandLandmarker = mp.tasks.vision.HandLandmarker
    HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
    HandLandmarkerResult = mp.tasks.vision.HandLandmarkerResult
    VisionRunningMode = mp.tasks.vision.RunningMode


class CameraConfig:
    """Camera configuration parameters.
    
    Attributes:
        WIDTH: Camera frame width in pixels
        HEIGHT: Camera frame height in pixels
        FPS: Target frames per second for video capture
    """
    WIDTH = 680
    HEIGHT = 480
    FPS = 30


class HandDetectorConfig:
    """Hand detector configuration parameters.
    
    Attributes:
        MODEL_PATH: Path to the MediaPipe hand landmark model file
        RUNNING_MODE: Detection mode (LIVE_STREAM for real-time processing)
        NUM_HANDS: Maximum number of hands to detect simultaneously
        MIN_DETECTION_CONFIDENCE: Minimum confidence for hand detection (0.0-1.0)
        MIN_PRESENCE_CONFIDENCE: Minimum confidence for hand presence (0.0-1.0)
        MIN_TRACKING_CONFIDENCE: Minimum confidence for hand tracking (0.0-1.0)
    """
    MODEL_PATH = "hand_landmarker.task"
    RUNNING_MODE = BaseSettings.VisionRunningMode.LIVE_STREAM
    NUM_HANDS = 4
    MIN_DETECTION_CONFIDENCE = 0.5
    MIN_PRESENCE_CONFIDENCE = 0.5
    MIN_TRACKING_CONFIDENCE = 0.5