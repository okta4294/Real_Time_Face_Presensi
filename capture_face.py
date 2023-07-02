import cv2
import os


dataset_path = './dataset'
person_names_file = './dataset/person_names.txt'

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


def load_person_names():
    if not os.path.isfile(person_names_file):
        return []
    with open(person_names_file, 'r') as file:
        return file.read().splitlines()


def save_person_names(person_names):
    with open(person_names_file, 'w') as file:
        for name in person_names:
            file.write(name + '\n')


person_names = load_person_names()

name = input("Masukkan nama: ")
person_names.append(name)
save_person_names(person_names)

person_dir = os.path.join(dataset_path, name)
os.makedirs(person_dir, exist_ok=True)

cap = cv2.VideoCapture(0)
count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        face_roi = gray[y:y + h, x:x + w]
        image_path = os.path.join(person_dir, f'{name}_{count}.jpg')
        cv2.imwrite(image_path, face_roi)
        count += 1

    cv2.imshow('Menangkap Gambar', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
