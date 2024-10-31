import os
from datetime import datetime
from ultralytics import YOLO
import cv2 as cv
from angleCalculator_gpu import angle_calculator
import csv

def log_joint_angles_to_csv(csv_file, data):
    # Check if the file already exists
    file_exists = os.path.isfile(csv_file)
    
    # Open the file in append mode
    with open(csv_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        
        # Write header only if the file doesn't exist (first time writing)
        if not file_exists:
            writer.writerow(data.keys())
        
        # Write the new row (joint angles)
        writer.writerow(data.values())

#change path to video you want to analyze - if you want the webcam choose 0


model = YOLO("yolo11x-pose.pt") # load an official model
current_time = datetime.now().strftime("%H%M") 
csv_file = f'joint_angles_{current_time}.csv'

results = model.predict(source="./images/Media1.mp4", show=True, verbose=False, device=0, save=True)  # predict on an image
#for r in results:
    #body_angels = angle_calculator(r.keypoints.xy[0])
    #log_joint_angles_to_csv(csv_file, body_angels)




#from ultralytics import ultralytics.yolo.v8.detect.predict import DetectionPredictor
#import cv2
#model = YOLO("yolo11n-pose.pt") # load an official model

# Use the model
#results = model.predict(source='0', show=True)  # predict on an image
#for r in results:
#    print(r.keypoints)
#results[0].show()