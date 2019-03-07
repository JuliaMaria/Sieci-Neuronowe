# May Julia
# Cw. 1
# Python

import numpy as np

def notOperator(bit):
    weights = np.array([-0.5, 0.3])
    result = np.dot(weights, np.array([bit, 1]))
    return 1 if result>=0 else 0

def andOperator(bit1, bit2):
    weights = np.array([0.4, 0.4, -0.6])
    result = np.dot(weights, np.array([bit1, bit2, 1]))
    return 1 if result>=0 else 0

def orOperator(bit1, bit2):
    weights = np.array([0.4, 0.4, -0.3])
    result = np.dot(weights, np.array([bit1, bit2, 1]))
    return 1 if result>=0 else 0

def nandOperator(bit1, bit2):
    weights = np.array([-0.3, -0.3, 0.4])
    result = np.dot(weights, np.array([bit1, bit2, 1]))
    return 1 if result>=0 else 0

print(notOperator(1))
print(notOperator(0))

print(andOperator(0, 0))
print(andOperator(0, 1))
print(andOperator(1, 0))
print(andOperator(1, 1))

print(orOperator(0, 0))
print(orOperator(0, 1))
print(orOperator(1, 0))
print(orOperator(1, 1))

print(nandOperator(0, 0))
print(nandOperator(0, 1))
print(nandOperator(1, 0))
print(nandOperator(1, 1))

