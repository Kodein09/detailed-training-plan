from typing import Any

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class AutoSelect:
    def __init__(self, figsize=(10,6)) -> None:
        self._figsize = figsize

    def _setup_plot(self, title: str, xlabel: str, ylabel: str) -> None:
        plt.figure(figsize=self._figsize)
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.grid(True, linestyle='--', alpha=0.6)

    def dispatcher(self, data: Any = None, x: Any = None, y: Any = None):
        #Check block
        if (data is None or len(data) == 0) and (x is None or y is None):
            raise ValueError("No data to plot")

        if x is not None and y is not None:
            if len(x) > 50:
                self.scatter(x, y)
                return
            else:
                self.line(x, y)
                return

        #Init block
        arr = np.array(data)
        unique_count = len(np.unique(arr))
        total_count = len(arr)

        is_numeric = np.issubdtype(arr.dtype, np.number) and not isinstance(arr[0], bool)

        #Logic block
        #int/float
        if is_numeric:
            if total_count >= 1000:
                self.violin(arr)
            else:
                self.hist(arr)

        #str
        elif isinstance(arr[0], str):
            self.bar(arr)

        #bool
        elif isinstance(arr[0], (object, bool)) or unique_count <= 5:
            if np.issubdtype(arr.dtype, np.number) and (0.99 <= np.sum(arr) <= 1.01 or 99 <= np.sum(arr) <= 101):
                self.pie(arr)
            else:
                self.bar(arr)

        #Undefined
        else:
            raise ValueError("Undefined dtype")

    #Plot block
    def line(self, x=None, y=None) -> None:
        self._setup_plot('Line Plot', 'X-axis', 'Y-axis')
        plt.plot(x, y, marker='o')
        plt.show()

    def scatter(self, x, y) -> None:
        self._setup_plot('Scatter Plot', 'X-axis', 'Y-axis')
        plt.scatter(x, y, alpha=0.5)
        plt.show()

    def bar(self, data: Any = None) -> None:
        self._setup_plot('Bar Plot', 'Category', 'Count')
        counts = pd.Series(data).value_counts()
        plt.bar(counts.index.astype(str), counts.values)
        plt.show()

    def hist(self, data: Any, bins=30) -> None:
        self._setup_plot('Histogram Plot', 'Value', 'Frequency')
        plt.hist(data, bins=bins, edgecolor='black', alpha=0.7)
        plt.show()

    def pie(self, data: Any) -> None:
        self._setup_plot('Composition', '', '')
        counts = pd.Series(data).value_counts()
        plt.pie(counts, labels=counts.index.astype(str), autopct='%1.1f%%')
        plt.show()

    def boxplot(self, data: Any) -> None:
        self._setup_plot('Statistical Distribution', '', '')
        plt.boxplot(data, showmeans=True, showbox=True, showfliers=True, showcaps=True)
        plt.show()

    def violin(self, data: Any) -> None:
        self._setup_plot('Statistical Distribution', '', '')
        plt.violinplot(data, showmeans=True, showmedians=True, showextrema=True)
        plt.show()

viz = AutoSelect()
viz.dispatcher([1,5,3,8,10])