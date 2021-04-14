from os import path
import cv2 as cv
import torch

#print(torch.cuda.device_count())
#print(torch.cuda.is_available())

i = input('Please enter:')
path = path.dirname(__file__) + '\\'
path = path + i

output = cv.imread(path)
cv.imshow('Group of 5 people', img)

#scale_percent = 60
#calculate the 50 percent of original dimensions
#width = int(img.shape[1] * scale_percent / 100)
#height = int(img.shape[0] * scale_percent / 100)
# dsize
#dsize = (width, height)
# resize image
#output = cv.resize(img, dsize)

gray = cv.cvtColor(output, cv.COLOR_BGR2GRAY)
cv.imshow('Gray People', gray)

haar_cascade = cv.CascadeClassifier("C:\\Users\\osamh\\Documents\\Python Scripts\\HaarCascade\\face.xml")

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=2)

print(f'Number of faces found = {len(faces_rect)}')
    
for (x,y,w,h) in faces_rect:
    cv.rectangle(output, (x,y), (x+w,y+h), (0,255,0), thickness=2)

cv.imshow('Detected Faces', output)

cv.waitKey(0)