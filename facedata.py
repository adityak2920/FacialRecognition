import numpy as np
import cv2
cap=cv2.VideoCapture(0)
face_cascade=cv2.CascadeClassifier('/anaconda3/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml')
skip=0
face_data=[]
dataset_path='/Users/adityakumar/Desktop/Face Recognition/'
file_name=input("Enter the name of the person: ")
def draw_border(img, pt1, pt2, color, thickness, r, d):
    x1,y1 = pt1
    x2,y2 = pt2

    # Top left
    cv2.line(img, (x1 + r, y1), (x1 + r + d, y1), color, thickness)
    cv2.line(img, (x1, y1 + r), (x1, y1 + r + d), color, thickness)
    cv2.ellipse(img, (x1 + r, y1 + r), (r, r), 180, 0, 90, color, thickness)

    # Top right
    cv2.line(img, (x2 - r, y1), (x2 - r - d, y1), color, thickness)
    cv2.line(img, (x2, y1 + r), (x2, y1 + r + d), color, thickness)
    cv2.ellipse(img, (x2 - r, y1 + r), (r, r), 270, 0, 90, color, thickness)

    # Bottom left
    cv2.line(img, (x1 + r, y2), (x1 + r + d, y2), color, thickness)
    cv2.line(img, (x1, y2 - r), (x1, y2 - r - d), color, thickness)
    cv2.ellipse(img, (x1 + r, y2 - r), (r, r), 90, 0, 90, color, thickness)

    # Bottom right
    cv2.line(img, (x2 - r, y2), (x2 - r - d, y2), color, thickness)
    cv2.line(img, (x2, y2 - r), (x2, y2 - r - d), color, thickness)
    cv2.ellipse(img, (x2 - r, y2 - r), (r, r), 0, 0, 90, color, thickness)
while True:
    ret, frame=cap.read()
    if ret==False:
        continue
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.3, 5)#what do these argument mean?
    k=1
    faces=sorted(faces, key=lambda x:x[2]*x[3],reverse=True)
    skip+=1
    for face in faces[:1]:
        x, y, w, h=face
        offset=7
        face_section=frame[y-offset:y+h+offset, x-offset:x+w+offset]
        face_section=cv2.resize(face_section, (100,100))
        if skip%10==0:#capturing every 10th face
            face_data.append(face_section)
            print(len(face_data))
        cv2.imshow(str(k), face_section)#my face section no. is not updating
        k+=1
        draw_border(frame, (x, y), (x+w,y+h), (0,0, 255), 2, 20, 30)
    cv2.imshow("Faces", frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break 

face_data=np.asarray(face_data)
face_data=face_data.reshape((face_data.shape[0], -1))
print(face_data.shape)
np.save(dataset_path+file_name, face_data)
print("Dataset saved at: {}".format(dataset_path+file_name+'.npy'))


cv2.destroyAllWindows()       
