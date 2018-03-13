
# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
from twilio.rest import Client
import time
import cv2
import smtplib
import threading
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
# initialize the camera and grab a reference to the raw camera capture
def motionStart():
	global flag
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	SUBJECT = "OpenCCTV: Movement Detected!"
	TEXT = "You might want to check for intruders right about now!"
	msg = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
	server.login("opencctv196", "pooppoop")
	font = cv2.FONT_HERSHEY_SIMPLEX
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
	camera.resolution = (480, 360)
	camera.framerate = 20
	rawCapture = PiRGBArray(camera, size=(480, 360))


	# allow the camera to warmup
	time.sleep(0.1)

	fourcc = cv2.VideoWriter_fourcc('H','2','6','4')
	out = cv2.VideoWriter('intrudersmd.mp4', fourcc, 20.0, (480,360))


	camera.capture(rawCapture, format = "bgr")
	output = rawCapture.array
	output.setflags(write=True)
	t_minus = cv2.cvtColor(output, cv2.COLOR_BGR2GRAY)
	t = cv2.cvtColor(output, cv2.COLOR_BGR2GRAY)
	t_plus = cv2.cvtColor(output, cv2.COLOR_BGR2GRAY)

	rawCapture.truncate(0)
	 
	# capture frames from the camera
	for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
            # grab the raw NumPy array representing the image, then initialize the timestamp
            # and occupied/unoccupied text

            diffImage = diffImg(t_minus, t, t_plus)
            cv2.putText(output, 'Press q to quit', (0,360), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1)
            localtime = time.asctime(time.localtime(time.time()))
            cv2.putText(output, localtime, (0,50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1)
            
            if cv2.countNonZero(diffImage) > 60000:
                text = "MOTION DETECTED"
                if flag == True:
                    if (estatus == True):
                        print("email working")
                        server.sendmail("opencctv196@gmail.com", email, msg)
                        print("sent email")
                    if pstatus == True:
                        print("phone working") 
                        textm(SUBJECT + " " + TEXT, phone)
                        print("sent text")
                    flag = False
                    status = threading.Timer(30, sendStatus)
                    status.start()
                out.write(output)
            else:
                text = "NO MOTION DETECTED"
            cv2.putText(output, "{}".format(text), (0,20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1)
            # show the frame
            cv2.imshow("Movement Detection", output)

            output = frame.array
            output.setflags(write=True)
            t_minus = t
            t = t_plus
            t_plus = cv2.cvtColor(output, cv2.COLOR_BGR2GRAY)
            
            key = cv2.waitKey(1) & 0xFF
            # clear the stream in preparation for the next frame
            rawCapture.truncate(0)
            # if the `q` key was pressed, break from the loop
            if key == ord("q"):
                break
	server.quit()
	cv2.destroyAllWindows()
motionStart()