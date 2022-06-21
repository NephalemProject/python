import cv2 as cv
import datetime
import time
import pandas

capture = cv.VideoCapture(0)
face_cas = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_frontalface_default.xml")
body_cas = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_fullbody.xml")

detected = 0
detect_stop_time = None
timer_start = False
seconds_to_rec = 10

frame_size = (int(capture.get(3)), int(capture.get(4)))
fourcc = cv.VideoWriter_fourcc(*"mp4v")

first_frame = None
status_list = [None, None]
times = []
df = pandas.DataFrame(columns = ["Start", "End"])

def appendTime(listname):
    listname.append(datetime.now())

while True:
    _, frame = capture.read()

    gray =  cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = face_cas.detectMultiScale(gray, 1.3, 5)
    bodies = body_cas.detectMultiScale(gray, 1.3, 5)

    if len(faces) + len(bodies) > 0:
        if detected == 1:
            timer_start = False
        else:
            detected = 1
            cur_time = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
            output = cv.VideoWriter(f"{cur_time}.mp4", fourcc, 20, frame_size)
            print("Started Recording")
    elif detected == 1:
        if timer_start:
            print(time.time() - detect_stop_time)
            if time.time() - detect_stop_time >= seconds_to_rec:
                detected = 0
                timer_start = False
                output.release()
                print("Stopped Recording")
        else:
            timer_start = True
            detect_stop_time = time.time()

    if detected:
        output.write(frame)

    # for(x, y, w, h) in faces:
    #     cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

    status_list.append(detected)

    status_list = status_list[-2:]

    if status_list[-1] != None and status_list[-2] != status_list[-1]:
        appendTime(times)

    cv.imshow("Footage", frame)

    if cv.waitKey(1) == ord('q'):
        break

capture.release()
output.release()
cv.destroyAllWindows()
