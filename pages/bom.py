#!/usr/bin/env python
# -*- coding: utf-8 -*-

import dash
import dash_mantine_components as dmc

from dash_iconify import DashIconify

layout = dmc.Container(
    children=[
        dmc.Button(
            id="add-item",
            children="Add Item",
            leftIcon=[DashIconify(icon="carbon:add")],
        )
    ]
)

dash.register_page(
    __name__,
    path="/builder",
    title="Builder | EasyBOM",
    description="",
    layout=layout
)