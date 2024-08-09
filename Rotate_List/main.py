n = int(input("Enter the array size : "))
ls = []

print("Enter the elements : ")
for x in range(n):
    ls.append(input(""))

step = int(input("Enter the steps : "))
res = ls[step+1:] + ls[:step+1]

print(ls)
print(res)