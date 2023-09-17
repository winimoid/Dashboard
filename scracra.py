import dash_mantine_components as dmc
from dash import Dash, html, dcc, Input, Output, State, callback, callback_context
from dash.exceptions import PreventUpdate
from dash_iconify import DashIconify

from layouts import accueuil, dashboard

# Initialize the app - incorporate a Dash Mantine theme
external_stylesheets = [dmc.theme.DEFAULT_COLORS]
app = Dash(__name__, external_stylesheets=external_stylesheets)


def get_icon(icon):
    return DashIconify(icon=icon, height=16, color="#c2c7d0")


myContent = html.Div(id='page-content')

app.layout = dmc.MantineProvider(
    theme={
        'fontFamily': '"Inter", sans-serif',
        "components": {
            "NavLink": {'styles': {'label': {'color': '#c2c7d0'}}}
        },
    },

    children=[
        dcc.Location(id='url', refresh=True),

        dmc.Container([
            dmc.Navbar(
                p="md",
                fixed=False,
                width={"base": 300},
                hidden=True,
                hiddenBreakpoint='md',
                position='right',
                height='100vh',
                id='sidebar',
                children=[
                    html.Div(
                        [
                            dmc.NavLink(
                                label="Accueuil",
                                icon=get_icon(icon="bi:house-door-fill"),
                            ),
                            dmc.NavLink(
                                label="Tableau de Bord",
                                icon=get_icon(icon="tabler:gauge"),
                            ),
                            dmc.NavLink(
                                opened=False,
                                label="With right section",
                                icon=get_icon(icon="tabler:gauge"),
                                rightSection=get_icon(icon="tabler-chevron-right"),
                            ),
                            dmc.NavLink(
                                label="Disabled",
                                icon=get_icon(icon="tabler:circle-off"),
                                disabled=True,
                            ),
                            dmc.NavLink(
                                label="With description",
                                description="Additional information",
                                icon=dmc.Badge(
                                    "3", size="xs", variant="filled", color="red", w=16, h=16, p=0
                                ),
                            ),
                            dmc.NavLink(
                                label="Active subtle",
                                icon=get_icon(icon="tabler:activity"),
                                rightSection=get_icon(icon="tabler-chevron-right"),
                                variant="subtle",
                                active=True,
                            ),
                        ],
                        style={'white-space': 'nowrap'},
                    )],
                style={'overflow': 'hidden', 'transition': 'width 0.3s ease-in-out', 'background-color': '#343a40'}
            ),
            dmc.Drawer(
                title="IDS Technologie - ALVANET",
                id="drawer-simple",
                padding="md",
                zIndex=10000,
                size=300,

                overlayOpacity=0.1,
                children=[
                    html.Div(
                        [
                            dmc.NavLink(
                                label="Accueuil",
                                icon=get_icon(icon="bi:house-door-fill"),
                            ),
                            dmc.NavLink(
                                label="Tableau de Bord",
                                icon=get_icon(icon="tabler:gauge"),
                            ),
                            dmc.NavLink(
                                opened=False,
                                label="With right section",
                                icon=get_icon(icon="tabler:gauge"),
                                rightSection=get_icon(icon="tabler-chevron-right"),
                            ),
                            dmc.NavLink(
                                label="Disabled",
                                icon=get_icon(icon="tabler:circle-off"),
                                disabled=True,
                            ),
                            dmc.NavLink(
                                label="With description",
                                description="Additional information",
                                icon=dmc.Badge(
                                    "3", size="xs", variant="filled", color="red", w=16, h=16, p=0
                                ),
                                style={
                                    'body': {'overflow': 'hidden'}
                                }
                            ),
                            dmc.NavLink(
                                label="Active subtle",
                                icon=get_icon(icon="tabler:activity"),
                                rightSection=get_icon(icon="tabler-chevron-right"),
                                variant="subtle",
                                active=True,
                            ),
                        ],
                        style={'white-space': 'nowrap'},
                    )
                ], style={'background-color': ''}, styles={'drawer': {'background-color': '#343a40'}}),
            dmc.Container([
                dmc.Header(
                    height=60,
                    children=[
                        dmc.Group([
                            dmc.MediaQuery([
                                dmc.Button(
                                    DashIconify(icon="ci:hamburger-lg", width=24, height=24, color="#c2c7d0"),
                                    variant="subtle",
                                    p=1,
                                    id='sidebar-button'
                                ),
                            ], smallerThan="md", styles={'display': 'none'}),
                            dmc.MediaQuery([
                                dmc.Button(
                                    DashIconify(icon="ci:hamburger-lg", width=24, height=24, color="#c2c7d0"),
                                    variant="subtle",
                                    p=1,
                                    id='drawer-demo-button'
                                ),
                            ], largerThan="md", styles={'display': 'none'}),
                            dmc.Text("IDS Technologie - ALVANET")
                        ])
                    ], p='10px', style={"backgroundColor": "#fff"}),
                # html.Div(
                #     id='page-content',
                #     children=[
                #         dcc.Tabs(
                #             id="tabs",
                #             children=[
                #                 dcc.Tab(label="Page 1", children=[
                #                     html.H1("Page 1"),
                #                 ]),
                #                 dcc.Tab(label="Page 2", children=[
                #                     html.H1("Page 2"),
                #                 ]),
                #             ]
                #         )
                #     ]
                # )
                myContent,
            ],
                id="page-container",
                p=0,
                fluid=True,
                style={'background-color': '#f4f6f9', 'width': '100%', 'margin': '0'}
            )
        ], size='100%', p=0, m=0, style={'display': 'flex'})
    ]
)


@callback(
    Output("sidebar", "width"),
    Input("sidebar-button", "n_clicks"),
    State('sidebar', 'width'),
    prevent_initial_call=True,
)
def drawer_demo(opened, width):
    if opened:
        if width['base'] == 300:
            return {"base": 70}
        else:
            return {'base': 300}
    else:
        raise PreventUpdate


@callback(
    Output("drawer-simple", "opened"),
    Input("drawer-demo-button", "n_clicks"),
    prevent_initial_call=True,
)
def drawer_dem(n_clicks):
    return True


# callback pour mettre à jour les pages
@callback(Output('page-content', 'children',),
          [Input('url', 'pathname')])
def display_page(pathname):
    # Get the current children of the page-content component
    myContent.children = []

    # Update the children of the page-content component based on the pathname
    if pathname == '/accueuil' or pathname == '/':
        myContent.children = []
        return myContent.children.append(accueuil.layout_acceuil)
    elif pathname == '/dashboard':
        myContent.children = []
        return myContent.children.append(dashboard.layout_dashboard)


if __name__ == '__main__':
    app.run(debug=True)
