from ultralytics import YOLO
import cv2

# Charger le modèle YOLOv8
model = YOLO('yolov8n.pt')  # Remplacez par le chemin de votre fichier de poids YOLOv8 si différent

# Ouvrir le flux vidéo de la webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Erreur : Impossible d'ouvrir la webcam")
    exit()

while True:
    # Lire une frame
    ret, frame = cap.read()
    if not ret:
        print("Erreur : Impossible de lire la frame")
        break

    # Faire des prédictions sur la frame capturée
    results = model(frame)

    # Annoter la frame avec les résultats
    annotated_frame = results[0].plot()

    # Afficher la frame annotée
    cv2.imshow('Webcam', annotated_frame)

    # Quitter la boucle si l'utilisateur appuie sur 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libérer les ressources
cap.release()
cv2.destroyAllWindows()
