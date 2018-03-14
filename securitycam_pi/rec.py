from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2
import time

def recStart():
    camera = PiCamera()
    camera.resolution = (800, 600)
    camera.framerate = 20
    rawCapture = PiRGBArray(camera, size=(800, 600))
    time.sleep(0.1)
    #ChaseSnortin
    fourcc = cv2.VideoWriter_fourcc('H','2','6','4')
    out = cv2.VideoWriter('DUMBASS_RECORDING.mp4', fourcc, 20.0, (800,600))
    
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        output = frame.array
        cv2.putText(output, 'Press q to quit', (0,360), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1)
        localtime = time.asctime(time.localtime(time.time()))
        cv2.putText(output, localtime, (0,50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1)
        cv2.imshow("Really Dumb Recording", output)
        out.write(output)
        key = cv2.waitKey(1) & 0xFF
        rawCapture.truncate(0)
        if key == ord("q"):
            break
    cv2.destroyAllWindows()
recStart()