# clickstream_dashboard.py
import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px

# Load data
product_df = pd.read_csv("product_clicks.csv", parse_dates=['timestamp'])
checkout_df = pd.read_csv("checkout_clicks.csv", parse_dates=['timestamp'])

# Preprocessing
product_df['hour'] = product_df['timestamp'].dt.hour
checkout_df['hour'] = checkout_df['timestamp'].dt.hour

# Aggregations
product_actions = product_df.groupby(['action']).size().reset_index(name='count')
checkout_actions = checkout_df.groupby(['action']).size().reset_index(name='count')

clicks_per_hour = pd.concat([
    product_df.groupby('hour').size().reset_index(name='clicks').assign(type='Product'),
    checkout_df.groupby('hour').size().reset_index(name='clicks').assign(type='Checkout')
])

# Create Dash app
app = dash.Dash(__name__)
app.title = "Clickstream Dashboard"

app.layout = html.Div([
    html.H1("E-commerce Clickstream Analytics", style={'textAlign': 'center'}),

    html.Div([
        html.Div([
            html.H3("Product Page Actions"),
            dcc.Graph(figure=px.bar(product_actions, x='action', y='count', color='action', title="Actions on Product Pages"))
        ], className="six columns"),

        html.Div([
            html.H3("Checkout Actions"),
            dcc.Graph(figure=px.pie(checkout_actions, values='count', names='action', title="Actions During Checkout"))
        ], className="six columns"),
    ], className="row"),

    html.Div([
        html.H3("Click Volume Per Hour"),
        dcc.Graph(figure=px.line(clicks_per_hour, x='hour', y='clicks', color='type', markers=True,
                                 title="Hourly Click Activity - Product vs Checkout"))
    ])
])

if __name__ == '__main__':
    app.run(debug=True)
