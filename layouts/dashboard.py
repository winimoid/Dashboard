import lorem_text
from dash import html, dcc
import dash_bootstrap_components as dbc
from plotly import graph_objects as go
from dash import callback, Input, Output
from dash import dash_table as table
from lorem_text import lorem

figureCard = dcc.Graph(figure=go.Figure(data=[go.Bar(x=[1, 2, 3], y=[4, 5, 6])]),
                       style={"width": "100%"}),

chiffresCard = dbc.Col(
    children=[
        dbc.Row(
            children=[
                dbc.Card(
                    children=[
                        dbc.CardHeader("Maximum"),
                        dbc.CardBody(
                            children=[
                                html.H4("75Mbps", className="card-title"),
                                html.P("Le lorem ipsum sit amet...", className="card-text")
                            ]
                        )
                    ],
                    style={"margin": "5px"}
                ),

            ]
        ),

        dbc.Row(
            children=[
                dbc.Card(
                    children=[
                        dbc.CardHeader("Minimum"),
                        dbc.CardBody(
                            children=[
                                html.H4("10Mbps", className="card-title"),
                                html.P("Le lorem ipsum sit amet...", className="card-text")
                            ]
                        )
                    ],
                    style={"margin": "5px"}
                )
            ]
        ),

        dbc.Row(
            children=[
                dbc.Card(
                    children=[
                        dbc.CardHeader("Débit Moyen"),
                        dbc.CardBody(
                            children=[
                                html.H4("34Mbps", className="card-title"),
                                html.P("Le lorem ipsum sit amet...", className="card-text")
                            ]
                        )
                    ],
                    style={"margin": "5px"}
                )
            ]
        )
    ],
    width="auto"
)
# color="#f4f6f9",
# style={"display": "content"}
# outline=True

body = dbc.Container(
    children=[
        html.Div(children=[
            # A card with a graph
            html.H3("Prédiction du Traffic Réseau"),

            html.Div(children=[
                dbc.Row(
                    children=[
                        dbc.CardGroup(
                            children=[
                                dbc.Col(
                                    children=[
                                        dcc.Graph(figure=go.Figure(data=[go.Bar(x=[1, 2, 3], y=[4, 5, 6])]),
                                                  style={"width": "100%"}),
                                        # figureCard
                                    ],
                                    style={"width": "80%", "margin": "1%", "flex": "60%"},
                                ),

                                dbc.Col(
                                    children=[
                                        chiffresCard
                                    ],
                                    style={"width": "20%", "text-align": "center", "margin": "1%"},
                                )
                            ],
                            style={"display": "flex"}
                        )
                    ]
                )
            ]),

            # Diagrams
            html.Div(
                children=[
                    html.H3("Diagrammes"),

                    dbc.Row(
                        children=[
                            dbc.Col(
                                children=[
                                    html.H4("Diagramme de Gantz"),
                                    dcc.Graph(figure=go.Figure(data=[go.Bar(x=[1, 2, 3], y=[4, 5, 6])]),
                                              style={"width": "100%"}),
                                ]
                            ),

                            dbc.Col(
                                children=[
                                    html.H4("Diagramme de Wini"),
                                    dcc.Graph(figure=go.Figure(data=[go.Bar(x=[1, 8, 3], y=[9, 5, 6])]),
                                              style={"width": "100%"}),
                                ]
                            ),

                            dbc.Col(
                                children=[
                                    html.H4("Conseils"),
                                    dbc.Card(
                                        children=[
                                            dbc.CardHeader("Conseils"),
                                            dbc.CardBody(
                                                children=[
                                                    html.P("Le lorem ipsum sit amet...", className="card-text")
                                                ]
                                            )
                                        ],
                                        style={"margin": "5px"}
                                    ),
                                ]
                            )
                        ]
                    )
                ]
            ),

            # A table with data
            html.Div(children=[
                html.H3("Tableau"),
                table.DataTable(data=[
                    {"Name": "John Doe", "Age": 30},
                    {"Name": "Jane Doe", "Age": 25}
                ])
            ]),
            # A button
            html.Div(children=[
                html.Button("Lancer une action", id="button", n_clicks=0),
                html.Div(id="output")
            ])
        ])
    ]
)

layout_dashboard = html.Div(
    children=[body],
    style={'background-image': 'url("/assets/bg.jpg")'}
)

# Define the callback function for the button
# @callback(
#     Output("output", "children"),
#     Input("button", "n_clicks")
# )
# def update_output(n_clicks):
#     # Update the output with the number of clicks
#     return f"Nombre de clics : {n_clicks}"
