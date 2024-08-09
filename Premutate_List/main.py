def permutateList ( ls ):
    if len(ls) == 0:
        return []
    elif len(ls) == 1:
        return [ls]

    per = []
    for i in range(len(ls)):
        a=ls[i]
        x=ls[:i] + ls[i+1:]
        for y in permutateList(x):
           per.append([a]+y)
    return per

user_list = []

n = int(input("Enter the range of the list: "))

print("Enter the Elements: ")
for i in range(n):
    user_list.append(int(input()))

result = permutateList(user_list)
for x in result:
    print(x)
