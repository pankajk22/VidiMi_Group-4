#importing th erequired libraries
import cv2
from imutils import paths
import os
import face_recognition
import pickle
import dlib


if __name__ == "__main__":
    

    print("Accessing database")

    #Opening the image folder where all the photos to train data are stored
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    images_dir = os.path.join(BASE_DIR, "images")

    count = 0
    known_names = []
    known_encodings = []

    #Traversing through each person's folder to get images to train the data
    for root, dirs, files in os.walk(images_dir):
        for fil in files:
            #print("count: ", count)
            count += 1
            
            #Checking for the file extention. I.E. it is an image file
            if fil.endswith("png") or fil.endswith("jpg") or fil.endswith("jpeg"):
                #getting the path of the image
                path = os.path.join(root, fil)
                
                #getting the name of the person this photo belongs to
                label = os.path.basename(root).replace(" ","-").lower()
            #print(label)
            
            #Opening the image file
            img = cv2.imread(path)
            rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            #getting the location of the faces in video
            box_info = face_recognition.face_locations(rgb, model = "hog")

            #encoding the faces in the image
            encodings = face_recognition.face_encodings(rgb, box_info)
            
            #appending the encoding and name for the face in this image to the encodings' list and name list respectively 
            for encod in encodings:
                known_encodings.append(encod)
                known_names.append(label)


    #print("Serializing Encodings.")

    #Creating Dictionary for the encoding and their corresponding person name
    data = {"encodings": known_encodings, "names": known_names}
    
    #Writing the encodings data in the pickle file. This is the trained data
    f = open("labels.pickle", 'wb')
    f.write(pickle.dumps(data))
    f.close()