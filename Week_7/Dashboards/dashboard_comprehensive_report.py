# import matplotlib.pyplot as plt
#
# numerator = 2
# denominator = 4
#
# remaining = denominator - numerator
#
# slices = [numerator, remaining]
# labels = [f'Доля {numerator}/{denominator}', 'Остаток']
# colors = ['maroon', 'steelblue']
#
# plt.figure(figsize=(6,6))
# plt.pie(
#     x=slices,
#     labels=labels,
#     colors=colors,
#     autopct='%1.1f%%',
#     startangle=90
# )
# plt.title(f"Визуализация дроби {numerator}/{denominator}")
# plt.show()



# from dash import Dash, html, Input, Output, dcc, callback
# import plotly.express as px
# import pandas as pd
#
# df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')
#
# app = Dash()
#
# app.layout = [
#     html.H1(children='Title of Dash App', style={'textAlign': 'center'}),
#     dcc.Dropdown(df.country.unique(), 'Canada', id='dropdown-selection'),
#     dcc.Graph(id='graph-content')
# ]
#
# @callback(
#     Output('graph-content', 'figure'),
#     Input('dropdown-selection', 'value'),
# )
# def update_graph(value):
#     dff = df[df.country==value]
#     return px.line(dff, x='year', y='pop')
#
# if __name__ == '__main__':
#     app.run(debug=True)



# from dash import Dash, html
#
# #Initialize the App
# app = Dash()
#
# #App layout
# app.layout = [html.Div(children='Hello World')]
#
# if __name__ == '__main__':
#     app.run(debug=True)


import plotly.express as px
from dash import Dash, html, dcc, callback, Output, Input
import dash_ag_grid as dag
import pandas as pd

# df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')
#
# app = Dash()
#
# app.layout = [
#     html.Div(children='My First App with Data'),
#     dag.AgGrid(
#         rowData=df.to_dict('records'),
#         columnDefs=[{'field': i} for i in df.columns]
#     )
# ]
#
# if __name__ == '__main__':
#     app.run(debug=True)

# df = px.data.iris()
# app = Dash()
# app.layout = [
#     html.H1("My own code for practice with iris DataFrame."),
#     dag.AgGrid(
#         rowData=df.to_dict('records'),
#         columnDefs=[{'field': i} for i in df.columns]
#     )
# ]
#
# if __name__ == '__main__':
#     app.run(debug=True)

# df = pd.DataFrame({
#     'stocks': ['APPL', 'TSLA', 'NVDA', 'AMD', 'INTL', 'MSFT'],
#     'price': [300, 440, 220, 430, 100, 410],
#     'year': [2026, 2026, 2026, 2026, 2026, 2026]
# })
#
# app = Dash()
#
# app.layout = [
#     html.H1(children='Popular stocks in 2026'),
#     dag.AgGrid(
#         rowData=df.to_dict('records'),
#         columnDefs=[{'field': i} for i in df.columns]
#     )
# ]
#
# if __name__ == '__main__':
#     app.run(debug=True)

# df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')
# app = Dash()
# app.layout = [
#     html.H1(children='Average LifeExp in different countries'),
#     dcc.Graph(figure=px.histogram(df, x='country', y='lifeExp', histfunc='avg')),
#     html.H1(children='Visualization GapMinder 2007 on Histogram'),
#     dag.AgGrid(
#         rowData=df.to_dict('records'),
#         columnDefs=[{'field': i} for i in df.columns]
#     ),
#     dcc.Graph(figure=px.bar(df, x='continent', y='pop', color='country', title='Populations in different Continents'))
# ]
# if __name__ == '__main__':
#     app.run(debug=True)


# df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')
# app = Dash()
# app.layout = [
#     html.H3(children='Bar Graph GapMinder 2007 - Express'),
#     dag.AgGrid(
#         rowData=df.to_dict('records'),
#         columnDefs=[{'field': i} for i in df.columns]
#     ),
#     dcc.Graph(figure=px.bar(df, x='continent', y='lifeExp'))
# ]
# if __name__ == '__main__':
#     app.run(debug=True)


