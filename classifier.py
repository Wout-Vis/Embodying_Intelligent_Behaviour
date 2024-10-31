from tensorflow import keras
import numpy as np
from sklearn.preprocessing import StandardScaler


def predict_class(data):
    sc = StandardScaler()

    model = keras.models.load_model('./exercise_detection_15.keras')
    new_data = list(data.values())
    new_data = np.array(new_data).reshape(1, -1)  # Shape (1, 8)
    predicted_class_probabilities = model.predict(new_data, verbose=False)
    predicted_class = np.argmax(predicted_class_probabilities, axis=1)
    exercise_classes = ['Pullup', 'Pushup', 'Situp', 'Squad']
    predicted_exercise = exercise_classes[predicted_class[0]]
    print(f"Predicted exercise: {predicted_exercise}")