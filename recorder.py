import cv2
import numpy as np
import pyautogui
import time

# display screen resolution, get it using pyautogui itself
SCREEN_SIZE = tuple(pyautogui.size())
# define the video format
fourcc = cv2.VideoWriter_fourcc(*"XVID")
# frames per second
fps = 20.0
# creates a time stamp in year-month-day hour-minute-seconds format
time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
#formatting the time stamp to string and using it as a dynamic file name
file_name = f'{time_stamp}.mp4'

# create the video write object
out = cv2.VideoWriter(file_name, fourcc, fps, (SCREEN_SIZE))
# the time you want to record in seconds. Keep the number high if you want to record until q is pressed.
record_seconds = 100000

for i in range(int(record_seconds * fps)):
    # make a screenshot
    img = pyautogui.screenshot()
    # convert these pixels to a proper numpy array to work with OpenCV
    frame = np.array(img)
    # convert colors to the way they originally were
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # write the frame
    out.write(frame)
    # show the frame
    cv2.imshow("screenshot", frame)
    # if the user clicks q, it exits
    if cv2.waitKey(1) == ord("q"):
        break

# make sure everything is closed when exited
cv2.destroyAllWindows()
out.release()
