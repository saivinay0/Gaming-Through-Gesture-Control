import cv2
from cvzone.HandTrackingModule import HandDetector
from pynput.keyboard import Controller

# Initialize webcam and hand detector
cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8)
keyboard = Controller()

# Define gesture regions and key mappings
up_region = [(50, 50), (200, 200)]  # Adjust coordinates based on your screen and hand position
down_region = [(250, 50), (400, 200)]  # Adjust coordinates based on your screen and hand position

# Main loop
while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)  # Mirror the image for better hand detection

    # Detect hands
    hands, img = detector.findHands(img)

    # Check for hands and process gestures
    if hands:
        hand = hands[0]
        lmList = hand["lmList"]  # Landmark list
        indexFingerX, indexFingerY = lmList[8]  # Index finger tip coordinates

        # Check if finger is within gesture regions
        is_up = False
        is_down = False
        if up_region[0][0] < indexFingerX < up_region[1][0] and up_region[0][1] < indexFingerY < up_region[1][1]:
            is_up = True
        if down_region[0][0] < indexFingerX < down_region[1][0] and down_region[0][1] < indexFingerY < down_region[1][1]:
            is_down = True

        # Simulate key presses based on gesture
        if is_up:
            keyboard.press('up')
        else:
            keyboard.release('up')
        if is_down:
            keyboard.press('down')
        else:
            keyboard.release('down')

    # Display image and gesture regions (optional)
    cv2.imshow("Image", img)

    # Exit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()