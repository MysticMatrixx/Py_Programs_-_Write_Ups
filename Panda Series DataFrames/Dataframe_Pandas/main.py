
import pandas as p 

l = {
    # Nested Dictionary
    'X' : { 1: 'a', 2: 'b', 3: 'c', 4: 'd' },
    'Y' : { 1: 'gunja', 2: 'jasus', 3: 'mahir', 4: 'jax' },
    'Z' : { 0: 'kolkata', 'c': 'delhi', 3: 'hyderabad', 'a': 'gujarat' },
}
lDataframe = p.DataFrame(l)
print(lDataframe.fillna(0))
# print(lDataframe.replace(n.nan,0))



s1 = p.Series((1,2,3,4,5))
s2 = p.Series(("a", "b", "c", "d", "e"))
# Two Series 
# Into One DataFrame
df = p.DataFrame([s1, s2])
print(df)
