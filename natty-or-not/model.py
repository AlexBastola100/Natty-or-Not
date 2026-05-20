import numpy as np
from utils import convert_to_metric, sigmoid, normalize_data
from data import sample_biometrics, sample_status

def train(): #Finding the appropriate weights and bias for the model 
    training_x = normalize_data(sample_biometrics) #height (cm), weight (kg), 1rpm (kg)
    training_y = sample_status #Natty or Not (0 or 1)
    W = np.random.randn(3) * 0.01 #sensible random weights 
    B = 0
    loss_threshold = 0.39
    lr = 0.001 #learning rate 

    while True:
        prediction = sigmoid(training_x @ W + B) # z = w1* x1+ w2 * x2 + w3 * x3 + b
        error = prediction - training_y

        grad_W = (training_x.T @ error) / len(training_y) #How much to change the feature weights based on the error
        grad_B = np.mean(error) 
    
        W = W - grad_W * lr
        B = B - grad_B * lr

        loss = -np.mean(training_y * np.log(prediction) + (1 - training_y) * np.log(1 - prediction)) #How wrong the model is on average (lower the better)
        print("Loss: ", loss)
        if loss <= loss_threshold:
            return W, B
    
def predict(height, weight, rpm, W, B): #height (inch), weight (lbs), 1rpm (lbs)  
    metric_biometrics = convert_to_metric(np.array([height, weight, rpm]))
    normalized_biometrics = normalize_data(metric_biometrics)

    return sigmoid(normalized_biometrics @ W + B) 
