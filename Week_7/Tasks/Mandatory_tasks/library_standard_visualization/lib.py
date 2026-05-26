import matplotlib.pyplot as plt

class MatPlotlibStandardViz:
    def __init__(self, figsize=(10, 6)):
        self._figsize = figsize

    def _setup_plot(self, title, xlabel, ylabel, legend=None):
        plt.figure(figsize=self._figsize)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        if legend is not None:
            plt.legend(legend)
        plt.grid(True, linestyle='--', alpha=0.7)

    def plot_line(self, x, y, title='Line Plot', xlabel='X', ylabel='Y'):
        self._setup_plot(title, xlabel, ylabel)
        plt.plot(x, y)
        plt.show()

    def plot_scatter(self, x, y, title='Scatter Plot', xlabel='X', ylabel='Y'):
        self._setup_plot(title, xlabel, ylabel)
        plt.scatter(x, y)
        plt.show()

    def plot_barchart(self, categories, values, title='Bar Chart'):
        self._setup_plot(title, "Categories", "Values")
        plt.bar(categories, values)
        plt.show()

    def plot_histogram(self, data, bins=10, title='Histogram Plot'):
        self._setup_plot(title, 'Value', 'Frequency')
        plt.hist(data, bins=bins, edgecolor='black')
        plt.show()

    def plot_pie(self, x, labels=None, title='Pie Plot'):
        self._setup_plot(title, '', '')
        plt.pie(x, labels=labels, autopct='%1.1f%%', startangle=90)
        plt.show()

    def plot_boxplot(self, x, title='Box Plot'):
        self._setup_plot(title, 'X', 'Y')
        plt.boxplot(x, showbox=True, showfliers=True, showmeans=True, showcaps=True)
        plt.show()

    def plot_violin(self, dataset, title='Violin Plot'):
        self._setup_plot(title, 'X', 'Y')
        plt.violinplot(dataset, showmedians=True, showmeans=True, showextrema=False)
        plt.show()

viz = MatPlotlibStandardViz()
# viz.plot_line([1, 2, 3], [10, 20, 15], title="Динамика роста")
# viz.plot_scatter([1, 2, 3], [10, 20, 15], title="Координаты")
# viz.plot_barchart(['Chocolate', 'Cakes', 'Ice-creams'], [10, 20, 15], title="Goods in Stock")
# viz.plot_pie([1,10,5,8], title='Purchases')
# viz.plot_histogram([1,10,5,8])
# viz.plot_violin([[1,5,8], [4,6,7]])
# viz.plot_boxplot([[1,5,8], [4,6,7]])

