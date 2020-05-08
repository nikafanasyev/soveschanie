from django.shortcuts import render
import numpy as np
import cv2

def index(request):
    return render(request, 'mainApp/homePage.html')
