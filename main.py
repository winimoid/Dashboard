import dash.development.component_loader
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc
from dash import Dash, html, dcc, Input, Output, State, callback
from dash.exceptions import PreventUpdate
from dash_iconify import DashIconify

from layouts import accueuil, dashboard

# Initialize the app - incorporate a Dash Mantine theme
# external_stylesheets = [dmc.theme.DEFAULT_COLORS]
# external_stylesheets = [dbc.themes.CYBORG]
# external_stylesheets = [dbc.themes.CERULEAN]
# external_stylesheets = [dbc.themes.DARKLY]
# external_stylesheets = [dbc.themes.COSMO]
# external_stylesheets = [dbc.themes.FLATLY]
# external_stylesheets = [dbc.themes.JOURNAL]
# external_stylesheets = [dbc.themes.LITERA]  # JOLI !
# external_stylesheets = [dbc.themes.LUMEN]
# external_stylesheets = [dbc.themes.LUX]  # PML
# external_stylesheets = [dbc.themes.MATERIA]  # BIEN !
# external_stylesheets = [dbc.themes.MINTY]
# external_stylesheets = [dbc.themes.MORPH]  # VRAIMENT BIEN
# external_stylesheets = [dbc.themes.PULSE]
# external_stylesheets = [dbc.themes.QUARTZ]  # BIEN !
# external_stylesheets = [dbc.themes.SANDSTONE]
# external_stylesheets = [dbc.themes.SIMPLEX]
# external_stylesheets = [dbc.themes.SKETCHY]  # TRES JOLI !
# external_stylesheets = [dbc.themes.SLATE]  # COOL !
# external_stylesheets = [dbc.themes.SOLAR]
# external_stylesheets = [dbc.themes.SPACELAB]
# external_stylesheets = [dbc.themes.SUPERHERO]
# external_stylesheets = [dbc.themes.UNITED]
# external_stylesheets = [dbc.themes.VAPOR]
# external_stylesheets = [dbc.themes.YETI]  # SURE !
external_stylesheets = [dbc.themes.ZEPHYR]
app = Dash(__name__, external_stylesheets=external_stylesheets)


def get_icon(icon):
    return DashIconify(icon=icon, height=16, color="#c2c7d0")


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
                html.Div(
                    id='page-redirect',
                    # children=[
                    #     dcc.Tabs(
                    #         id="tabs",
                    #         children=[
                    #             dcc.Tab(label="Page 1", children=[
                    #                 html.H1("Page 1"),
                    #             ]),
                    #             dcc.Tab(label="Page 2", children=[
                    #                 html.H1("Page 2"),
                    #             ]),
                    #         ]
                    #     )
                    # ]
                ),
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


# callback pour rediriger vers la page dashboard
@app.callback(
    Output("url", "pathname"),
    [Input("button", "n_clicks")],
    prevent_initial_call=True,
    suppress_callback_exceptions=True)
def redirect_to_dashboard(n_clicks):
    if n_clicks > 0:
        display_page(pathname="/dashboard")
        # return "/dashboard"
    else:
        display_page(pathname="/")
        # return "/"


# callback pour mettre à jour les pages
@callback(Output('page-redirect', 'children'),
          [Input('url', 'pathname')], prevent_initial_call=True)
def display_page(pathname):
    # children.clear()
    if pathname == '/accueuil' or pathname == '/':
        return accueuil.layout_acceuil
    elif pathname == '/dashboard':
        return dashboard.layout_dashboard


if __name__ == '__main__':
    app.run(debug=True)
