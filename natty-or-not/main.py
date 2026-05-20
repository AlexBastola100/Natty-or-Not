from model import train, predict

height = 68 #inches
weight = 130 #lbs
rpm = 405 #lbs

weights, bias = train()
print("Trained Weights & Bias: ", weights, bias)

prediction = predict(height, weight, rpm, weights, bias)
print("Prediction (0-1, where 1 is enhanced):", prediction)