import cv2
import imutils
import imutils.video as VideoStream
import pickle
import face_recognition
import time
import numpy as np
print("Load encodings")
data = pickle.loads(open("labels.pickle", 'rb').read())


print("Starting Video Stream.")
video = cv2.VideoCapture("input_video.mp4")
writer = None
time.sleep(2.0)



while (True):

    ret, sample_img = video.read()
    
    if not ret:
        break
    sample_img = cv2.rotate(sample_img, cv2.ROTATE_90_CLOCKWISE)
    rgb = cv2.cvtColor(sample_img, cv2.COLOR_BGR2RGB)
    rgb = imutils.resize(sample_img, width=750)
    r = sample_img.shape[1] / float(rgb.shape[1])

    #recognizing the face in the sample image
    box_info = face_recognition.face_locations(rgb, model = "hog")
    encodings = face_recognition.face_encodings(rgb, box_info)

    names = []

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

    if writer is None:
        fourcc = cv2.VideoWriter_fourcc(*"MJPG")
        writer = cv2.VideoWriter("Output_video.avi", fourcc, 30, (sample_img.shape[1], sample_img.shape[0]), True)

    if writer is not None:
        writer.write(sample_img)

    '''
    cv2.imshow("Image", sample_img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    '''
#cap.release()
video.release()
cv2.destroyAllWindows()