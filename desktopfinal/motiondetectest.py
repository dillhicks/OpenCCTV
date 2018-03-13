import cv2
import time
import imutils as im
import smtplib
import threading
import time
from twilio.rest import Client
accountSID = 'AC9374b36a69cd65573445a6f312091953'
authToken = '6800e6926e7c96fad789d0384518dd08'
twilioNumber = '+19095514774'

global flag
flag = True
def sendStatus():
  global flag
  flag = True

def textm(message, number1):
  twilioCli = Client(accountSID, authToken)
  twilioCli.messages.create(body=message, from_=twilioNumber, to=number1)

def diffImg(t0, t1, t2):
  d1 = cv2.absdiff(t2, t1)
  d2 = cv2.absdiff(t1, t0)
  return cv2.bitwise_and(d1, d2)

def motionStart():  
  global flag
  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.starttls()
  SUBJECT = "OpenCCTV: Movement Detected!"
  TEXT = "You might want to check for intruders right about now!"
  msg = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)

  server.login("opencctv196", "pooppoop")
  minarea = 500
  camera = cv2.VideoCapture(0)
  
  winName = "Movement Indicator"
  cv2.namedWindow(winName, cv2.CV_WINDOW_AUTOSIZE)


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
  # Live feed of camera:
  live= camera.read()[1]

  #converting to grey
  t_minus = cv2.cvtColor(camera.read()[1], cv2.COLOR_RGB2GRAY)
  t = cv2.cvtColor(camera.read()[1], cv2.COLOR_RGB2GRAY)
  t_plus = cv2.cvtColor(camera.read()[1], cv2.COLOR_RGB2GRAY)

  #resizing to standard size
 
  fourcc = cv2.cv.CV_FOURCC('X','V','I','D')
  out = cv2.VideoWriter('intrudersmd.avi', fourcc, 20.0, (640,480))

  while True:
    diffImage = diffImg(t_minus, t, t_plus)
    currentFrame = t
    nextFrame = t_plus
    currentFrame = cv2.GaussianBlur(currentFrame, (21,21),0)
    nextFrame = cv2.GaussianBlur(currentFrame, (21,21), 0)
    cv2.putText(live, 'Press q to quit', (0,360), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1)
    localtime = time.asctime(time.localtime(time.time()))
    cv2.putText(live, localtime, (0,50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1)
    if cv2.countNonZero(diffImage) > 85000:
      text = "MOTION DETECTED"
      if flag == True:   
        if estatus == True:
          print("email working")
            #server.sendmail("opencctv196@gmail.com", email, msg)
          print("sent email")
        if pstatus == True:
          print("phone working") 
          #textm(SUBJECT + " " + TEXT, phone)
          print("sent text")
        flag = False
        status = threading.Timer(30, sendStatus)
        status.start()
      out.write(live)
    else:
      text = "NO MOTION DETECTED"
    cv2.putText(live, "{}".format(text), (0,20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1)
    cv2.imshow(winName, live)
    #cv2.imshow("frameDelta", frameDelta)
    # Read next image
    live = camera.read()[1]
    t_minus = t
    t = t_plus
    t_plus = cv2.cvtColor(camera.read()[1], cv2.COLOR_BGR2GRAY)
  
    #if q is pressed, end program
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break
      
  print "Goodbye"
  camera.release()
  cv2.destroyAllWindows()
  server.quit()
