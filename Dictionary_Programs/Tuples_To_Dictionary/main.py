
n = input("Enter the size of the tuple:")
tuples_list = []

print("Enter " + n + " values for tuple 1 :")
for x in range(int(n)):
    k = input("Key : ")
    v = input("Value : ")
    
    tuples_list.append((k,v))

print(dict(tuples_list))





# something else
# theDict = tuple(zip(tup1, tup2))