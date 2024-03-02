import cv2

face_ref = cv2.CascadeClassifier("face_ref.xml")
camera = cv2.VideoCapture(0)

def face_detection():
    optimized_frame = cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
    faces = face_ref.detectMultiScale(optimized_frame,scaleFactor=1.1)
    return faces

def drawer_box():
    for x,y,w,h in face_detection(frame):
        cv2.rectangle(frame,(x,y), (x+w,y+h),(0,0,255),4)
    
def close_window():
    camera.release()
    cv2.destroyAllWindows()
    exit()

def main():
    while True:
        _,frame = camera.read()
        drawer_box(frame)
        cv2.imshow("Facereg",frame)
        
        if cv2.waitkey(1) & 0xFF == ord('q'):
            break
    

if __name__ == "__main__":
    main()