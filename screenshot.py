import cv2
import mediapipe as mp
import time

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
last_screenshot_time = 0  

def take_screenshot():
    """Take a screenshot and save it with a timestamp."""
    global last_screenshot_time
    if time.time() - last_screenshot_time > 1:  
        last_screenshot_time = time.time()
        screenshot = cap.read()[1]
        cv2.imwrite(f'screenshot_{int(time.time())}.png', screenshot)
        print("Screenshot taken!")

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
        if (landmark_list[5][2] < landmark_list[9][2] and
            landmark_list[5][2] < landmark_list[13][2] and
            landmark_list[5][2] < landmark_list[17][2]):
            take_screenshot()

    cv2.imshow("Palm Screenshot Capture", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
