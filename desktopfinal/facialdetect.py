import face_recognition
import cv2
import threading
import time
import smtplib
from twilio.rest import Client
accountSID = 'AC9374b36a69cd65573445a6f312091953'
authToken = '6800e6926e7c96fad789d0384518dd08'
twilioNumber = '+19095514774'

global flag
flag = True
#timer for sending
#timer for pictures
def sendStatus():
  global flag
  flag = True
#send text function
def textm(message, number1):
  twilioCli = Client(accountSID, authToken)
  twilioCli.messages.create(body=message, from_=twilioNumber, to=number1)

#start camera
def facialStart():
    global flag
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    SUBJECT = "OpenCCTV: Movement Detected!"
    TEXT = "You might want to check for intruders right about now!"
    msg = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
    server.login("opencctv196", "pooppoop")
    

    #start camera
    video_capture = cv2.VideoCapture(0)

    #reading data from files
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
  
    #setting bool from file
    if(data[0] == 'true\n'):
      estatus = True
    else:
      estatus = False
    if(data[1] == 'true\n'):
      pstatus = True
    else:
      pstatus = False



  


    #loading pictures and training models  
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
    font = cv2.FONT_HERSHEY_DUPLEX
    #setting up video saving 
    fourcc = cv2.cv.CV_FOURCC('X','V','I','D')
    out = cv2.VideoWriter('intrudersfr.avi', fourcc, 20.0, (640,480))
    b = 0
    #starting facial recogntion
    process_this_frame = True
    while True:
        ret, frame = video_capture.read()
        #smaller frame for quicker computation time
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]
        #processing frame
        if process_this_frame:
            unknowns = 0
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
            face_names = []
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
        process_this_frame = not process_this_frame
        utext = "Unknowns:"
        ustring = str(unknowns)
        text = utext + ustring
        localtime = time.asctime(time.localtime(time.time()))
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4
            if name == "unknown":
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
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
                cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), -1)
                cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
                out.write(frame)
            else: 
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
                cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 255, 0), -1)
                cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
            currentx = (right + left)/2    
            currenty = (top + bottom) / 2
            print("x:" + str(currentx) + "y:" + str(currenty))
        
        cv2.putText(frame, text, (0,25), font, 0.5, (255,255,255), 1)
        cv2.putText(frame, localtime, (0,50), font, 0.5, (255,255,255), 1)
        cv2.putText(frame, 'Press q to quit', (0,460), font, 0.5, (255,255,255), 1)
        cv2.imshow('Video', frame)
        if cv2.waitKey(1) and 0xFF == ord('q'):
            break
       #print(framecount)
        
    #(utext + str(unknowns)) 
    # Release handle to the webcam
    out.release()
    video_capture.release()
    cv2.destroyAllWindows()