# df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')
# app = Dash()
# app.layout = [
#     html.Div(
#         children='My First Graph with Controls (CallBack)',
#         style={
#             'color': 'maroon',
#             'borderColor': '#2c3e50',
#             'padding': '20px',
#             'textAlign': 'center',
#             'fontFamily': 'Arial, sans-serif',
#             'fontSize': '40px'
#         }),
#     html.Hr(),
#     dcc.RadioItems(options=['pop', 'lifeExp', 'gdpPercap'], value='pop', id='radio-item'),
#     dag.AgGrid(
#         rowData=df.to_dict('records'),
#         columnDefs=[{'field': i} for i in df.columns]
#     ),
#     html.Hr(style={
#         'BorderTop': '10px solid #ff4444',
#         'width': '100%',
#         'height': '5x',
#         'opacity': '1'
#     }),
#     dcc.Graph(figure={}, id='controls-and-graph')
# ]
#
# @callback(
#     Output(component_id='controls-and-graph', component_property='figure'),
#     Input(component_id='radio-item', component_property='value')
# )
# def update_graph(col_chosen):
#     fig = px.histogram(df, x='continent', y=col_chosen, histfunc='avg')
#     return fig
#
# if __name__ == '__main__':
#     app.run(debug=True)


#
# df = px.data.gapminder()
# print(df.columns)
# app = Dash()
#
# years = sorted(df['year'].unique())
#
# app.layout = html.Div([
#     html.Div(
#         children='World Map of GapMinder',
#         style={
#             'padding': '30px', 'color': 'white', 'backgroundColor': '#111111',
#             'fontSize': '40px', 'fontFamily': 'Arial, sans-serif', 'textAlign': 'center',
#             'border': '7px solid steelblue'
#         }
#     ),
#     dcc.RadioItems(
#         options=[
#             {'label': 'Population', 'value': 'pop'},
#             {'label': 'Life Exp', 'value': 'lifeExp'},
#             {'label': 'gdpPercap', 'value': 'gdpPercap'}
#         ],
#         value='pop',
#         id='choropleth-radio-item',
#         labelStyle={
#             'display': 'inline-block',
#             'padding': '5px',
#             'color': 'white'
#         },
#         style={
#             'padding': '10px',
#             'textAlign': 'center',
#             'backgroundColor': '#111111',
#             'fontFamily': 'Arial, sans-serif',
#             'fontSize': '16px',
#             'border': '6px solid steelblue'
#         }
#     ),
#     html.Div([
#         html.Label("Choose year:", style={'color': 'white'}),
#         dcc.Slider(
#             min=min(years),
#             max=max(years),
#             step=None,
#             marks={
#                 str(year): {
#                     'label': str(year),
#                     'style': {'color': 'maroon' if year in [1952, 2007] else 'white',
#                               'fontSize': '14px', 'fontFamily': 'Arial, sans-serif'}
#                 }
#                 for year in years
#             },
#             value=min(years),
#             id='global-year-slider'
#         )
#     ], style={'padding': '20px', 'backgroundColor': '#111111', 'color': 'white'}),
#
#     dcc.Graph(figure={}, id='choropleth-graph'),
#     dcc.Graph(figure={}, id='line-graph'),
#     dcc.Graph(figure={}, id='bar-graph'),
# ])
#
# @callback(
#     Output(component_id='choropleth-graph', component_property='figure'),
#     Output(component_id='line-graph', component_property='figure'),
#     Output(component_id='bar-graph', component_property='figure'),
#     Input(component_id='choropleth-radio-item', component_property='value'),
#     Input(component_id='global-year-slider', component_property='value')
# )
#
# def update_graph(col_chosen, year_chosen):
#     dff = df[df['year'] == year_chosen]
#
#     fig_map = px.choropleth(
#         dff,
#         locations='iso_alpha',
#         color=col_chosen,
#         title=f"{col_chosen} indicator on the world map in {year_chosen} years",
#         subtitle='Plotly Express Choropleth - gapminder 2007',
#         hover_name='country',
#         hover_data={col_chosen: True, 'iso_alpha': False},
#         color_continuous_scale='Plasma',
#         range_color=[1000, 60000],
#         projection='orthographic',
#     )
#     fig_map.update_geos(
#         showland=True, landcolor='lightGrey',
#         showrivers=True, rivercolor='blue',
#         showlakes=True, lakecolor='blue',
#         showcoastlines=True, coastlinecolor='Grey',
#         showocean=True, oceancolor='steelblue',
#         showcountries=True, countrycolor='DarkGrey',
#         projection_type='orthographic',
#         lataxis_showgrid=False, lonaxis_showgrid=False,
#         resolution=110
#     )
#     fig_map.update_layout(margin={'t': 50, 'r': 0, 'b': 50, 'l': 0}, template='plotly_dark')
#
#     fig_line = px.line(
#         dff,
#         x='country',
#         y=col_chosen,
#         title=f"Linear Graph {col_chosen}"
#     )
#     fig_line.update_layout(template='plotly_dark')
#
#     fig_bar = px.bar(
#         dff,
#         x='country',
#         y=col_chosen
#     )
#     fig_bar.update_layout(template='plotly_dark')
#
#     return fig_map, fig_line, fig_bar
#
# if __name__ == '__main__':
#     app.run(debug=True)