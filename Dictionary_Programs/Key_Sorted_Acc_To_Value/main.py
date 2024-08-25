
sortedDict = {}
dic = {
    "Three":3,
    "Two":2,
    "Four":4,
    "One":1,
}

keys = list(dic.keys())
values = list(dic.values())
values.sort()

# print(values)

for i in values:
    for j in keys:
        if i == dic[j]:
           sortedDict[j] = i

print(sortedDict)