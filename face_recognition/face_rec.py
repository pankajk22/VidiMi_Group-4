import os
from PIL import Image
import numpy as np
import pickle
import cv2

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

images_dir = os.path.join(BASE_DIR, "images")

face_cascade = cv2.CascadeClassifier('C:/Users/vs241/Desktop/face_rec/haarcascades/haarcascade_frontalface_alt2.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()

current_id = 0
labels_ids = {}
y_labels = []
x_train = []

for root, dirs, files in os.walk(images_dir):
    for fil in files:
        if fil.endswith("png") or fil.endswith("jpg") or fil.endswith("jpeg"):
            path = os.path.join(root, fil)
            label = os.path.basename(root).replace(" ","-").lower()

            if not label in labels_ids:
                labels_ids[label] = current_id
                current_id += 1
                
            id_ = labels_ids[label]
            pil_image = Image.open(path).convert("L")
            size = (550, 550)
            final_image = pil_image.resize(size, Image.ANTIALIAS)            
            image_arr = np.array(final_image, "uint8")

            faces = face_cascade.detectMultiScale(image_arr, scaleFactor=1.5, minNeighbors = 5)

            for (x,y,w,h) in faces:
                roi = image_arr[y:y+h, x:x+w]
                x_train.append(roi)
                y_labels.append(id_)


with open("labels.pickle", 'wb') as f:
    pickle.dump(labels_ids, f)

#training via recognizer
recognizer.train(x_train, np.array(y_labels))
recognizer.save("trainner.yml")
