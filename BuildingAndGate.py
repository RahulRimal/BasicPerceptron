import random as ran

lr = 1			# Learning Rate
bs = 1			# Bias
weights = [ran.random(), ran.random(), ran.random()]		# Weight for Connection of 1st Input, 2nd Input and Bias Input

def perceptron(input1, input2, output):
	output_predect = input1 * weights[0] + input2 * weights[1] + bs * weights[2] 		# Calcualtion for predection by the neuron

	if output_predect > 0:				# Kinda like the activation function....  ;)
		output_predect = 1
	else:
		output_predect = 0

	error = output - output_predect		# Error Calculation
	weights[0] += error * input1 * lr
	weights[1] += error * input2 * lr 	# Correcting the Weights !!
	weights[2] += error * bs * lr

for i in range(30):
	perceptron(0, 0, 0)
	perceptron(0, 1, 0)					# Training the Model
	perceptron(1, 0, 0)
	perceptron(1, 1, 1)

input1 = int(input("Enter the 1st value (0 or 1):  "))					# Getting the Inputs form the User 
input2 = int(input("Enter the 2nd value (0 or 1):  "))

out = input1 * weights[0] + input2 * weights[1] + bs * weights[2]		# Predection Calculation

if out >0:
	out = 1
else:
	out = 0

print(input1, "or", input2, " is : ", out)