import os
import plotly.io as pio
import plotly.express as px
import plotly.graph_objects as go

from dash import dash, dash_table, Output, Input, callback, html, dcc

pio.defaults.default_format = 'png'

class GraphExport:
    def __init__(self, output_dir: str = 'images'):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    # def to_png(self, fig: go.Figure, filename: str = 'graph.png'):
    #     full_path = os.path.join(self.output_dir, filename)
    #     fig.write_image(full_path)
    #     print("Graph was successfully saved as static image png")
    #
    # def to_jpeg(self, fig: go.Figure, filename: str = 'graph.jpeg'):
    #     full_path = os.path.join(self.output_dir, filename)
    #     fig.write_image(full_path)
    #     print("Graph was successfully saved as static image jpeg")
    #
    # def to_webp(self, fig: go.Figure, filename: str = 'graph.webp'):
    #     full_path = os.path.join(self.output_dir, filename)
    #     fig.write_image(full_path)
    #     print("Graph was successfully saved as static image webp")
    #
    # def to_svg(self, fig: go.Figure, filename: str = 'graph.svg'):
    #     full_path = os.path.join(self.output_dir, filename)
    #     fig.write_image(full_path)
    #     print("Graph was successfully saved as static image svg")
    #
    # def to_pdf(self, fig: go.Figure, filename: str = 'graph.pdf'):
    #     full_path = os.path.join(self.output_dir, filename)
    #     fig.write_image(full_path)
    #     print("Graph was successfully saved as static image pdf")
    #
    # def to_eps(self, fig: go.Figure, filename: str = 'graph.eps'):
    #     full_path = os.path.join(self.output_dir, filename)
    #     fig.write_image(full_path)
    #     print("Graph was successfully saved as static image eps")

    def to_image(self, fig: go.Figure, filename: str = 'graph.png') -> None:
        ext = os.path.splitext(filename)[1].lower().strip('.')
        valid_extensions = ['png', 'jpeg', 'webp', 'svg', 'pdf', 'eps']
        if ext not in valid_extensions:
            raise ValueError(f"Unsupported file format '.{ext}' Use one of {valid_extensions}")
        full_path = os.path.join(self.output_dir, filename)
        fig.write_image(full_path)
        print(f"Graph was successfully saved as static image {ext}")

    def to_html(self, fig: go.Figure, filename: str = 'graph.html') -> None:
        full_path = os.path.join(self.output_dir, filename)
        fig.write_html(full_path)
        print("Graph was successfully saved as html file")

    def to_json(self, fig: go.Figure, filename: str = 'graph.json') -> None:
        full_path = os.path.join(self.output_dir, filename)
        fig.write_json(full_path)
        print("Graph was successfully saved as json file")

exp = GraphExport()

def figure():
    df_usa = px.data.gapminder().query("country == 'Germany'")
    fig = px.bar(df_usa, x='year', y='pop')
    return fig

graph = figure()

# exp.to_image(graph, 'graph2.eps')
# exp.to_html(graph)
# exp.to_json(graph)