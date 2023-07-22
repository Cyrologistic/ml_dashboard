import dash
from dash import dcc
from dash import html
import plotly.io as pio
import flask

non_categorical = ['Year_Birth','Income', 'Dt_Customer', 'Recency','MntWines','MntFruits','MntMeatProducts',
                   'MntFishProducts','MntSweetProducts','MntGoldProds','NumDealsPurchases',
                   'NumWebPurchases','NumCatalogPurchases','NumStorePurchases','NumWebVisitsMonth']

server = flask.Flask(__name__)
app = dash.Dash(__name__, server=server)

year_birth = pio.read_json('Year_Birth.json')
income = pio.read_json('Income.json')
dt_Customer = pio.read_json('Dt_Customer.json')
recency = pio.read_json('Recency.json')
mntwines = pio.read_json('MntWines.json')
mntfruits = pio.read_json('MntFruits.json')
mntmeatproducts = pio.read_json('MntMeatProducts.json')
mntfishproducts = pio.read_json('MntFishProducts.json')
mntsweetproducts = pio.read_json('MntSweetProducts.json')
mntgoldprods = pio.read_json('MntGoldProds.json')
numdealpurchases = pio.read_json('NumDealsPurchases.json')
numwebpurchases = pio.read_json('NumWebPurchases.json')
numcatalogpurchases = pio.read_json('NumCatalogPurchases.json')
numstorepurchases = pio.read_json('NumStorePurchases.json')
numwebvisitsmonth = pio.read_json('NumWebVisitsMonth.json')


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

learning_curve = "Learning_Curve.png"
learning_src = app.get_asset_url(learning_curve)
learning_image = html.Img(src=learning_src)

# define app layout
app.layout = html.Div([
    html.H1('ML Dashboard'),
    html.H2('Exploratory Data Analysis'),
    dcc.Graph(figure=year_birth),
    dcc.Graph(figure=income),
    dcc.Graph(figure=dt_Customer),
    dcc.Graph(figure=recency),
    dcc.Graph(figure=mntwines),
    dcc.Graph(figure=mntfruits),
    dcc.Graph(figure=mntmeatproducts),
    dcc.Graph(figure=mntfishproducts),
    dcc.Graph(figure=mntsweetproducts),
    dcc.Graph(figure=mntgoldprods),
    dcc.Graph(figure=numdealpurchases),
    dcc.Graph(figure=numwebpurchases),
    dcc.Graph(figure=numcatalogpurchases),
    dcc.Graph(figure=numstorepurchases),
    dcc.Graph(figure=numwebvisitsmonth),
    html.H2('Model Evaluation'),
    html.Div(
        style={
        'text-align': 'center',
        'margin': 'auto'
        },
        children = [logistic_image]),
    html.Div(
        style={
        'text-align': 'center',
        'margin': 'auto'
        },
        children = [decision_image]),
    html.Div(
        style={
        'text-align': 'center',
        'margin': 'auto'
        },
        children = [xgb_image]),
    html.H2('Model Insights'),
    html.Div(
        style={
        'text-align': 'center',
        'margin': 'auto'
        },
        children = [feature_image]),
    html.Div(
        style={
        'text-align': 'center',
        'margin': 'auto'
        },
        children = [lime_image]),
    html.Div(
        style={
        'text-align': 'center',
        'margin': 'auto'
        },
        children = [learning_image])
])

# run the app
if __name__ == '__main__':
    app.run_server(debug=True)
