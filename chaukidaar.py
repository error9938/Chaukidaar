import cv2
import time
import pygame
from ultralytics import YOLO

# Siren setup
SIREN_FILE = "siren.wav"   # <- yahi file apne chaukidar folder me rakho
pygame.mixer.init()
siren = pygame.mixer.Sound(SIREN_FILE)

# YOLO model load
model = YOLO("yolov8n.pt")

# Animal labels (jo YOLO detect karega)
ANIMAL_LABELS = ["elephant", "cow", "dog", "cat", "horse"]

# Camera start
cap = cv2.VideoCapture(0)

siren_playing = False  # siren state flag

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # YOLO detect
    results = model(frame)

    animal_detected = False

    for r in results:
        boxes = r.boxes
        for box in boxes:
            cls_id = int(box.cls[0])
            label = model.names[cls_id]

            # Agar label animal list me hai
            if label in ANIMAL_LABELS:
                animal_detected = True

                # rectangle + text draw
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
                cv2.putText(frame, label, (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

    # Siren control
    if animal_detected and not siren_playing:
        print("🔴 Animal detected → Siren ON")
        siren.play(-1)  # continuous bajega
        siren_playing = True
    elif not animal_detected and siren_playing:
        print("🟢 Animal gone → Siren OFF")
        siren.stop()
        siren_playing = False

    # Show window
    cv2.imshow("Chaukidaar (YOLOv8 + Siren)", frame)

    # Quit 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
siren.stop()
