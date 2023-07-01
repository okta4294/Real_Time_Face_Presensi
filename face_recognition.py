import cv2
import pickle
import os
import numpy as np

recognizer_path = './recognizer'
encodings_file = os.path.join(recognizer_path, 'encodings.pickle')

with open(encodings_file, 'rb') as f:
    data = pickle.load(f)
    face_encodings = data['encodings']
    labels = data['labels']
    person_names = data['person_names']

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.train(face_encodings, np.array(labels))

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        face_roi = gray[y:y + h, x:x + w]
        face_roi = cv2.resize(face_roi, (160, 160))
        label, confidence = recognizer.predict(face_roi)

        if confidence < 100:
            text = person_names[label - 1]
        else:
            text = "Unknown"

        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    cv2.imshow('Face Recognition', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
