#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 12:30:53 2024

@author: upes
"""

import cv2

# Open the default camera
cam = cv2.VideoCapture(0)


while True:
    ret, frame = cam.read()


    # Display the captured frame
    cv2.imshow('Camera', frame)

    # Press 'q' to exit the loop
    if cv2.waitKey(1) == ord('q'):
        break

# Release the capture and writer objects
cam.release()
out.release()
cv2.destroyAllWindows()
