import cv2
import numpy as np
face_classifier = cv2.CascadeClassifier("Cascade/haarcascade_frontalface_default.xml")
eye_classifier = cv2.CascadeClassifier("Cascade/haarcascade_eye.xml")

name = input("enter your name:")
cap = cv2.VideoCapture(0)
while True:

	ret, frame = cap.read()

	if ret:
	
		faces = face_classifier.detectMultiScale(frame)
		eye = eye_classifier.detectMultiScale(frame)
		for face in faces:
			fx, fy, fw, fh = face
			cv2.rectangle(frame, (fx, fy), (fx+fw, fy+fh), (255,255,255), 2)
			cv2.putText(frame, name, (fx, fy-12), cv2.FONT_HERSHEY_COMPLEX, 2, (255,0,0),2)
		for ex, ey, ew, eh  in eye:
			cv2.rectangle(frame, (ex, ey), (ex+ew, ey+eh), (255,0,0),2)
			
			
		cv2.imshow("capture",frame)
			
	key = cv2.waitKey(1)
	if key == ord("q"):
		break
	if key == ord("c"):
		cv2.imwrite(name + ".jpg", frame)	
cap.release()
cv2.destroyAllWindows()
