#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 14:12:09 2024

@author: upes
"""

import face_recognition
import cv2
import numpy as np

from gtts import gTTS
from playsound import playsound
import time


# The text that you want to convert to audio
#mytext = 'Welcome to the IoT Lab!'
welcomeMsg = 'Have a nice day Ahead!'

# Language in which you want to convert
language = 'en'

TIME_CUTOFF = 30 # in seconds

# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed

# This is a super simple (but slow) example of running face recognition on live video from your webcam.
# There's a second example that's a little more complicated but runs faster.

# PLEASE NOTE: This example requires OpenCV (the `cv2` library) to be installed only to read from your webcam.
# OpenCV is *not* required to use the face_recognition library. It's only required if you want to run this
# specific demo. If you have trouble installing it, try any of the other demos that don't require it instead.

# Get a reference to webcam #0 (the default one)
video_capture = cv2.VideoCapture(0)

# Load a sample picture and learn how to recognize it.
Bhupendra_image = face_recognition.load_image_file("./face_images/Bhupendra.png")
Bhupendra_face_encoding = face_recognition.face_encodings(Bhupendra_image)[0]

# Load a second sample picture and learn how to recognize it.
biden_image = face_recognition.load_image_file("./face_images/biden.jpg")
biden_face_encoding = face_recognition.face_encodings(biden_image)[0]

# Load a second sample picture and learn how to recognize it.
utsav_image = face_recognition.load_image_file("./face_images/Utsav.jpeg")
utsav_face_encoding = face_recognition.face_encodings(utsav_image)[0]

# Load a second sample picture and learn how to recognize it.
Ajay_image = face_recognition.load_image_file("./face_images/Professor_Ajay.png")
Ajay_face_encoding = face_recognition.face_encodings(Ajay_image)[0]

# Load a second sample picture and learn how to recognize it.
Nikhil_image = face_recognition.load_image_file("./face_images/Nikhil.jpeg")
Nikhil_face_encoding = face_recognition.face_encodings(Nikhil_image)[0]

# Load a second sample picture and learn how to recognize it.
Professor_Ak = face_recognition.load_image_file("./face_images/Professor_Ak.png")
Professor_Ak_face_encoding = face_recognition.face_encodings(Professor_Ak)[0]

# Load a second sample picture and learn how to recognize it.
Professor_Alind = face_recognition.load_image_file("./face_images/Professor_Alind.png")
Professor_Alind_face_encoding = face_recognition.face_encodings(Professor_Alind)[0]

# Load a second sample picture and learn how to recognize it.
Professor_Ambika = face_recognition.load_image_file("./face_images/Professor_Ambika.png")
Professor_Ambika_face_encoding = face_recognition.face_encodings(Professor_Ambika)[0]
# Load a second sample picture and learn how to recognize it.
Professor_Anushree = face_recognition.load_image_file("./face_images/Professor_Anushree.png")
Professor_Anushree_face_encoding = face_recognition.face_encodings(Professor_Anushree)[0]

# Load a second sample picture and learn how to recognize it.
Professor_PB = face_recognition.load_image_file("./face_images/Professor_PB.png")
Professor_PB_face_encoding = face_recognition.face_encodings(Professor_PB)[0]

# Load a second sample picture and learn how to recognize it.
Professor_Rohit = face_recognition.load_image_file("./face_images/Professor_Rohit.png")
Professor_Rohit_face_encoding = face_recognition.face_encodings(Professor_Rohit)[0]

# Load a second sample picture and learn how to recognize it.
Professor_Sandeep = face_recognition.load_image_file("./face_images/Professor_Sandeep.png")
Professor_Sandeep_face_encoding = face_recognition.face_encodings(Professor_Sandeep)[0]

# Load a second sample picture and learn how to recognize it.
Professor_Saurabh = face_recognition.load_image_file("./face_images/Professor_Saurabh.png")
Professor_Saurabh_face_encoding = face_recognition.face_encodings(Professor_Saurabh)[0]

# Load a second sample picture and learn how to recognize it.
Professor_Tripathi = face_recognition.load_image_file("./face_images/Professor_Tripathi.png")
Professor_Tripathi_face_encoding = face_recognition.face_encodings(Professor_Tripathi)[0]

# Create arrays of known face encodings and their names
known_face_encodings = [
    Bhupendra_face_encoding,
    biden_face_encoding,
    utsav_face_encoding,
    Ajay_face_encoding,
    Nikhil_face_encoding,
    Professor_Ak_face_encoding,
    Professor_Alind_face_encoding,
    Professor_Ambika_face_encoding,
    Professor_Anushree_face_encoding,
    Professor_PB_face_encoding,
    Professor_Rohit_face_encoding,
    Professor_Sandeep_face_encoding,
    Professor_Saurabh_face_encoding,
    Professor_Tripathi_face_encoding
]
known_face_names = [
    "Professor Bhupendra",
    "Joe Biden",
    "Utsav",
    "Professor Ajay",
    "Nikhil",
    "Professor Akashdeep Bharadwaj",
    "Professor Alind",
    "Professor Ambika",
    "Professor Anushree",
    "Professor Pankaj",
    "Professor Rohit",
    "Professor Sandeep",
    "Professor Saurabh",
    "Professor Tripathi"
]

visitedFaces = {'null': 0}

while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    #rgb_frame = frame[:, :, ::-1]
    
    rgb_frame = np.ascontiguousarray(frame[:, :, ::-1])

    # Find all the faces and face enqcodings in the frame of video
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    # Loop through each face in this frame of video
    all_names = ""
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

        name = "Unknown"

        # If a match was found in known_face_encodings, just use the first one.
        # if True in matches:
        #     first_match_index = matches.index(True)
        #     name = known_face_names[first_match_index]

        # Or instead, use the known face with the smallest distance to the new face
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:                
            name = known_face_names[best_match_index]
            
            visitedNames = visitedFaces.keys()
            
            found = False
            for n in visitedNames:
                if(n == name):
                    found = True
                    print("found " + name + " in the visited list")
                    break
            
            currentT = int(time.time())
            if( found == False):
                visitedFaces.update({name:currentT})
                all_names = all_names + name + " "
            else:
                if(abs(currentT - visitedFaces[name]) > TIME_CUTOFF):
                    print("time passeddddddddddddddddddddddddddddddddddddddddddddddddddddd")
                    del(visitedFaces[name])
                    visitedFaces.update({name:currentT})
                    all_names = all_names + name + " "            
            
            print(visitedFaces)           

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    if(len(all_names) > 1):
        mytext = "Hello " + all_names + welcomeMsg
        myobj = gTTS(text=mytext, lang=language, slow=False)

        myobj.save("welcome.mp3")

        playsound('welcome.mp3')
    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()