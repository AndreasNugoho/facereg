import cv2

face_ref = cv2.CascadeClassifier("face_ref.xml")
camera = cv2.VideoCapture(0)

def face_detection():
    pass

def drawer_box():
    pass

def main():
    _,frame = camera.read()
    pass

if __name__ == "__main__":
    main()