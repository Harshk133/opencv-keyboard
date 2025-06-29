# import cv2
# import mediapipe as mp
# import pyautogui

# # MediaPipe hand detection setup
# mp_hands = mp.solutions.hands
# hands = mp_hands.Hands(max_num_hands=1)
# mp_draw = mp.solutions.drawing_utils

# # Webcam setup
# cap = cv2.VideoCapture(0)

# # Manually update these coordinates based on your paper layout
# # Use printed coordinates from console to map exact positions
# keyboard_keys = {
#     'A': (165, 178),
#     'B': (170, 141),
#     'C': (293, 233),
#     'D': (252, 191),
#     'E': (215, 140),
#     'F': (294, 190),
#     'G': (340, 198),
#     'H': (381, 194),
#     'I': (421, 169),
#     'J': (417, 200),
#     'K': (447, 198),
#     'L': (472, 205),
#     'M': (439, 238),
#     'N': (412, 234),
#     'O': (152, 171),
#     'P': (485, 170),
#     'Q': (126, 127),
#     'R': (252, 151),
#     'S': (210, 185),
#     'T': (301, 153),
#     'U': (385, 167),
#     'V': (336, 232),
#     'W': (166, 138),
#     'X': (249, 222),
#     'Y': (349, 152),
#     'Z': (203, 330),
# }

# pressed_key = None

# while True:
#     success, img = cap.read()
#     img = cv2.flip(img, 1)  # mirror image
#     img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#     results = hands.process(img_rgb)

#     if results.multi_hand_landmarks:
#         for hand_landmarks in results.multi_hand_landmarks:
#             # Index finger tip = landmark 8
#             finger_tip = hand_landmarks.landmark[8]
#             h, w, _ = img.shape
#             x = int(finger_tip.x * w)
#             y = int(finger_tip.y * h)

#             # Draw circle and coordinates
#             cv2.circle(img, (x, y), 10, (255, 0, 255), cv2.FILLED)
#             cv2.putText(img, f"{x},{y}", (x+10, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0,255), 2)

#             # Draw keyboard zones
#             for key, (kx, ky) in keyboard_keys.items():
#                 cv2.rectangle(img, (kx-30, ky-30), (kx+30, ky+30), (255, 255, 255), 2)
#                 cv2.putText(img, key, (kx-10, ky+10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

#                                 # Detect if finger is within a key zone
#                 if abs(x - kx) < 30 and abs(y - ky) < 30:
#                     # 🔴 Changed color from green to bold red (thicker box)
#                     cv2.rectangle(img, (kx-30, ky-30), (kx+30, ky+30), (0, 0, 255), 3)
#                     if pressed_key != key:
#                         print("Key Pressed:", key)
#                         pyautogui.write(key)
#                         pressed_key = key
#                     break

#             else:
#                 pressed_key = None

#             mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

#     cv2.imshow("Paper Keyboard", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()



# import cv2
# import mediapipe as mp
# import pyautogui

# # MediaPipe hand detection setup
# mp_hands = mp.solutions.hands
# hands = mp_hands.Hands(max_num_hands=1)
# mp_draw = mp.solutions.drawing_utils

# # Webcam setup
# cap = cv2.VideoCapture(0)

# # Coordinates based on your paper layout
# keyboard_keys = {
#     'A': (165, 178),
#     'B': (170, 141),
#     'C': (293, 233),
#     'D': (252, 191),
#     'E': (215, 140),
#     'F': (294, 190),
#     'G': (340, 198),
#     'H': (381, 194),
#     'I': (421, 169),
#     'J': (417, 200),
#     'K': (447, 198),
#     'L': (472, 205),
#     'M': (439, 238),
#     'N': (412, 234),
#     'O': (152, 171),
#     'P': (485, 170),
#     'Q': (126, 127),
#     'R': (252, 151),
#     'S': (210, 185),
#     'T': (301, 153),
#     'U': (385, 167),
#     'V': (336, 232),
#     'W': (166, 138),
#     'X': (249, 222),
#     'Y': (349, 152),
#     'Z': (203, 330),
# }

# pressed_key = None

# while True:
#     success, img = cap.read()
#     img = cv2.flip(img, 1)  # Mirror image
#     img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#     results = hands.process(img_rgb)

