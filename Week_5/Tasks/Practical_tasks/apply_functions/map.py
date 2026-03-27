import pandas as pd
import numpy as np

#---------- map
df = pd.DataFrame(data=np.random.randint(0, 10, size=[4,3]), columns=["Book1", "Book2", "Book3"])
print(df, '\n')

# print(df.map(lambda x: len(str(x))))
print(df.map(lambda x: x**2))