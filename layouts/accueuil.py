from dash import html, dcc
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from lorem_text import lorem

body = dbc.Container(
    children=[
        html.Div(
            children=[
                html.Br([]),
                html.H5("Bienvenue !", style={'color': '#03afd2', 'font-size': '24px', 'font-family': 'verdana'}),
                html.Br([]),
                lorem.paragraph(),
                html.Br([]),

                html.Br([]),

                dmc.Button(
                    children=[
                        html.H3("Tableau de bord =>")
                    ],
                    color="primary",
                    size="lg",
                    id="button"
                ),

            ]
        )
    ]
)

layout_acceuil = html.Div(
    children=[body],
    style={'background-image': 'url("/assets/bg.jpg")'}
)