#     if results.multi_hand_landmarks:
#         for hand_landmarks in results.multi_hand_landmarks:
#             # Index finger tip = landmark 8, DIP joint = landmark 7
#             finger_tip = hand_landmarks.landmark[8]
#             finger_dip = hand_landmarks.landmark[7]

#             h, w, _ = img.shape
#             x_tip = int(finger_tip.x * w)
#             y_tip = int(finger_tip.y * h)
#             x_dip = int(finger_dip.x * w)
#             y_dip = int(finger_dip.y * h)

#             # Distance between fingertip and its DIP joint
#             dist = ((x_tip - x_dip) ** 2 + (y_tip - y_dip) ** 2) ** 0.5

#             # Draw finger tip circle and coordinates
#             cv2.circle(img, (x_tip, y_tip), 10, (255, 0, 255), cv2.FILLED)
#             cv2.putText(img, f"{x_tip},{y_tip}", (x_tip + 10, y_tip),
#                         cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

#             # Only check key presses if finger is extended
#             if dist > 15:  # Finger is straight (extended)
#                 for key, (kx, ky) in keyboard_keys.items():
#                     cv2.rectangle(img, (kx - 30, ky - 30), (kx + 30, ky + 30), (255, 255, 255), 2)
#                     cv2.putText(img, key, (kx - 10, ky + 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

#                     # Detect finger hover in key zone
#                     if abs(x_tip - kx) < 30 and abs(y_tip - ky) < 30:
#                         cv2.rectangle(img, (kx - 30, ky - 30), (kx + 30, ky + 30), (0, 0, 255), 3)
#                         if pressed_key != key:
#                             print("Key Pressed:", key)
#                             pyautogui.write(key)
#                             pressed_key = key
#                         break
#                 else:
#                     pressed_key = None
#             else:
#                 pressed_key = None

#             # Draw hand landmarks
#             mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

#     # Show frame
#     cv2.imshow("Paper Keyboard", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Cleanup
# cap.release()
# cv2.destroyAllWindows()



import cv2
import mediapipe as mp
import pyautogui
import time

# MediaPipe setup
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

# Webcam setup
cap = cv2.VideoCapture(0)

# Coordinates based on your paper layout
keyboard_keys = {
    'A': (165, 178),
    'B': (170, 141),
    'C': (293, 233),
    'D': (252, 191),
    'E': (215, 140),
    'F': (294, 190),
    'G': (340, 198),
    'H': (381, 194),
    'I': (421, 169),
    'J': (417, 200),
    'K': (447, 198),
    'L': (472, 205),
    'M': (439, 238),
    'N': (412, 234),
    'O': (152, 171),
    'P': (485, 170),
    'Q': (126, 127),
    'R': (252, 151),
    'S': (210, 185),
    'T': (301, 153),
    'U': (385, 167),
    'V': (336, 232),
    'W': (166, 138),
    'X': (249, 222),
    'Y': (349, 152),
    'Z': (203, 330),
}

hover_start_time = 0
hover_key = None
pressed_key = None
HOVER_DURATION = 0.3  # 300 milliseconds

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            finger_tip = hand_landmarks.landmark[8]
            finger_dip = hand_landmarks.landmark[7]

            h, w, _ = img.shape
            x_tip = int(finger_tip.x * w)
            y_tip = int(finger_tip.y * h)
            x_dip = int(finger_dip.x * w)
            y_dip = int(finger_dip.y * h)

            dist = ((x_tip - x_dip) ** 2 + (y_tip - y_dip) ** 2) ** 0.5

            if dist > 15:  # finger extended
                current_hover = None
                for key, (kx, ky) in keyboard_keys.items():
                    if abs(x_tip - kx) < 30 and abs(y_tip - ky) < 30:
                        current_hover = key
                        break

                if current_hover:
                    if current_hover == hover_key:
                        if time.time() - hover_start_time > HOVER_DURATION and pressed_key != current_hover:
                            pyautogui.write(current_hover)
                            pressed_key = current_hover
                    else:
                        hover_key = current_hover
                        hover_start_time = time.time()
                        pressed_key = None
                else:
                    hover_key = None
                    pressed_key = None
            else:
                hover_key = None
                pressed_key = None

    cv2.imshow("Paper Keyboard", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


