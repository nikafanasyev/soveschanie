from django.shortcuts import render
import numpy as np
import cv2

def index(request):
    cap = cv2.VideoCapture(0)
    ret, _ = cap.read()
    if ret == True:
        res = "Camera is working"
    else:
        res = "Camera is not working"
    data = {"res": res}
    cv2.destroyAllWindows()
    return render(request, 'mainApp/connecting.html', context=data)
    