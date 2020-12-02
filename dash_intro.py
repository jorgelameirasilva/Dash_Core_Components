import dash
import dash_core_components as dcc 
import dash_html_components as html 
import plotly.express as px


dash  = dash.Dash()

fig = px.line(x=[0,1,2], y=[2,3,4])


dash.layout  = html.Div([
    #dropdown
    dcc.Dropdown(id="my-dropdown", 
                options = [
                    {"label": "France", "value":"France"},
                    {"label": "England", "value":"England"},
                    {"label": "Portugal", "value":"Portugal"},
                ], 
                multi=True, 
                placeholder = "Pick you favorite country"),

    #Radio Items
    dcc.RadioItems(
        id="radio", 
        options = [
    {"label": "France", "value":"France"},
    {"label": "England", "value":"England"},
    {"label": "Portugal", "value":"Portugal"},
]
    ),
    #Graph
    dcc.Graph(figure= fig)

])


dash.run_server(debug=True)