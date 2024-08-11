import numpy as np
import pandas as pd

data = {"color": ["red", "blue", "red", "green"]}
df = pd.DataFrame(data)

df = pd.get_dummies(df).astype('int32')
print(df.filter(items=["color_red", "color_blue", "color_green"]))