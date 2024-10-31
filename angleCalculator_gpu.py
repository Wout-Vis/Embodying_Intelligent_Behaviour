import numpy as np

# Function to calculate angle between three points, for point P2
def calculate_angle(p1, p2, p3):
    # Create vectors from points
    v1 = p1 - p2
    v2 = p3 - p2

    # Normalize vectors
    v1_norm = v1 / np.linalg.norm(v1)
    v2_norm = v2 / np.linalg.norm(v2)
    
    # Calculate the angle in radians between the vectors
    dot_product = np.dot(v1_norm, v2_norm)
    angle_radians = np.arccos(np.clip(dot_product, -1.0, 1.0))
    
    # Convert radians to degrees
    angle_degrees = np.degrees(angle_radians)
    #angle_degrees = round(angle_degrees, 2)

    return angle_degrees

# Function to calculate angle relative to ground (horizontal)
def calculate_ground_angle(p1, p_ground):
    v = p1 - p_ground
    angle_radians = np.arctan2(v[1], v[0])
    angle_degrees = np.degrees(angle_radians)
    return abs(angle_degrees)

# Function to handle missing data (if point is [0.0, 0.0])
def adjust_for_missing_data(point):
    if np.all(point == 0.0):
        return np.array([0.01, 0.01])  # Adjust missing points slightly to avoid errors
    return point

# Function to calculate angle with check for missing data
def calculate_angle_with_check(p1, p2, p3):
    p1, p2, p3 = adjust_for_missing_data(p1), adjust_for_missing_data(p2), adjust_for_missing_data(p3)
    return calculate_angle(p1, p2, p3)

# Function to calculate ground angle with check for missing data
def calculate_ground_angle_with_check(p1, p2):
    p1 = adjust_for_missing_data(p1)
    return calculate_ground_angle(p1, p2)

# Example data block


def angle_calculator(data_block):
    data_block = data_block.cpu()
    datapoints = np.array([point.float() for point in data_block])
    if len(datapoints) == 17:
        nose, left_eye, right_eye, left_ear, right_ear, left_shoulder, right_shoulder, left_elbow, right_elbow, left_wrist, right_wrist, left_hip, right_hip, left_knee, right_knee, left_ankle, right_ankle = datapoints
        shoulder_angle_left = calculate_angle_with_check(left_elbow, left_shoulder, left_hip)
        shoulder_angle_right = calculate_angle_with_check(right_elbow, right_shoulder, right_hip)

        elbow_angle_left = calculate_angle_with_check(left_shoulder, left_elbow, left_wrist)
        elbow_angle_right = calculate_angle_with_check(right_shoulder, right_elbow, right_wrist)

        hip_angle_left = calculate_angle_with_check(left_shoulder, left_hip, left_knee)
        hip_angle_right = calculate_angle_with_check(right_shoulder, right_hip, right_knee)

        knee_angle_left = calculate_angle_with_check(left_hip, left_knee, left_ankle)
        knee_angle_right = calculate_angle_with_check(right_hip, right_knee, right_ankle)

        results = {
        "Shoulder_Angle_Left": shoulder_angle_left,
        "Shoulder_Angle_Right": shoulder_angle_right,
        "Elbow_Angle_Left": elbow_angle_left,
        "Elbow_Angle_Right": elbow_angle_right,
        "Hip_Angle_Left": hip_angle_left,
        "Hip_Angle_Right": hip_angle_right,
        "Knee_Angle_Left": knee_angle_left,
        "Knee_Angle_Right": knee_angle_right
        }
        return(results)
    
    else:
        results = {
        "Shoulder_Angle_Left": 0,
        "Shoulder_Angle_Right": 0,
        "Elbow_Angle_Left": 0,
        "Elbow_Angle_Right": 0,
        "Hip_Angle_Left": 0,
        "Hip_Angle_Right": 0,
        "Knee_Angle_Left": 0,
        "Knee_Angle_Right": 0
        }
        return(results)
