import pandas as pd
import numpy as np

# def func(a):
#     return a**a
#
# squared = pd.Series(
#     data=[1,2,3,4]
# )
# print(squared.apply(func))


# df = pd.DataFrame([[2,3]] * 4, columns=["A", "B"])
# print(df, '\n')
#
# print(df.apply(np.sqrt), '\n')
#
# print(df.apply(func=np.sum, axis=0), '\n')
# print(df.apply(func=np.sum, axis=1), '\n')
#
# print(f"result_type=reduce(){df.apply(func=lambda x: [1,2], axis=0, raw=False, result_type='reduce')}", '\n')
# print(f"result_type=expand:\n{df.apply(func=lambda x: [1,2,3], axis=1, raw=False, result_type='expand')}", '\n')
#
# print(df.apply(func=lambda x: x**2, axis=0, raw=True, result_type='expand'))

# df = pd.DataFrame(data=np.random.randn(4,3), columns=list('ABC'))
# print(df, '\n')
#
# fn = lambda ser: ser.max() - ser.min()
# print(df.apply(fn))


