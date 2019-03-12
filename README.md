# Facial_Recognition
FacialRecognition using webcam

A docker image for directly run in browser :- [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/adityak2920/Facial_Recognition/master)

Functions of different files:
   1. facedata.py - for collecting data from laptop's web cam.
   2. faceipwebcam.py - for collectin data from phone's camera(using an app called ipwebcam)
   3. recogn.py - for recognition of faces using laptop's web cam(we can also use phone's camera training by making some 
                   changes in the code like in faceipwebcam.py), here i have used KNN for training.
   4. .npy - theses are the files containg data of images captured using facedata.py and faceipwebcam.py(here i have only 
             captured 13 images of per person)
             
Link for demo:-  [Video](https://drive.google.com/open?id=1So876Leh-Q9adzxb9-ZEe-Qvk7xjYHwq)
