import cv2
import imutils
import pickle
import face_recognition


print("Load encodings")
data = pickle.loads(open("labels.pickle", 'rb').read())

sample_img = cv2.imread("5.jpeg")
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
    stroke = 2
    cv2.rectangle(sample_img, (h,x), (y,w), color, stroke)
    color = (0, 255, 0)
    stroke = 1
    font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
    cv2.putText(sample_img, name, (h,x), font, 1, color, stroke, cv2.LINE_AA)


cv2.imshow("Image", sample_img)
    #if cv2.waitKey(20) & 0xFF == ord('q'):
    #    break

#cap.release()
cv2.waitKey(0)
cv2.destroyAllWindows()