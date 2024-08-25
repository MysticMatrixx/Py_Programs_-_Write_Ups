
text = """For a some quick analysis, creating a corpus could or might be overkill. If all you need is a word list, but its fine and as there are some simpler ways to achieve that goal for further operations."""

t = text.split()
freq = {}
for i in t:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

keys = list(freq.keys())
values = list(freq.values())
values.sort(reverse=True)

sortedDict = {}

for i in values:
    for j in keys:
        if i == freq[j]:
           sortedDict[j] = i

print(sortedDict)
