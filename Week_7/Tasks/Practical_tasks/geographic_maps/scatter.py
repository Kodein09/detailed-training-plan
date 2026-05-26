import plotly.express as px
import pandas as pd
import numpy as np
import plotly.graph_objects as go

df = pd.DataFrame({
    'lat': [37.77, 37.8],
    'lon': [-122.4, -122.5],
    'val': [1,2]
})

fig = px.scatter_map(
    df,
    lat=df['lat'],
    lon=df['lon'],
    color='val',
    zoom=10,
    map_style='open-street-map'
)
fig.update_layout(title='Plotly Scatter Map - Express')
fig.show()


fig = go.Figure(go.Scattermap(
    lon=[138.6534, 104.3475, 128.0462, 7.4210, -19.0426],
    lat=[36.4867, 34.4354, 36.3589, 43.7335, 65.0475],
    mode='lines+markers',
    marker=go.scattermap.Marker(
        size=14,
        color=['pink', 'red', 'steelblue', 'maroon', 'skyblue']
    ),
    text=['Japan', 'China', 'South Korea', 'Monaco', 'Iceland']
))
fig.update_layout(
    hovermode='closest',
    map=dict(
        bearing=0,
        center=go.layout.map.Center(
            lat=43.4000,
            lon=7.500
        ),
        pitch=20,
        zoom=4
    )
)
fig.show()