import cv2
import mediapipe as mp
import numpy as np
import platform
import subprocess

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    model_complexity=1,
    min_detection_confidence=0.75,
    min_tracking_confidence=0.75,
    max_num_hands=1
)

draw_utils = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

is_light_mode = True

def toggle_windows_mode(light_mode):
    mode = 1 if light_mode else 0
    subprocess.run(f'reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Themes\\Personalize /v AppsUseLightTheme /t REG_DWORD /d {mode} /f', shell=True)


while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    result = hands.process(frame_rgb)

    landmark_list = []
    
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            for id, lm in enumerate(hand_landmarks.landmark):
                h, w, c = frame.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                landmark_list.append((id, cx, cy))
            
            draw_utils.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    if landmark_list:
        thumb_tip_x, thumb_tip_y = landmark_list[4][1], landmark_list[4][2]
        index_tip_x, index_tip_y = landmark_list[8][1], landmark_list[8][2]

        if thumb_tip_y < index_tip_y:  
            if not is_light_mode:
                is_light_mode = True
                if platform.system() == "Windows":
                    toggle_windows_mode(is_light_mode)
        else:  
            if is_light_mode:
                is_light_mode = False
                if platform.system() == "Windows":
                    toggle_windows_mode(is_light_mode)
                

    cv2.imshow("Screen Mode Switch", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
