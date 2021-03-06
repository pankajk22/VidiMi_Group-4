import cv2
from imutils import paths
import os
import face_recognition
import pickle
import dlib
from zipfile import ZipFile 
import sys

fileNames = sys.argv[1]
userId = sys.argv[2]

# Hint: To compress file without hidden mac files zip -r -X Archive.zip *
print('Extracting files')

# specifying the zip file name 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_name = os.path.join(BASE_DIR, "images/" + fileNames + ".zip")

# opening the zip file in READ mode 
with ZipFile(file_name, 'r') as zip: 
	# extracting all the files 
	print('Extracting all the files now...') 
	zip.extractall('python/images/' + fileNames + '/' + userId) 
	print('Done!') 

# deleting zip file
os.remove(file_name)

print("Accessing database")

# specifying the images directory
images_dir = os.path.join(BASE_DIR, "images/" + fileNames)

count = 0
known_names = []
known_encodings = []

# Walking through the images directory
for root, dirs, files in os.walk(images_dir):
    for fil in files:
        print("count: ", count)
        count += 1
        # Cheking for the extentions of the open file
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

# setting .pickle file location
pickle_dir = os.path.join(BASE_DIR, "database/" + userId.replace(" ","-").lower() + "_labels.pickle")
f = open(pickle_dir, 'wb')
f.write(pickle.dumps(data))

# deleting the images folder
images_folder_dir = os.path.join(BASE_DIR, "images/" + fileNames)
import shutil
shutil.rmtree(images_folder_dir)

f.close()