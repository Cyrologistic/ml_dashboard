import dash
from dash import dcc
from dash import html
import plotly.io as pio

# create Dash app
app = dash.Dash(__name__)

eda = pio.read_json('eda.json')

logistic_cm = "Logistic Regression_confusion_matrix.png"
logistic_src = app.get_asset_url(logistic_cm)
logistic_image = html.Img(src=logistic_src)

decision_cm = "Decision Tree_confusion_matrix.png"
decision_src = app.get_asset_url(decision_cm)
decision_image = html.Img(src=decision_src)

xgb_cm = "XGBoost_confusion_matrix.png"
xgb_src = app.get_asset_url(xgb_cm)
xgb_image = html.Img(src=xgb_src)

feature_impotance = "feature_importance.png"
feature_src = app.get_asset_url(feature_impotance)
feature_image = html.Img(src=feature_src)

lime = "lime.png"
lime_src = app.get_asset_url(lime)
lime_image = html.Img(src=lime_src)

learning_curve = "learning_curve.png"
learning_src = app.get_asset_url(learning_curve)
learning_image = html.Img(src=learning_src)

# define app layout
app.layout = html.Div([
    html.H1('My Dashboard'),
    dcc.Graph(figure=eda),
    html.Div([logistic_image]),
    html.Div([decision_image]),
    html.Div([xgb_image]),
    html.Div([feature_image]),
    html.Div([lime_image]),
    html.Div([learning_image])
])

# run the app
if __name__ == '__main__':
    app.run_server(debug=True)