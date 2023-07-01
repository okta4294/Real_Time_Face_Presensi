import cv2
import pickle
import os
import numpy as np
import pandas as pd
from datetime import datetime

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

# Membaca file Excel ke dalam DataFrame (jika file sudah ada)
if os.path.exists('data_pengenalan_wajah.xlsx'):
    df = pd.read_excel('data_pengenalan_wajah.xlsx')
else:
    df = pd.DataFrame(columns=['No', 'Nama', 'Waktu'])

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

        if confidence < 80:
            text = person_names[label - 1]
        else:
            text = "Unknown"

        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

        # Memeriksa apakah data sudah ada dalam DataFrame
        existing_data = df[df['Nama'] == person_names[label - 1]]
        if existing_data.empty:
            # Data belum ada, tambahkan ke DataFrame
            data = {'No': [len(df) + 1], 'Nama': [person_names[label - 1]], 'Waktu': [datetime.now()]}
            new_data = pd.DataFrame(data)
            df = df._append(new_data, ignore_index=True)
            # Menyimpan DataFrame ke file Excel
            df.to_excel('data_pengenalan_wajah.xlsx', index=False, engine='openpyxl')

    cv2.imshow('Pengenalan Wajah', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
