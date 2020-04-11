#importing required libraries
import cv2
import imutils
import pickle
import face_recognition

#Putting box and name around all the detected faces in the frame
def put_box_around_face(box_info, names, sample_img):

    output_image2 = sample_img
    
    #Putting box and name around all the detected faces in the frame
    for ((x,y,w,h), name) in zip(box_info, names):
        color = (0,0,255)
        stroke = 2
        
        #Setting rectangle around the detected face.
        output_image1 = cv2.rectangle(output_image2, (h,x), (y,w), color, stroke)
        color = (0, 255, 0)
        stroke = 1
        font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
        
        #Putting name of the detected person on top of the rectangle
        output_image2 =  cv2.putText(output_image1, name, (h,x), font, 1, color, stroke, cv2.LINE_AA)
        
    return output_image2




if __name__ == "__main__":
    
    #Opening the trained data file
    print("Load encodings")
    data = pickle.loads(open("labels.pickle", 'rb').read())

    #Opening the input image file
    sample_img = cv2.imread("input_image.jpg")
    rgb = cv2.cvtColor(sample_img, cv2.COLOR_BGR2RGB)

    #getting the location of the faces in video
    box_info = face_recognition.face_locations(rgb, model = "hog")
    
    #encoding the faces in the image
    encodings = face_recognition.face_encodings(rgb, box_info)

    #list of names of detected faces in the current frame
    names = []

    
    for encoding in encodings:

        #matching the faces-data from the database, having tolerance as 0.37
        matches = face_recognition.compare_faces(data["encodings"], encoding, tolerance =0.37)
        
        #initially assuming face is unknown
        name = "unknown"


        if True in matches:

            matchedIndx = [i for (i,b) in enumerate(matches) if b]
            count = {}


            for i in matchedIndx:
                name = data["names"][i]
                count[name] = count.get(name, 0) + 1

            name = max(count, key= count.get)
        
        names.append(name)

    #Putting box around the detected face.
    sample_img = put_box_around_face(box_info, names, sample_img)
    
    #saving the output image
    cv2.imwrite("Output_image.png", sample_img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()