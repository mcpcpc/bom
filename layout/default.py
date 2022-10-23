#!/usr/bin/env python
# -*- coding: utf-8 -*-

import dash_mantine_components as dmc

from dash import page_container
from dash import dcc
from dash import html
from dash import clientside_callback

from dash import Input
from dash import Output
from dash_iconify import DashIconify

header_left = dmc.Center(
    dcc.Link(
        href="/",
        style={"paddingTop": 3, "textDecoration": "none"},
        children=[
            dmc.MediaQuery(
                dmc.Text(
                    "b0m",
                    size="xl",
                    color="gray"
                ),
                smallerThan="sm",
                styles={"display": "none"}
            ),
            dmc.MediaQuery(
                dmc.Text(
                    "b0m Builder",
                    size="xl",
                    color="gray"
                ),
                largerThan="sm",
                styles={"display": "none"}
            )
        ]
    )
)

header_right = dmc.Group(
    position="right",
    align="center",
    spacing="xl",
    children=[
        html.A(
            dmc.ThemeIcon(
                DashIconify(
                    icon="radix-icons:github-logo",
                    width=22,
                ),
                radius=30,
                size=36,
                variant="outline",
                color="gray"
            ),
            href="https://github.com/mcpcpc/bom",
        ),
        dmc.ThemeSwitcher(
            id="color-scheme-toggle",
            style=dict(cursor="pointer"),
        ),
    ]
)

def header(data):
    return dmc.Header(
        height=70,
        fixed=True,
        p="md",
        children=[
            dmc.Container(
                fluid=True,
                children=[
                    header_left,
                    header_right
                ]
            ) 
        ]
    ) 
 
def wrapper(data):
    return html.Div(
        id="wrapper",
        children=[
            dmc.Container(
                children=page_container,
                pt=90,
                size="lg"
            )
        ]
    )

def layout(data):
    return dmc.MantineProvider(
        id="theme-provider",
        withGlobalStyles=True,
        withNormalizeCSS=True,
        theme={
            "colorScheme": "light",
            "fontFamily": "'Inter', sans-serif",
            "primaryColor": "indigo",
        },
        children=[
            dmc.NotificationsProvider(
                children=[
                    header(data),
                    wrapper(data)
                ]
            )
        ]
    )

clientside_callback(
    """function(colorScheme) { 
        return {
            colorScheme,
            fontFamily: "'Inter', sans-serif", 
            primaryColor: "indigo"
        }
    }""",
    Output("theme-provider", "theme"),
    Input("color-scheme-toggle", "value"),
    prevent_initial_callback=True,
)