import numpy as np

arr = [2,3,45,56,77,88,97]
n = len(arr)
sumArr = 0

for x in arr:
    sumArr += x

mean = sumArr / n
standardDeviation = 0
variance = 0
sumSD = 0

for x in arr:
    temp = (x - mean)
    sumSD += (temp ** 2)

variance = sumSD / (n)
standardDeviation = (variance ** 0.5)

print("NUMPY")
print("mean = " + str(np.mean(arr)) 
      + "\nstandard deviation = " 
      + str(np.std(arr)) 
      + "\nvariance = " + str(np.var(arr)))

print("\nSELF")
print("mean = " + str(mean) 
      + "\nstandard deviation = " 
      + str(standardDeviation) 
      + "\nvariance = " + str(variance))
