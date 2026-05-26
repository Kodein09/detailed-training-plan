import numpy as np
import pandas as pd
import dash_ag_grid as dag
import plotly.express as px
import plotly.graph_objects as go

from  dash import Dash, html, dcc, callback, Output, Input

# np.random.seed(1)
#
# n = 100_000
#
# df = pd.DataFrame(dict(x=np.random.randn(n), y=np.random.randn(n)))
#
# fig = px.scatter(df, x='x', y='y', render_mode='webgl')
# fig.update_traces(marker_line=dict(width=1, color='DarkSlateGray'))
# fig.show()

# np.random.seed(1)
# n = 1_000_000
# fig = go.Figure()
# fig.add_trace(
#     go.Scattergl(
#         x=np.random.randn(n),
#         y=np.random.randn(n),
#         mode='markers',
#         marker = dict(
#             line = dict(
#                 width = 1,
#                 color = 'DarkSlateGray'
#             )
#         )
#     )
# )
# fig.show()


# df = px.data.gapminder()
# app = Dash()
# top_country = df.groupby('country')['pop'].sum().idxmax()
# top_country_df = df[df['country'] == top_country]
# print(top_country_df)
#
# fig = go.Figure()
#
# app.layout = html.Div([
#     dcc.Loading(dcc.Graph(id='main-graph'), type='cube'),
#     dag.AgGrid(
#         id='optimized-table',
#         rowData=df.to_dict('records'),
#         columnDefs=[{'field': i} for i in df.columns],
#         dashGridOptions={'pagination': True, 'paginationPageSize': 10},
#         style={'height': '400px', 'width': '100%'}
#     ),
#     dcc.Graph(figure=fig, config={'displayModeBar': False})
# ])
#
# @callback(
#     Output(component_id='main-graph', component_property='figure'),
#     Input(component_id='main-graph', component_property='value')
# )
# def update_dash(col):
#     px.scatter_geo(
#         df,
#         locations=col,
#         hover_data=('country', 'pop')
#     )
#
#     px.choropleth()
#
# if __name__ == '__main__':
#     app.run(debug=True)


df = px.data.gapminder()
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = Dash(__name__, external_stylesheets=external_stylesheets)

years = sorted(df['year'].unique())

column_defs = [
    {'field': 'country', 'filter': True},
    {'field': 'continent', 'filter': True},
    {'field': 'year'},
    {'field': 'pop', 'valueFormatter': {"function": "d3.format(',.0f')(params.value)"}},
    {'field': 'gdpPercap', 'valueFormatter': {"function": "d3.format('$,.2f')(params.value)"}}
]

app.layout = html.Div([
    html.H2(children='optimized World Data Dashboard'),

    html.Div([
        html.Label("Select Metric:"),
        dcc.Dropdown(
            id='metric-choice',
            options=[{'label': i, 'value': i} for i in ['pop', 'lifeExp', 'gdpPercap']],
            value='pop',
            style={'width': '40%'}
        ),
    ], style={'width': '40%', 'padding-bottom': '20px'}),

    dcc.Loading(
        id='loading-1',
        type='cube',
        children=dcc.Graph(id='main-graph', config={'displayModeBar': 'hover', 'scrollZoom': True, 'responsive': True})
    ),
    html.Div([
        html.Label("Select year:"),
        dcc.Slider(
            min=min(df['year']),
            max=max(df['year']),
            step=None,
            value=min(df['year']),
            id='year-slider',
            marks={int(year): str(year) for year in years}
        ),
    ], style={'padding': '40px'}),

    html.Div(id='output-container-range-slider', style={'textAlign': 'center', 'fontSize': '20px'}),

    html.Div([
        html.H3('Data Explorer (Virtual Table)'),
        dag.AgGrid(
            id='optimized-table',
            rowData=df.to_dict('records'),
            columnDefs=column_defs,
            dashGridOptions={'pagination': True, 'paginationPageSize': 10},
            style={'height': '400px', 'width': '100%'}
        )
    ], style={'padding': '20px'})
])

@callback(
    Output(component_id='main-graph', component_property='figure'),
    Output(component_id='output-container-range-slider', component_property='children'),
    Input(component_id='metric-choice', component_property='value'),
    Input(component_id='year-slider', component_property='value')
)
def update_dash(col, selected_year):
    filtered_df = df[df['year'] == selected_year]

    fig = px.scatter_geo(
        filtered_df,
        locations='iso_alpha',
        color=col,
        size=col,
        hover_name='country',
        projection='orthographic',
        title=f'Global {col} Distribution - {selected_year} year'
    )

    fig.update_layout(template='plotly_dark', margin={'t': 50, 'r': 0, 'b': 0, 'l': 0})

    status_text = f"Selected year: {selected_year}"

    return fig, status_text

if __name__ == '__main__':
    app.run(debug=True)