
import math

val = int(input("Enter x : "))
precision = int(input("Enter n : "))

power = 1.0
neg = 1

def sin(v, p):
    global power, neg
    
    if (p == 1): 
        power = v
        return v
    
    recursiveCall = sin(v, p - 1)
    
    power = power * v * v
    
    factorial = math.factorial((2 * p - 1))
    
    if neg <= 1: neg *= -1

    return (recursiveCall + (neg * power / factorial))


power = 1.0
neg = 1

def cos(v, p):
    global power, neg

    if (p == 1): 
        return 1
    
    recursiveCall = cos(v, p - 1)
    
    power = power * v * v
    
    factorial = math.factorial((2 * p - 2))
    
    if neg <= 1: neg *= -1

    return (recursiveCall + (neg * power / factorial))


# for sin x
print(sin(val, precision))

# for cos x
print(cos(val, precision))