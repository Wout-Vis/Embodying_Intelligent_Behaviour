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


model = YOLO("yolo11m-pose.pt") # load an official model
current_time = datetime.now().strftime("%H%M") 
csv_file = f'joint_angles_{current_time}.csv'

#change the source to a file to get the points
results = model.predict(source="./images/Media1.mp4", show=True, verbose=False, device=0, save=True)  # predict on an image
