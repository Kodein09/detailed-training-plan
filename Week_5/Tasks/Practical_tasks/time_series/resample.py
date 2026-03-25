import pandas as pd
import numpy as np

# index = pd.date_range("1/1/2000", periods=9, freq="min")
# series = pd.Series(range(9), index=index)
# print(index, '\n')
# print(series, '\n')
#
# print(series.resample('3min').sum(), '\n')
#
# print(series.resample('3min', label='right').sum(), '\n')
#
# print(series.resample('3min', label='right', closed='right').sum(), '\n')
#
# print(series.resample('30s').asfreq()[0:5], '\n')
#
# print(series.resample('30s').ffill()[0:5], '\n')
#
# print(series.resample('30s').bfill()[0:5], '\n')
#
# def custom_resample(arraylike):
#     return np.sum(arraylike)
#
# print(series.resample("3min", label='left', closed='left').apply(custom_resample), '\n')
# print(series.resample("3min", label='right', closed='right').apply(custom_resample), '\n')
# print(series.resample("3min", label='left', closed='right').apply(custom_resample), '\n')
# print(series.resample("3min", label='right', closed='left').apply(custom_resample), '\n')

# index = pd.date_range("01:00", periods=5, freq='min')
# series = pd.Series(range(5), index=index)
# print(index)
# print(series)
# print(series.resample('5min', label='left', closed='right'))


#Resample a year by quartet using "start" convention. Values are assigned to the first quarter of the period
# s = pd.Series(
#     [1,2], index=pd.period_range(start="2026", periods=2, freq="Y")
# )
# print(s, '\n')
#
# print(s.resample(rule="Q", convention="end").asfreq())

# index = pd.period_range("2000-01-01", periods=5, freq='Q')
# df = pd.DataFrame(data=range(0, 5), index=index, columns=['count'])
#
# print(df, '\n')
#
# print(df.resample(rule='M', label="left", closed='left').sum())

#
# index = pd.period_range(start="00:00", periods=4, freq='min')
# s = pd.Series(data=[1,2,3,4], index=index)
# print(s, '\n')
#
# print(s.resample(rule='3min', closed='right').sum())
# print(s.resample(rule='3min', closed='left').sum())

# rng = pd.date_range(start="2025-09-01", periods=25, freq='h')
# ts = pd.DataFrame(data=range(0, 25), index=rng, columns=['day'])
# print(ts, '\n')
#
# print(ts.resample(rule='d', closed='right').sum())


# index = pd.date_range("2000-1-2", periods=9, freq="3min")
# df = pd.DataFrame(data=range(9), index=index, columns=["count"])
# print(df, '\n')
#
# print(df.resample("7min", label="right", closed="right").sum())