#importing required libraries
import cv2
import imutils
import imutils.video as VideoStream
import pickle
import face_recognition
import time
import numpy as np

#Check if List_A is a subset of List_B
def check_list_subset(list_A, list_B):

    for name in list_A:
        if (name not in list_B):
            return True


#Putting box and name around all the detected faces in the frame
def put_box_around_face(box_info, names, sample_img):

    output_image2 = sample_img
    
    
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



#Save the frame when the person was detected first time in the input video
def detect_person(name, box_info, sample_img, names, time_of_frame):

    output_image = put_box_around_face(box_info, names, sample_img)
    
    #Output image file name will be the timelength at which it has occured first time in the video
    cv2.imwrite("output_frames/"+ time_of_frame+ ".png", output_image)




if __name__ == "__main__":
    

    #Opening the trained data file
    print("Load encodings")
    data = pickle.loads(open("labels.pickle", 'rb').read())

    #Opening the input video file
    print("Starting Video Stream.")
    video = cv2.VideoCapture("input_video2.mp4")
    writer = None
    time.sleep(2.0)

    #getting the frames per second or frame rate of the video
    fps = video.get(cv2.CAP_PROP_FPS)

    
    counter = 0
    detected_names = ['unknown']


    while (True):

        #getting the frame from the video
        ret, sample_img = video.read()
        
        if not ret:
            break
        
        #Selecting every 10th frame for analysis.
        counter += 1
        if(counter %10 == 0):

            #the timelength of the frame in the video    
            time_of_frame = str(float('%.4f'%(counter/fps)))

            sample_img = cv2.rotate(sample_img, cv2.ROTATE_90_CLOCKWISE)
            rgb = cv2.cvtColor(sample_img, cv2.COLOR_BGR2RGB)
            
            #recognizing the face in the sample image
            box_info = face_recognition.face_locations(rgb, model = "hog")
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

                #if one of the face in the frame is detected the first time.
                first_time = check_list_subset(names, detected_names)

                if(first_time):
                    detected_names.append(name)
                    
                    #saving the frame
                    detect_person(name, box_info, sample_img, names, time_of_frame)

            #Putting box around the detected face.
            sample_img = put_box_around_face(box_info, names, sample_img)

            #if video file is not yet traversed completely
            if writer is None:
                #appending frame to the output video file
                fourcc = cv2.VideoWriter_fourcc(*"MJPG")
                writer = cv2.VideoWriter("Output_video.avi", fourcc, 30, (sample_img.shape[1], sample_img.shape[0]), True)

            if writer is not None:
                writer.write(sample_img)
        
    
    #closing the video file
    video.release()
    
    cv2.destroyAllWindows()



