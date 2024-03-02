import cv2

face_ref = cv2.CascadeClassifier("face_ref.xml")
camera = cv2.VideoCapture(0)

def face_detection():
    faces = face_ref.detectMultiScale(frame,scaleFactor=1.1)
    pass

def drawer_box():
    for x,y,w,h in face_detection(frame):
        cv2.rectangle(frame,(x,y), (x+w,y+h),(0,0,255),4)
        
    pass

def main():
    _,frame = camera.read()
    pass

if __name__ == "__main__":
    main()