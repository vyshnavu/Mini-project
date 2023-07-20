from tele import call
import cv2
from time import sleep 
import asyncio
import serial
import time
from catcher import unauthorised_person
def main_app(name):
        # Establish serial communication with Arduino
        arduino = serial.Serial('COM2', 9600)  # Replace 'COM3' with the appropriate port
        # Allow time for the connection to be established
        time.sleep(2)
        
        face_cascade = cv2.CascadeClassifier('./data/haarcascade_frontalface_default.xml')
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read(f"./data/classifiers/{name}_classifier.xml")
        #recognizer.read(f"./data/classifiers/"+"akku"+"_classifier.xml")
        cap = cv2.VideoCapture(0)
        pred = 0
        while True:
            ret, frame = cap.read()
            #default_img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray,1.3,5)

            for (x,y,w,h) in faces:


                roi_gray = gray[y:y+h,x:x+w]

                id,confidence = recognizer.predict(roi_gray)
                confidence = 100 - int(confidence)
                pred = 0
                if confidence > 50:
                    #if u want to print confidence level
                            #confidence = 100 - int(confidence)
                            pred += +1
                            text = "Authorized Person"
                            font = cv2.FONT_HERSHEY_PLAIN
                            frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                            frame = cv2.putText(frame, text, (x, y-4), font, 1, (0, 255, 0), 1, cv2.LINE_AA)

                else:   
                            pred += -1
                            text = "UnAuthorized Person"
                            font = cv2.FONT_HERSHEY_PLAIN
                            frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
                            frame = cv2.putText(frame, text, (x, y-4), font, 1, (0, 0,255), 1, cv2.LINE_AA)

            cv2.imshow("image", frame)


            if cv2.waitKey(20) & 0xFF == ord('q'):
                print(pred)
                if pred > 0 : 
                    arduino.write(b'1')  # Send command to turn on the relay
                    print("Relay turned on.") 
                      
                else:
                    
                    arduino.write(b'0')  # Send command to turn off the relay
                    print("Relay turned off.")
                    unauthorised_person()
                    asyncio.run(call())

# Close the serial connection
                arduino.close()
                break


        cap.release()
        cv2.destroyAllWindows()
        
