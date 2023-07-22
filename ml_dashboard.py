import dash
from dash import dcc
from dash import html
import plotly.io as pio

# create Dash app
app = dash.Dash(__name__)

fig1 = pio.read_json('eda.json')

# define app layout
app.layout = html.Div([
    html.H1('My Dashboard'),
    dcc.Graph(figure=fig1),
    html.Img(src='Logistic Regression_confusion_matrix.png'),
    html.Img(src='Decision Tree_confusion_matrix.png'),
    html.Img(src='XGBoost_confusion_matrix.png'),
    html.Img(src='feature_importance.png'),
    html.Img(src='lime.png'),
    html.Img(src='Learning_Curve.png'),
])

# run the app
if __name__ == '__main__':
    app.run_server(debug=True)