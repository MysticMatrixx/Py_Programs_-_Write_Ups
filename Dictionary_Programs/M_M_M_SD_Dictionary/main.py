import numpy as n
import scipy.stats as s

d = {
    1 : 98,
    2 : 27,
    3 : 11,
    4 : 54,
    5 : 50,
    6 : 98,
}

vals = list(d.values())

mean = n.mean(vals)

sumSD = 0
for x in vals:
    sumSD += (x - mean) ** 2
    
median =  n.median(vals)
mode = s.mode(vals)
resSD = n.sqrt(sumSD / len(vals))

print(mean)
print(median)
print(mode)
print(resSD)
