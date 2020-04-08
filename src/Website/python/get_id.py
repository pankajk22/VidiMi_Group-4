import cv2
import imutils
import pickle
import face_recognition
import os
import sys

fileNames = sys.argv[1]

print("Load encodings")
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
pickle_dir = os.path.join(BASE_DIR, "add_to_db_labels.pickle")
data = pickle.loads(open(pickle_dir, 'rb').read())

test_img_dir = os.path.join(BASE_DIR, fileNames + ".jpg")
sample_img = cv2.imread(test_img_dir)
rgb = cv2.cvtColor(sample_img, cv2.COLOR_BGR2RGB)

box_info = face_recognition.face_locations(rgb, model = "hog")
encodings = face_recognition.face_encodings(rgb, box_info)


names = []

#cap = cv2.VideoCapture(0)
'''
while (True):

    ret, sample_img = cap.read()
    rgb = cv2.cvtColor(sample_img, cv2.COLOR_BGR2RGB)

    #recognizing the face in the sample image
    box_info = face_recognition.face_locations(rgb, model = "hog")
    encodings = face_recognition.face_encodings(rgb, box_info)
'''

for encoding in encodings:
    matches = face_recognition.compare_faces(data["encodings"], encoding, tolerance =0.37)
    name = "unknown"


    if True in matches:

        matchedIndx = [i for (i,b) in enumerate(matches) if b]
        count = {}


        for i in matchedIndx:
            name = data["names"][i]
            count[name] = count.get(name, 0) + 1

        name = max(count, key= count.get)
    
    names.append(name)

for ((x,y,w,h), name) in zip(box_info, names):
    color = (0,0,255)
    stroke = 5
    cv2.rectangle(sample_img, (h,x), (y,w), color, stroke)
    color = (0, 255, 0)
    stroke = 3
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(sample_img, name, (h,x), font, 2, color, stroke, cv2.LINE_AA)

result_img_dir = os.path.join(BASE_DIR, "../public/images/getId/" + fileNames + ".png")
print('Saving the result file at "/public/images/getId/' + fileNames + '.png"' )
cv2.imwrite(result_img_dir, sample_img)

# deleting test image
os.remove(test_img_dir)

#cap.release()
cv2.destroyAllWindows()