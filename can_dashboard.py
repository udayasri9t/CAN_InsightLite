import dash
from dash import dcc, html
from dash.dependencies import Output, Input
import dash_bootstrap_components as dbc
import plotly.graph_objs as go
import random
import time
from collections import deque

# Simulated CAN message generator
def generate_can_message():
    return {
        'timestamp': time.time(),
        'can_id': hex(random.choice([0x101, 0x102, 0x103, 0x104])),
        'data': [random.randint(0, 255) for _ in range(8)]
    }

# Initialize Dash App with Bootstrap
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "CAN Insight Lite"

# Data stores
speed_data = deque(maxlen=30)
time_data = deque(maxlen=30)

# Layout
app.layout = dbc.Container(fluid=True, children=[
    html.H1("CAN Insight Lite Dashboard", 
        style={
            "textAlign": "center",
            "color": "#0056b3",
            "fontWeight": "bold",
            "fontSize": "3rem",
            "marginTop": "30px",
            "marginBottom": "30px",
            "textShadow": "1px 1px 2px lightgray"
        }),

    dbc.Row([
        dbc.Col(dbc.Card([
            dbc.CardHeader("Speed (km/h)"),
            dbc.CardBody(html.H4(id="speed-display", className="card-title"))
        ], color="light", inverse=False), width=3),

        dbc.Col(dbc.Card([
            dbc.CardHeader("RPM"),
            dbc.CardBody(html.H4(id="rpm-display", className="card-title"))
        ], color="light", inverse=False), width=3),

        dbc.Col(dbc.Card([
            dbc.CardHeader("Temperature (°C)"),
            dbc.CardBody(html.H4(id="temp-display", className="card-title"))
        ], color="light", inverse=False), width=3),

        dbc.Col(dbc.Card([
            dbc.CardHeader("Brake Status"),
            dbc.CardBody(html.H4(id="brake-display", className="card-title"))
        ], color="light", inverse=False), width=3),
    ], className="mb-4"),

    dcc.Graph(id='speed-graph', config={'displayModeBar': False}),
    
    dcc.Interval(id='interval-component', interval=1000, n_intervals=0)  # every 1 sec
])

# Callbacks
@app.callback(
    [Output("speed-display", "children"),
     Output("rpm-display", "children"),
     Output("temp-display", "children"),
     Output("brake-display", "children"),
     Output("speed-graph", "figure")],
    Input("interval-component", "n_intervals")
)
def update_dashboard(n):
    msg = generate_can_message()
    speed = msg['data'][0]
    rpm = msg['data'][1] * 30
    temp = msg['data'][2]
    brake = "ON" if msg['data'][3] > 127 else "OFF"

    speed_data.append(speed)
    time_data.append(time.strftime("%H:%M:%S"))

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=list(time_data), y=list(speed_data),
                             mode='lines+markers', name='Speed',
                             line=dict(color='royalblue', width=3)))
    fig.update_layout(title="Speed Over Time", xaxis_title="Time", yaxis_title="Speed (km/h)",
                      template="plotly_white")

    return f"{speed} km/h", f"{rpm} RPM", f"{temp} °C", brake, fig

# Run
if __name__ == "__main__":
    app.run(debug=True)
