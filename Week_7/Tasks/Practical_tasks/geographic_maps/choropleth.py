from urllib.request import urlopen

import json
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 1000)

try:
    with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
        counties = json.load(response)
except Exception as e:
    print(f"Can't download file GeoJSON: {e}")

for feat in counties['features']:
    print(feat)

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/fips-unemp-16.csv",
                 dtype={"fips": str})
print(df.head())

fig = px.choropleth(
    data_frame=df,
    geojson=counties,
    locations='fips',
    color='unemp',
    color_continuous_scale='Viridis',
    range_color=[0, 20],
    scope='usa',
    labels={"unemp": "unemployment rate"},
    title="Plotly Choropleth Char - Express"
)
fig.update_layout(
    title="Безработица в США по округам",
    margin={"r": 0, "t": 40, "l": 0, "b": 0})
fig.show()


df = px.data.election()
geojson = px.data.election_geojson()
print(geojson)
print(df.head())

fig = px.choropleth(
    data_frame=df,
    geojson=geojson,
    color='winner',
    locations='district',
    featureidkey="properties.district",
    projection='orthographic',
    hover_data=['Bergeron', 'Joly', 'Coderre']
)

fig.update_geos(fitbounds='locations', visible=True)
fig.update_layout(title="Political candidate voting pool analysis",margin={"r": 0, "t": 50,"l": 0,"b": 50})
fig.show()

fig = go.Figure(go.Scattergeo())
fig.update_geos(
    resolution=50,
    showcoastlines=True, coastlinecolor="RebeccaPurple",
    showocean=True, oceancolor='LightBlue',
    showlakes=True, lakecolor='Blue',
    showrivers=True, rivercolor='Blue',
    showland=True, landcolor='LightGreen',
    projection_type='orthographic',
    showcountries=True
)
fig.show()

fig = go.Figure(go.Scattergeo())
fig.update_geos(
    visible=False, resolution=110,
    showcountries=True, countrycolor="RebeccaPurple",
    projection_type='orthographic', bgcolor='black'
)
fig.update_layout(paper_bgcolor='black')
fig.show()

fig = go.Figure(go.Scattergeo())
fig.update_geos(projection_type='orthographic', bgcolor='black')
fig.update_layout(paper_bgcolor='black')
fig.show()

fig = go.Figure(go.Choropleth(
    locations=['TX', 'NY', 'CA', 'LA'],
    z=[1, 2, 3, 4],
    locationmode='USA-states',
    colorscale='Viridis',
))
fig.update_geos(projection_type='orthographic')
fig.update_layout(title_text="Example Choropleth (States)")
fig.show()

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_world_gdp_with_codes.csv')

fig = go.Figure(go.Choropleth(
    locations=df['CODE'],
    z=df['GDP (BILLIONS)'],
    text=df['COUNTRY'],
    colorscale='Blues',
    autocolorscale=False,
    reversescale=False,
    marker_line_color='darkgray',
    marker_line_width=0.5,
    colorbar_tickprefix='$',
    colorbar_title='DGP<br>BILLIONS US$'
))

fig.update_layout(
    title_text='2014 Global GDP',
    geo=dict(
        showframe=True,
        showcoastlines=False,
        projection_type='orthographic'
    ),
    annotations = [dict(
        x=0.55,
        y=0.1,
        xref='paper',
        yref='paper',
        text='Source: <a href="https://www.cia.gov/library/publications/the-world-factbook/fields/2195.html">\
            CIA World Factbook</a>',
        showarrow=False
    )]
)
fig.show()

df = px.data.gapminder()
map_data = df[df['year'] == df['year'].max()]
fig = make_subplots(
    rows=2, cols=1,
    subplot_titles="ВВП на душу населения по странам",
    row_heights=[0.7, 0.3], #Высота графиков строк
    vertical_spacing=0.1, #Расстояние между графиками по вертикали
    specs=[
        [{'type': 'geo'}], #Верхний подграфик для совместимости - географический
        [{'type': 'xy'}] #Нижний подграфик обычный XY
    ],
)
choropleth = px.choropleth(
    map_data,
    locations='iso_alpha', #Сопоставление полигонов на карте и данных
    color='gdpPercap',
    hover_name='country',
    hover_data={'gdpPercap': ':.0f', 'pop': ':.1M'},
    color_continuous_scale='Plasma',
    range_color=[1000, 60000],
    projection='orthographic'
)
for trace in choropleth.data:
    fig.add_trace(trace, row=1, col=1)
fig.update_geos(
    showcoastlines=True, coastlinecolor='LightGrey',
    showland=True, landcolor='LightGrey',
    showocean=True, oceancolor='LightBlue',
    showcountries=True, countrycolor='DarkGrey',
    showrivers=True, rivercolor='Blue',
    showlakes=True, lakecolor='Blue',
    projection_type='orthographic',
    lataxis_showgrid=False, lonaxis_showgrid=False #Отключение сетки по широте и долготе
)

top_countries = df.groupby('country')['pop'].max().nlargest(5).index
line_data = df[df['country'].isin(top_countries)]
line_plot = px.line(
    line_data,
    x='year',
    y='gdpPercap',
    color='country',
    hover_data={'pop': ':.1M'}
)
for trace in line_plot.data:
    fig.add_trace(trace, row=2, col=1)
fig.update_layout(
    height=800,
    title_text='Анализ ВВП на душу населения: пространственное и временное население',
    showlegend=True,
    legend=dict(
        orientation='h',
        yanchor='bottom',
        y=-0.15,
        xanchor='center',
        x=0.5
    ),
    margin=dict(l=50, b=80)
)
fig.update_xaxes(title_text='Update xaxes (title_text)')
fig.update_yaxes(title_text='Update yaxes (title_text)')
fig.show()