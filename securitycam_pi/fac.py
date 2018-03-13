from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import threading
import face_recognition
import smtplib

global flag
flag = True
def sendStatus():
  global flag
  flag = True

def textm(message, number1):
  twilioCli = Client(accountSID, authToken)
  twilioCli.messages.create(body=message, from_=twilioNumber, to=number1)


def facialStart():
    # initialize the camera and grab a reference to the raw camera capture
    global flag
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    SUBJECT = "OpenCCTV: Movement Detected!"
    TEXT = "You might want to check for intruders right about now!"
    msg = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
    server.login("opencctv196", "pooppoop")
    
    with open('main.config','r') as file:
        data = file.readlines()
    file.close()

    email = data[2]
    email = email[:-1]
    phone = data[3]
    phone = phone[:-1]
    print(email)
    print(phone)
    print(data)

    if(data[0] == 'true\n'):
        estatus = True
    else:
        estatus = False
    if(data[1] == 'true\n'):
        pstatus = True
    else:
        pstatus = False

    camera = PiCamera()
    camera.resolution = (240,180)
    camera.framerate = 20
    rawCapture = PiRGBArray(camera, size=(240, 180))
     
    # allow the camera to warmup
    time.sleep(0.1)
    

    fourcc = cv2.VideoWriter_fourcc('H','2','6','4')
    out = cv2.VideoWriter('intrudersfr.mp4', fourcc, 20.0, (240,180))
    font = cv2.FONT_HERSHEY_DUPLEX
    with open("modelnames.config", "r") as ins:
        names = []
        for line in ins:
            line = line[:-1]
            names.append(line)
        ins.close()
    with open("modellocations.config", 'r') as files:
        filelocations = []
        for line in files:
            line = line[:-1]
            filelocations.append(line)
        files.close()
    encodings = []
    for i in xrange(len(filelocations)):
        currentimage = face_recognition.load_image_file(filelocations[i])
        currentencoding = face_recognition.face_encodings(currentimage)[0]
        encodings.append(currentencoding)
        known_face_encodings = encodings
        known_face_names = names
        face_locations = []
        face_encodings = []
        face_names = []
    # capture frames from the camera
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
            # grab the raw NumPy array representing the image, then initialize the timestamp
        unknowns = 0
            # and occupied/unoccupied text
        output = frame.array
        output.setflags(write=True)
        print("Capturing image.")
        # Grab a single frame of video from the RPi camera as a numpy array


        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(output)
        print("Found {} faces in image.".format(len(face_locations)))
        face_encodings = face_recognition.face_encodings(output, face_locations)

        # Loop over each face found in the frame to see if it's someone we know.
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "unknown"
            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]
                    #detecting number of unknown subjects    
            if name == "unknown": 
                unknowns += 1
            face_names.append(name)
        text = "Unknowns: " + str(unknowns)
        localtime = time.asctime(time.localtime(time.time()))
        cv2.putText(output, text, (0,5), font, 0.5, (255,255,255), 1)
        cv2.putText(output, localtime, (0,25), font, 0.5, (255,255,255), 1)
        cv2.putText(output, "Press 'q' to quit", (0, 160), font, 0.5, (255,255,255), 1)
        if unknowns > 0:
            if flag == True:   
                if estatus == True:
                    print("email working")
                    server.sendmail("opencctv196@gmail.com", email, msg)
                    print("sent email")
                if pstatus == True:
                    print("phone working") 
                    textm(SUBJECT + " " + TEXT, phone)
                    print("sent text")
                flag = False
                status = threading.Timer(3, sendStatus)
                status.start()
        
            try:
                out.write()
            except:
                print("could not grab frame because of memory issues")
        cv2.imshow('Facial Recognition', output)
        key = cv2.waitKey(1) & 0xFF
     
            # clear the stream in preparation for the next frame
        rawCapture.truncate(0)
     
            # if the `q` key was pressed, break from the loop
        if key == ord("q"):
            break