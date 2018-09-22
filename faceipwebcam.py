import urllib
import numpy as np
import cv2
import time
url = 'http://10.121.21.299:8080/shot.jpg'


#cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier('/Users/adityakumar/Desktop/ML/haarcascade/haarcascade_frontalface_default.xml')

skip = 0
face_data = []
dataset_path = '/Users/adityakumar/Desktop/ML/FaceRecognition/'

file_name = raw_input('Enter the name of the person: ')

while True:
    #ret, frame = cap.read()
    img_response = urllib.urlopen(url)
    img_numpy = np.array(bytearray(img_response.read()), dtype=np.uint8)
    frame = cv2.imdecode(img_numpy, -1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    k = 1
    face = sorted(faces, key=lambda x:x[2]*x[3], reverse = True)
    skip+=1
    for face in faces[:1]:
        x, y, w, h = face
        
        offset = 7
        face_section = frame[y-offset:y+offset+h, x-offset:x+w+offset]
        face_section = cv2.resize(face_section, (100, 100))
        if skip %10 ==0:
            face_data.append(face_section)
            print len(face_data)
        cv2.imshow(str(k), face_section)
        k+=1
        cv2.rectangle(frame, (x, y), (x+w, y+h),(0, 255, 0), 2)
    cv2.imshow('faces', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


face_data = np.asarray(face_data)
face_data = face_data.reshape((face_data.shape[0], -1))
print face_data.shape

# Save the dataset in filesystem
np.save(dataset_path + file_name, face_data)
#print "Dataset saved at: {}".format(dataset_path + file_name + '.npy')

cv2.destroyAllWindows()
