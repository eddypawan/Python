import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px

# Load data into a pandas DataFrame
#df = pd.read_csv('data.csv')
df = pd.read_csv('G:\Python\pythonRepo\Python\Files\sample.csv', encoding='iso-8859-1')

# Initialize the Plotly Dash app
app = dash.Dash(__name__)

# Set the layout of the app
app.layout = html.Div([
    dcc.Graph(id='graph'),
    dcc.Slider(
        id='x-slider',
        min=df['x'].min(),
        max=df['x'].max(),
        value=df['x'].min(),
        marks={str(x): str(x) for x in df['x'].unique()}
    )
])

# Define the callback function that updates the scatter plot based on the slider value
@app.callback(
    dash.dependencies.Output('graph', 'figure'),
    [dash.dependencies.Input('x-slider', 'value')])
def update_figure(selected_x):
    filtered_df = df[df['x'] == selected_x]
    fig = px.scatter(filtered_df, x='x', y='y')
    return fig

# Start the app
if __name__ == '__main__':
    app.run_server(debug=True)
