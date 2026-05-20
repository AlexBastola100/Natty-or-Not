from numpy import array, exp

def sigmoid(x):
    return 1 / (1 + exp(-x))

def normalize_data(data):
    return data / array([200, 120, 250]) 

def convert_to_metric(x):
    conversion = array([2.54, 0.453592, 0.453592]) #inch to cm, lbs to kg, lbs to kg
    return x * conversion