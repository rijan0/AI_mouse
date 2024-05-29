import cv2
import mediapipe as mp
import pyautogui
mp_hands = mp.solutions.hands.Hands()
get = cv2.VideoCapture(0)
drawing_utils = mp.solutions.drawing_utils
screen_width, screen_height =  pyautogui.size()
chori_y = 0
chori_x = 0
while True:
    _,frame = get.read()
    frame = cv2.flip(frame,1)
    frame_height, frame_width, _ = frame.shape
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    output = mp_hands.process(frame)
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)
            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):
                x = int (landmark.x * frame_width )
                y = int (landmark.y * frame_height)
                if id == 8:
                    cv2.circle(img=frame, center=(x,y,), radius=10,color=(0, 255, 255))
                    chori_x = screen_width / frame_width *x
                    chori_y = screen_height / frame_height *y
                    pyautogui.moveTo(chori_x , chori_y)
                if id == 4:
                    cv2.circle(img=frame, center=(x,y,), radius=10,color=(0, 255, 255))
                    budi_x = screen_width / frame_width *x
                    budi_y = screen_height / frame_height *y
                    distance = ((budi_x - chori_x) ** 2 + (budi_y - chori_y) ** 2) ** 0.5
                    print(distance)
                    if distance < 50:  
                       print('clicked')
                       pyautogui.click()
    cv2.imshow('gesture', frame)
    cv2.waitKey(1)
