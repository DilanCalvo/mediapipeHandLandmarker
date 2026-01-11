from settings import *
from settings import BaseSettings as bs
from settings import CameraConfig as cam
from settings import HandDetectorConfig as hdc
from common import detection_result, detection_timestamp
from drawer import draw_landmarks_on_image

def process_result(result, output_image, timestamp_ms):
    
    global detection_result ,detection_timestamp
    detection_result = result
    detection_timestamp = timestamp_ms


def main():
    global detection_result
    
    print('Starting Camera...')
    cap = cv2.VideoCapture(0)
    
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, cam.WIDTH)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, cam.HEIGHT)
    cap.set(cv2.CAP_PROP_FPS, cam.FPS)
    
    if not cap.isOpened():
        print('Error with the camera')
        return
    
    print('Camera Ready')
    print("Press 'q' or Esc for exit")
    
    options = bs.HandLandmarkerOptions(
        base_options = bs.BaseOptions(
            model_asset_path = hdc.MODEL_PATH
        ),
        running_mode = hdc.RUNNING_MODE,
        num_hands = hdc.NUM_HANDS,
        min_hand_detection_confidence = hdc.MIN_DETECTION_CONFIDENCE,
        min_hand_presence_confidence = hdc.MIN_PRESENCE_CONFIDENCE,
        min_tracking_confidence = hdc.MIN_TRACKING_CONFIDENCE,
        result_callback = process_result
    )
    
    with bs.HandLandmarker.create_from_options(options) as landmarker:
        print("Hands Detector Initilisated")
        
        while cap.isOpened():
            ret, frame = cap.read()
            
            if not ret:
                print("Error")
                break
            
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            
            mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame_rgb)
            
            timestamp_ms = int(time.time() * 1000)
            
            landmarker.detect_async(mp_image, timestamp_ms)
            
            # Crear copia local para evitar race conditions
            current_result = detection_result
            if current_result:
                frame = draw_landmarks_on_image(frame, current_result)
                
            
            cv2.putText(frame, "Press 'q' or ESC to exit", (10, frame.shape[0] - 10),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)
            
            cv2.imshow('Hand Detector - MediaPipe', frame)
            
            key = cv2.waitKey(1) & 0xFF
            
            if key == ord('q') or key == 27:
                print("Exiting...")
                break
    

    cap.release()
    cv2.destroyAllWindows()
    print("Program finished")

if __name__ == "__main__":
    main()