import time

import numpy as np
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc

from dash import Dash, html, Output, Input, dcc, callback, dash_table


#Init dataframe, app
df = px.data.gapminder()
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "Analytical Dashboard"

years = sorted(df['year'].unique())
last_year = df['year'].max()

#preliminary data cleaning
class CleanData:
    def drop_duplicates(self, df: pd.DataFrame) -> pd.DataFrame:
        return df.drop_duplicates(ignore_index=True)

    def data_typing(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.copy()
        for col in df.columns:
            #Num
            if np.issubdtype(df[col], np.number):
                num_conv = pd.to_numeric(arg=df[col], errors='coerce')
                if num_conv.notna().mean() > 0.7:
                    df[col] = num_conv
                    continue
            #Date
            if np.issubdtype(df[col], np.datetime64):
                date_conv = pd.to_datetime(arg=df[col], format='%Y-%d-%m')
                if date_conv.notna().mean() > 0.7:
                    df[col] = date_conv
                    continue
            #Str
            if np.issubdtype(df[col], 'object'):
                num_unique = df[col].nunique()
                num_total = len(df)
                if num_unique / num_total < 0.5:
                    df[col] = df[col].astype('object')
                    continue
        return df

    def down_casting(self, df: pd.DataFrame) -> pd.DataFrame:
        for col in df.select_dtypes(np.number).columns:
            df[col] = pd.to_numeric(arg=df[col], errors='coerce', downcast='integer' if 'int' in str(df[col].dtype) else 'float')
        return df

    def missing_value(self, df: pd.DataFrame) -> pd.DataFrame:
        for col in df.select_dtypes(np.number).columns:
            df[col] = df[col].fillna(df[col].median())
        for col in df.select_dtypes(['object', 'category']).columns:
            mode_series = df[col].mode()
            if not mode_series:
                df[col] = df[col].fillna(mode_series[0])
        for col in df.select_dtypes([np.datetime64, 'datetimetz']).columns:
            df[col] = df[col].fillna().bfill()
        return df

    def iqr(self) -> pd.DataFrame:
        pass

    def z_score(self) -> pd.DataFrame:
        pass

    def pipeline(self, df: pd.DataFrame):
        print("Data is being analyze...")
        df = (df.pipe(self.drop_duplicates)
              .pipe(self.data_typing)
              .pipe(self.missing_value)
              .pipe(self.down_casting)
              )
        return df

columns_defs = [
    {'field': 'continent', 'filter': True},
    {'field': 'country', 'filter': True},
    {'field': 'pop', 'valueFormatter': {"function": "d3.format(',.0f')(params.value)"}},
    {'field': 'gdpPercap', 'valueFormatter': {"function": "d3.format('$,.2f')(params.value)"}},
    {'field': 'expLife', 'valueFormatter': {"function": "d3.format('$,.2f')(params.value)"}}
]

app.layout = html.Div(
    style={'padding': '20px', 'fontFamily': 'Arial, sans-serif', 'backgroundColor': 'f9f9f9'},
    children=[
        html.H1('Data Interactive Analyze (Gapminder 2007)', style={
            'textAlign': 'center',
            'padding': '20px',
            'color': '#2c43e50'
        }),
        html.Div(
            style={'display': 'flex', 'justifyContent': 'space-around', 'marginBottom': '30px'},
            children=[
                html.Div(style={
                    'backgroundColor': '#ffffff',
                    'padding': '20px',
                    'borderRadius': '8px',
                    'textAlign': 'center',
                    'flex': '1'
                },
                children=[html.H3('Total countries in the database', style={'color': '#7f8c8d', 'margin': '0'}),
                          html.H2(f"{df['country'].nunique()}", style={
                              'color': '#2980b9',
                              'margin': '10px 0 0 0'
                          })]
                ),
                html.Div(style={
                    'backgroundColor': '#ffffff',
                    'padding': '20px',
                    'borderRadius': '8px',
                    'textAlign': 'center',
                    'flex': '1'
                },
                    children=[html.H3('Unique continents', style={'color': '#7f8c8d', 'margin': '0'}),
                              html.H2(f"{df['continent'].nunique()}", style={
                                  'color': '#27ae60',
                                  'margin': '10px 0 0 0'
                              })]
                ),
                html.Div(style={
                    'padding': '20px',
                    'backgroundColor': '#fff',
                    'borderRadius': '8px',
                    'textAlign': 'center',
                    'flex': '1'
                },
                    children=[html.H3("Latest Year", style={'color': '#7f8c8d', 'margin': '0'}),
                              html.H2(f"{last_year}", style={'color': '#67e22', 'margin': '10px 0 0 0'})
                    ])
            ]),

        html.Div(style={
            'backgroundColor': '#fff',
            'padding': '20px',
            'borderRadius': '8px',
            'textAlign': 'center',
            'flex': 1,
            'marginBottom': '30px'
        }, children=[
            html.Label("Select a continent for filter", style={
                'fontSize': '24px',
                'fontFamily': 'Arial, sans-serif',
                'fontWeight': 'semi-bold'}),
            dcc.Dropdown(
                id='continent-dropdown',
                options=[{'label': i, 'value': i} for i in df['continent'].unique()],
                value='Europe',
                clearable=False,
                style={'width': '50%', 'marginTop': '10px', 'marginBottom': '20px', 'margin': '0 auto'}
            ),
            dcc.Loading(
                id='loading-graph',
                type='cube',
                color='#2980b9',
                children=[
                    dcc.Graph(figure={}, id='life-exp-graph'),
                ]
            )
        ]),

        html.Div(style={
            'backgroundColor': '#fff',
            'flex': '1',
            'textAlign': 'center',
            'padding': '20px',
            'borderRadius': '8px'
        }, children=[
            html.H3('Pivot table', style={'color': '#2c3e50', 'marginTop': '0'}),
            dash_table.DataTable(
                id='data-table',
                columns=[{'name': i, 'id': i} for i in df.columns],
                page_size=10,
                style_table={'overflowX': 'auto'},
                style_cell={'textAlign': 'left', 'padding': '10px', 'fontFamily': 'Arial, sans-serif'},
                style_header={'backgroundColor': '#ecf0f1', 'fontWeight': 'bold', 'color': '#2c3e50'}
            )
        ])
    ])
#Layout

@app.callback(
    Output('life-exp-graph', 'figure'),
    Output('data-table', 'data'),
    Input('continent-dropdown', 'value')
)

def update_dash(selected_continent):
    time.sleep(2)
    filtered_df = df[df['continent'] == selected_continent]
    fig = px.line(
        filtered_df,
        x='year',
        y='lifeExp',
        color='country',
        title=f'Life Expectancy Dynamic: {selected_continent}',
        labels={'year': 'Year', 'lifeExp': 'Life Expectancy', 'country': 'Country', 'continent': 'Continent'}
    )
    fig.update_layout(transition_duration=500)
    table_data = filtered_df.to_dict('records')
    return fig, table_data

if __name__ == '__main__':
    app.run(debug=True, port=8080)