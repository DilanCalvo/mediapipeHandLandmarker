import cv2
import mediapipe as mp
import time

class BaseSettings:
    BaseOptions = mp.tasks.BaseOptions
    HandLandmarker = mp.tasks.vision.HandLandmarker
    HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
    HandLandmarkerResult = mp.tasks.vision.HandLandmarkerResult
    VisionRunningMode = mp.tasks.vision.RunningMode


class CameraConfig:
    WIDTH = 680
    HEIGHT = 480
    FPS = 30


class HandDetectorConfig:
    MODEL_PATH = "hand_landmarker.task"
    RUNNING_MODE = BaseSettings.VisionRunningMode.LIVE_STREAM
    NUM_HANDS = 4
    MIN_DETECTION_CONFIDENCE = 0.5
    MIN_PRESENCE_CONFIDENCE = 0.5
    MIN_TRACKING_CONFIDENCE = 0.5