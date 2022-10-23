#!/usr/bin/env python
# -*- coding: utf-8 -*-

import dash
import dash_mantine_components as dmc

from dash import Input
from dash import Output
from dash import State
from dash import callback

from dash_iconify import DashIconify

modal_add_item = dmc.Modal(
    id="modal-add-item",
    title="Add Item",
    centered=True,
    children=[
        dmc.Text("Inserts a new line item into the current bill of material."),
        dmc.Space(h=20),
        dmc.Select(
            id="nexar-search",
            label="Search NEXAR Database",
            description="Automatically populate the line item parameters based NEXAR database search results.",
            searchable=True,
            clearable=True,
            placeholder="Search MPN...",
            nothingFound="No match found",
            icon=[
                DashIconify(
                    icon="radix-icons:magnifying-glass"
                )
            ],
        ),
        dmc.Divider(style={"height": 20}),
        dmc.Select(
            id="classification",
            label="Classifiction",
            searchable=False,
            clearable=False
        ),
        dmc.TextInput(
            id="mpn",
            label="Manufacturing Part Number"
        ),
        dmc.TextInput(
            id="manufacturer",
            label="Manufacturer"
        ),
        dmc.TextInput(
            id="description",
            label="Description"
        ),
        dmc.NumberInput(
            id="quantity",
            label="Quantity",
            value=1
        ),
        dmc.Select(
            id="unit",
            label="Unit",
            searchable=True,
            clearable=False,
            nothingFound="No options found"
        ),
        dmc.Space(h=20),
        dmc.Group(
            position="right",
            children=[
                dmc.Button(
                    id="add-item",
                    children="Add"
                )
            ] 
        )
    ]
)

layout = dmc.Container(
    children=[
        modal_add_item,
        dmc.Button(
            id="open-modal-add-item",
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

@callback(
    Output("modal-add-item", "opened"),
    Input("open-modal-add-item", "n_clicks"),
    State("modal-add-item", "opened"),
    prevent_initial_call=True)
def modal_add_item_update(n_clicks, opened):
    return not opened
    