import mediapipe as mp
import cv2
import time
import pyautogui
from loc import *

time.sleep(0.2)
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands
cap = cv2.VideoCapture(0)

with mp_hands.Hands(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5,max_num_hands=1) as hands:
    while cap.isOpened():
        success, image = cap.read()                                                                                                   
        h, w, c = image.shape
        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
        results=hands.process(image)
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(image,hand_landmarks,mp_hands.HAND_CONNECTIONS)
                loc = results.multi_hand_landmarks[0]
                x1=loc.landmark[INDEX_FINGER_TIP]
                x2=loc.landmark[INDEX_FINGER_DIP]
                x4=loc.landmark[MIDDLE_FINGER_TIP]
                x5=loc.landmark[MIDDLE_FINGER_DIP]
                x6=loc.landmark[RING_FINGER_TIP]
                x7=loc.landmark[RING_FINGER_DIP]
                x8=loc.landmark[PINKY_TIP]
                x9=loc.landmark[PINKY_DIP]
                if x1.x*w>w/2 and x1.y<x2.y:
                    pyautogui.keyDown('space')
                    # pyautogui.keyUp('left')
                elif x1.x*w<w/2 and x1.y<x2.y: 
                    if  pyautogui.keyDown('space')==True :
                    # pyautogui.keyDown('left')
                         pyautogui.keyDown('space')==False              

            cv2.imshow('MediaPipe Hands', image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()