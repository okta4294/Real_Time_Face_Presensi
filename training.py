import cv2
import os
import numpy as np
import pickle

dataset_path = './dataset'
recognizer_path = './recognizer'
encodings_file = os.path.join(recognizer_path, 'encodings.pickle')

if not os.path.exists(recognizer_path):
    os.makedirs(recognizer_path)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()

face_encodings = []
labels = []

person_names = []

for person_dir in os.listdir(dataset_path):
    person_name = person_dir
    person_names.append(person_name)
    person_path = os.path.join(dataset_path, person_dir)
    if not os.path.isdir(person_path):
        continue

    for image_file in os.listdir(person_path):
        image_path = os.path.join(person_path, image_file)
        image = cv2.imread(image_path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in faces:
            face_roi = gray[y:y + h, x:x + w]
            face_roi = cv2.resize(face_roi, (160, 160))
            face_encodings.append(face_roi)
            labels.append(person_names.index(person_name) + 1)

recognizer.train(face_encodings, np.array(labels))

with open(encodings_file, 'wb') as f:
    pickle.dump({'encodings': face_encodings, 'labels': labels, 'person_names': person_names}, f)