#!/usr/bin/env python
# -*- coding: utf-8 -*-

import dash
import dash_mantine_components as dmc

from dash import Input
from dash import Output
from dash import State
from dash import callback

from dash_iconify import DashIconify

from utils.lineitem import LineItem
from utils.lineitem import Unit
from utils.lineitem import Classification
from utils.nexar import NexarLifeCycle

modal_automatic_add_item = dmc.Modal(
    id="modal-manual-add-item",
    title="Manually Add Item",
    centered=True,
    children=[
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
        dmc.Space(h=20),
        dmc.Group(
            position="right",
            children=[
                dmc.Button(
                    id="automatic-add-item",
                    children="Add"
                )
            ] 
        )
    ]
)

modal_manual_add_item = dmc.Modal(
    id="modal-manual-add-item",
    title="Manually Add Item",
    centered=True,
    children=[
        dmc.Text("Inserts a new line item into the current bill of material."),
        dmc.Space(h=20),
        dmc.Select(
            id="classification",
            label="Classification"
        ),
        dmc.NumberInput(
            id="parent",
            label="Parent",
            min=0
        ),
        dmc.NumberInput(
            id="child",
            label="Child",
            min=0
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
            min=0,
            value=1
        ),
        dmc.Select(
            id="unit",
            label="Unit",
            value="Each"
        ),
        dmc.Space(h=20),
        dmc.Group(
            position="right",
            children=[
                dmc.Button(
                    id="manual-add-item",
                    children="Add"
                )
            ] 
        )
    ]
)

layout = dmc.Container(
    children=[
        modal_manual_add_item,
        modal_automatic_add_item,
        dmc.Button(
            id="open-modal-manual-add-item",
            children="Manual",
            leftIcon=[DashIconify(icon="carbon:add")],
        ),
        dmc.Button(
            id="open-modal-automatic-add-item",
            children="Automatic",
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
    Output("modal-manual-add-item", "opened"),
    Input("open-modal-manual-add-item", "n_clicks"),
    State("modal-manual-add-item", "opened"),
    prevent_initial_call=True)
def modal_manualadd_item_update(n_clicks, opened):
    return not opened

@callback(
    Output("modal-automatic-add-item", "opened"),
    Input("open-modal-automatic-add-item", "n_clicks"),
    State("modal-automatic-add-item", "opened"),
    prevent_initial_call=True)
def modal_manualadd_item_update(n_clicks, opened):
    return not opened