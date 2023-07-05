import cv2 #library opencv buat kamera
import os #library buat ngatur file atau interaksi dengan sistem operasi

#path untuk folder dataset dan file person_names.txt
dataset_path = './dataset' 
person_names_file = './dataset/person_names.txt'

#load cascade classifier buat deteksi wajah
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

#fungsi buat load nama-nama orang yang sudah ada di file person_names.txt
def load_person_names():
    if not os.path.isfile(person_names_file):
        return []
    with open(person_names_file, 'r') as file:
        return file.read().splitlines()

#fungsi buat nulis nama-nama orang yang sudah ada di file person_names.txt
def save_person_names(person_names):
    with open(person_names_file, 'w') as file:
        for name in person_names:
            file.write(name + '\n')

#load nama-nama orang yang sudah ada di file person_names.txt
person_names = load_person_names()

#input nama orang yang mau ditambahkan ke dataset
name = input("Masukkan nama: ")
person_names.append(name)
save_person_names(person_names)

#buat folder dengan nama orang yang mau ditambahkan ke dataset
person_dir = os.path.join(dataset_path, name)
os.makedirs(person_dir, exist_ok=True)

#buka kamera
cap = cv2.VideoCapture(0)
count = 0

#looping buat menangkap gambar
while True:
    ret, frame = cap.read()
    if not ret:
        break
#deteksi wajah
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        face_roi = gray[y:y + h, x:x + w]
        image_path = os.path.join(person_dir, f'{name}_{count}.jpg')
        cv2.imwrite(image_path, face_roi)
        count += 1
#tampilin gambar
    cv2.imshow('Menangkap Gambar', frame)
#tekan q untuk keluar
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
#tutup kamera
cap.release()
cv2.destroyAllWindows()
