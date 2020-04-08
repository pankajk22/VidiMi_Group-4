import cv2
from imutils import paths
import os
import face_recognition
import pickle
import dlib

print("Accessing database")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
images_dir = os.path.join(BASE_DIR, "images")

count = 0
known_names = []
known_encodings = []

for root, dirs, files in os.walk(images_dir):
    for fil in files:
        print("count: ", count)
        count += 1
        if fil.endswith("png") or fil.endswith("jpg") or fil.endswith("jpeg"):
            path = os.path.join(root, fil)
            label = os.path.basename(root).replace(" ","-").lower()
            print(label)
            img = cv2.imread(path)
            rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            box_info = face_recognition.face_locations(rgb, model = "hog")

            encodings = face_recognition.face_encodings(rgb, box_info)
            
            for encod in encodings:
                known_encodings.append(encod)
                known_names.append(label)


print("Serializing Encodings.")

data = {"encodings": known_encodings, "names": known_names}
f = open("labels.pickle", 'wb')
f.write(pickle.dumps(data))
f.close()