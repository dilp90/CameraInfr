#!/usr/bin/python
import time
import picamera
 
with picamera.PiCamera() as picx:
    picx.start_preview()
    time.sleep(50)
    picx.stop_preview()
    picx.close()
    