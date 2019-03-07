# May Julia
# Cw. 2
# Python

def dotProduct(v1, v2):
    result = 0
    for i in range(len(v1)):
        result += v1[i] * v2[i]
    return result

def f(n):
    if (n >= 0):
        return 1
    else:
        return 0

def perceptronLearn(U, W, c):
    currentW = W
    t = 1
    counter = 0
    while (counter != 5):
        index = (t - 1) % 5
        if (index < 3):
            z = 1.0
        else:
            z = 0.0
        y = f(dotProduct(currentW, U[index])) 
        if (z != y):
            for i in range(len(W)):
                currentW[i] += c * (z - y) * U[index][i]
        t += 1
        if (z == y):
            counter += 1
        else:
            counter = 0
    return t, currentW

U1 = [0,0,0,0,0,0,1,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,1]
U2 = [0,0,1,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1]
U3 = [0,0,0,0,0,1,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,1]
U4 = [0,0,0,0,0,0,1,1,1,0,0,1,0,1,0,0,1,1,1,0,0,0,0,0,0,1]
U5 = [0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,1,0,1,0,0,1,1,1,0,0,1]
W = [0 for i in range(26)]

U = [U1, U2, U3, U4, U5]

for i in [1.0, 0.1, 0.01]:

    time, weights = perceptronLearn(U, W, i)
    print('t = ' + str(time))
    print('w[t] = ' + str(weights) + '\n')

    
