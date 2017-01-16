import numpy as np

numSamples = 100
numFeatures = 2

X = np.random.randn(numSamples, numFeatures)

X[:50, :] = X[:50, :] - 2 * np.ones((50, numFeatures))
X[50:, :] = X[50:, :] + 2 * np.ones((50, numFeatures))

target = np.array([0] * 50 + [1] * 50)

ones = np.array([[1] * numSamples]).T
Xb = np.concatenate((ones, X), axis = 1)

#initialize weights
weights = np.random.randn(numFeatures + 1)

#calcuate output of the model
output = Xb.dot(weights)

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

Y = sigmoid(output)

def calc_cross_entropy(target, Y):
    entropy = 0
    for i in xrange(numSamples):
        if target[i] == 1:
            entropy -= np.log(Y[i])
        else:
            entropy -= np.log(1 - Y[i])
    return entropy

print calc_cross_entropy(target, Y)
