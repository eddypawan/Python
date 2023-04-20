import pandas as pd
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html

# Load volcano data
volcano_data = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/volcano_db.csv", encoding='iso-8859-1')
#volcano_data = pd.read_csv('G:\Python\pythonRepo\Python\Files\volcano_db.csv', encoding='iso-8859-1')

# Create app
app = dash.Dash(__name__)

# Define app layout
app.layout = html.Div([
    dcc.Graph(
        id='volcano-map',
        figure={
            'data': [
                {'type': 'scattergeo',
                 'lat': volcano_data['Latitude'],
                 'lon': volcano_data['Longitude'],
                 'mode': 'markers',
                 'marker': {'size': 10, 'color': 'red'}
                }
            ],
            'layout': {
                'geo': {
                    'center': {'lat': 0, 'lon': 0},
                    'projection': {'type': 'natural earth'},
                    'scope': 'world'
                },
                'margin': {'l': 0, 'r': 0, 't': 0, 'b': 0}
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
