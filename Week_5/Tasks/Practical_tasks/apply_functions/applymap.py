import pandas as pd
import numpy as np

#Works only with DataFrames, applies function to each element (element-by-element)
#But applymap has FutureWarning: FutureWarning: DataFrame.applymap has been deprecated. Use DataFrame.map instead.

df = pd.DataFrame(data={
    "A": [1,2],
    "B": [3,4]
})

def show_order(x):
    print(x)
    return x * 10

print(df, '\n')
print(df.applymap(show_order))