import os
from datetime import datetime
from ultralytics import YOLO
import cv2 as cv

#To switch to non-gpu uncomment the line below by removing the #
#from angleCalculator import angle_calculator
from angleCalculator_gpu import angle_calculator
from classifier import predict_class
import csv

#log the results in a csv file
def log_joint_angles_to_csv(csv_file, data):
    file_exists = os.path.isfile(csv_file)
    with open(csv_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        
        if not file_exists:
            writer.writerow(data.keys())
            writer.writerow(data.values())

#change path to video you want to analyze - if you want the webcam choose 0
video_path = "./images/vid.mp4"

model = YOLO("yolo11m-pose.pt") # load an official model
current_time = datetime.now().strftime("%H%M") 
csv_file = f'joint_angles_{current_time}.csv'

cap = cv.VideoCapture(video_path)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, frame = cap.read()
 
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    results = model.predict(source=frame, show=True ,verbose=False, device=0) #Predict on the provided frame
    for r in results:
        body_angels = angle_calculator(r.keypoints.xy[0])
        log_joint_angles_to_csv(csv_file, body_angels)
        current_class = predict_class(body_angels)
        #give_feedback(body_angels, current_class)
    if cv.waitKey(1) == ord('q'):
        break
 
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()
