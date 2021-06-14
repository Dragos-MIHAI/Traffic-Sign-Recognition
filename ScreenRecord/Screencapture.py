####### Program used for Screen capturing and displaying it into a new window. Part of this program was use in the traffic sign detection.#################################################################

import numpy as np
import cv2
from mss import mss
from PIL import Image

mon = {'top': 160, 'left': 160, 'width': 200, 'height': 200}

sct = mss()

monitor_number = 2
mon = sct.monitors[monitor_number]

while 1:
   mss().grab(mon)
   screenshot = mss().grab(mon)
   img = Image.frombytes("RGB", (screenshot.width, screenshot.height), screenshot.rgb)
   img_np = np.array(img)
   frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
   cv2.imshow('test', frame)
   print(frame)

		##Option tried, not working, maybe somebody can find a solution
   
   #img_np2 = frame.ravel()
   #img_np2 = np.asscalar(img_np2)
   #vector = np.vectorize(np.float)
   #img_np2 = vector(frame)
   #img_np2 = np.array_split(img_np2,len(img_np2))
   #img_np2 = frame.iloc[0]
   #print()
   #vid_capture = cv2.VideoCapture(0)
   #print(vid_capture)
   

		##End Option tried#############################################


   if cv2.waitKey(25) & 0xFF == ord('q'):
      cv2.destroyAllWindows()
      break



	       ## Other Method but only takes a screenshot#####################

#from PIL import ImageGrab
#import numpy as np
#import cv2

#while 1:
#  img = ImageGrab.grab() #bbox specifies specific region (bbox= x,y,width,height *starts top-left)
#  img_np = np.array(img) #this is the array obtained from conversion
#  frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
#  cv2.imshow("test", frame)
#  cv2.waitKey(0)
#  cv2.destroyAllWindows()
#  break
