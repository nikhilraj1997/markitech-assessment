from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import numpy as np
from datetime import datetime

external_stylesheets = [
    "https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;700&display=swap", "./assets/styles/main.css"]

app = Dash(__name__, title="Markitech.ai Assessment",
           external_stylesheets=external_stylesheets)

_navbar = html.Div(children=[
    html.Nav(children=[
        html.Div(children=[
            dcc.Dropdown(["SDC", "NYC", "SF", "LA"], id="city-dropdown"),
            dcc.Dropdown(["Team (All)", "01A", "01B", "01C",
                          "02A", "03A"], id="team-dropdown"),
        ]),
        html.Button("Export Results", id="export-button", className="button")
    ], className="nav"),
    html.Div(children=[
        html.Div(children=[
            html.Div(children=[
                html.Img(src="./assets/icons/location.svg"),
            ]),
            html.Div(children=[
                html.H4("SDC"),
                html.H1("YZX")
            ]),
        ], className="header__location"),
        html.Div(children=[
            html.P("Last Refreshed"),
            html.P(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        ], className="header__refresh",)
    ], className="header__title")
], className="header")


_model_options_section = html.Div(children=[
    html.Form(children=[
        html.Fieldset(children=[
            html.Label("Select Projection Timeframe",
                       style={"width": "14rem"}),
            dcc.RadioItems(
                options=[
                    {"label": "3 Month Outlook", "value": "3MO"},
                    {"label": "6 Month Outlook", "value": "6MO"},
                ], value="3MO", id="model-timeframe-radio")
        ], className="radio-list radio-list--column"),
        html.Fieldset(children=[
            html.Label("Select Scenario Parameters for Model Projection",
                       style={"width": "18rem"}),
            dcc.RadioItems(
                options=[
                    {"label": html.P([html.Span("Existing Geoboundary", className="bold"), " and ", html.Span("Existing Team", className="bold"), " Assignments"]),
                        "value": "existing"},
                    {"label": html.P([html.Span("Optimal Geoboundary", className="bold"), " and ", html.Span("Optimal Team", className="bold"), " Assignments"]),
                        "value": "optimal"},
                    {"label": html.Div([
                        html.P(
                            [html.Span("Optimal Geoboundaries", className="bold"), " based on ", html.Span("Defined # of Teams", className="bold"), " Assignments"]),
                        html.Div([
                            dcc.Input(id="defined-geoboundary-input",
                                      type="number", value=0, min=0, max=10),
                            html.P("Teams")
                        ])
                    ], className="nested-inputs"), "value": "defined"},
                    {"label": dcc.Dropdown(["Option 1", "Option 2", "Option 3", "Option 4"],
                                           id="defined-members-value"), "value": "defined-members"},
                ], value="existing", id="model-scenario-radio")
        ], className="radio-list radio-list--row"),
        html.Div(children=[
            html.Button("Run Model Projection",
                        id="model-run-button", className="button"),
            html.Button("Reset", id="model-reset-button",
                        className="button button--secondary")
        ], className="model-options-form__actions"),
    ], className="model-options-form")
], className="model-options-section")


def outlook_item(icon, metric, value, subtext=None, comparison=None):
    return html.Div(children=[
        html.Div(children=[
            html.Img(src=icon)
        ]),
        html.Div(children=[
            html.H4(metric, className="outlook-item__metric-header"),
            html.H1(value),
            html.P(subtext if subtext else "",
                   className="outlook-item__subtext")
        ]),
        html.Div(children=[
            html.P(comparison) if comparison else None
        ], className="outlook-item__comparison"),
    ], className="outlook-item")


def outlook_extra_item(extra_metric_items=[]):
    return html.Div(children=[
        html.Div(children=[
            html.P("by"),
            html.P("Type")
        ]),
        html.Div(children=extra_metric_items,
                 className="outlook-extra-metric-items"),
        html.Div(children=[
        ], className="outlook-item__comparison"),
    ], className="outlook-extra-item")


def outlook_extra_item_metric(value, text):
    return html.Div(children=[
        html.P(value),
        html.P(text, className="outlook-item__subtext")
    ], className="outlook-extra-item__metric")


def outlook_element(title, items, extra_items=None, subtext=None):
    if extra_items:
        items.extend(extra_items)

    return html.Div(children=[
        html.H4(title),
        html.Div(children=items),
        html.P(subtext) if subtext else None
    ], className="outlook-element")


_outlook_element_1 = outlook_element(["Outlook ", html.Span("Summary")],
                                     [
    outlook_item("/assets/icons/icon1.svg",
                 "Projected Visits", "200", "/bi-weekly"),
    outlook_item("/assets/icons/icon2.svg",
                 "Projected Clients", "134", "/bi-weekly"),
    outlook_item("/assets/icons/icon3.svg", "Existing Nurses", "100")
], [
    outlook_extra_item([outlook_extra_item_metric(67, "Full time 0.0%"), outlook_extra_item_metric(
        25, "Part time 0.0%"), outlook_extra_item_metric(8, "Casual 0.0%")])
])

_outlook_element_2 = outlook_element(["Projected Staff ", html.Span("Utilization")], [
    outlook_item("/assets/icons/icon4.svg",
                 "Utilization", "101%", None, "-"),
    outlook_item("/assets/icons/icon5.svg", "Total Nurse Gap",
                 "+15", "Recommended additional nurses to optimize KPIs", "-"),
], [
    outlook_extra_item([outlook_extra_item_metric("+8", "Full time"), outlook_extra_item_metric(
        "+4", "Part time"), outlook_extra_item_metric("+3", "Casual")])
], "Compared to Existing Geoboundaries")

_outlook_element_3 = outlook_element(["Projected Nurse ", html.Span("Workload")], [
    outlook_item("/assets/icons/icon6.svg",
                 "Average Visits per Nurse", "39", "/bi-weekly", "-"),
    outlook_item("/assets/icons/icon7.svg",
                 "Distance Travelled per Nurse", "200 km", "/bi-weekly", "-"),
], None, "Compared to Existing Geoboundaries")

_outlook_element_4 = outlook_element(["Projected ", html.Span("Patient Care")], [
    outlook_item("/assets/icons/icon8.svg",
                 "Continuity of Care", "57%", None, "-"),
], None, "Compared to Existing Geoboundaries")

_outlook_element_5 = outlook_element(["Projected ", html.Span("Acceptance")], [
    outlook_item("./assets/icons/icon9.svg",
                 "Referral Acceptance Rate", "85%", None, "-"),
], None, "Compared to Existing Geoboundaries")

_outlook_section = html.Div(children=[
    html.H4("Model Projections - 3 Month Outlook"),
    html.Div(children=[_outlook_element_1, _outlook_element_2,
             _outlook_element_3, _outlook_element_4, _outlook_element_5], className="outlook-element__container")
], className="outlook-section")

_summary = html.Div(children=[
    html.Div(children=[
        html.H4("Nurse Team Summary"),
        html.P("Total Teams: 5"),
    ]),
    html.Div(children=[
        dcc.Tabs(id="summary-tab", value="existing-nurse-count", children=[
            dcc.Tab(label="Existing Nurse Count",
                    value="existing-nurse-count"),
            dcc.Tab(label="Ideal Nurse Count", value="ideal-nurse-count"),
            dcc.Tab(label="Nurse Gap", value="nurse-gap"),
            dcc.Tab(label="Capacity %", value="capacity"),
        ], className="summary-tab", ),
        html.Div(id="summary-tab-content", className="summary-tab__content"),
    ])
], className="summary-section")


def generate_random_df(num_rows, num_cols, min_val, max_val, col_names=None, row_names=None):
    if col_names is None:
        col_names = ["Col" + str(i) for i in range(num_cols)]
    if row_names is None:
        row_names = ["Row" + str(i) for i in range(num_rows)]
    df = pd.DataFrame(np.random.randint(min_val, max_val, size=(
        num_rows, num_cols)), columns=col_names, index=row_names)
    return df


def generate_table(dataframe, max_rows=15):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])


def generate_two_head_table(dataframe, max_rows=5):
    return html.Table([
        html.Thead(
            html.Tr([html.Th([]),
                     *[html.Th(col) for col in dataframe.columns]])
        ),
        html.Tbody([
            html.Tr([
                html.Th(dataframe.index[i]),
                *[html.Td(dataframe.iloc[i][col]) for col in dataframe.columns]
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])


df_existing_nurse_count = generate_random_df(
    4, 5, 0, 100, col_names=["01A", "01B", "01C", "02A", "03A"], row_names=["Total", "Full Time", "Part Time", "Casual"])


df_ideal_nurse_count = generate_random_df(
    4, 5, 0, 100, col_names=["01A", "01B", "01C", "02A", "03A"], row_names=["Total", "Full Time", "Part Time", "Casual"])


df_nurse_gap = generate_random_df(
    4, 5, 0, 100, col_names=["01A", "01B", "01C", "02A", "03A"], row_names=["Total", "Full Time", "Part Time", "Casual"])

df_capacity = generate_random_df(
    4, 5, 0, 100, col_names=["01A", "01B", "01C", "02A", "03A"], row_names=["Total", "Full Time", "Part Time", "Casual"])

summary_tab_data = {
    "existing-nurse-count": generate_two_head_table(df_existing_nurse_count),
    "ideal-nurse-count": generate_two_head_table(df_ideal_nurse_count),
    "nurse-gap": generate_two_head_table(df_nurse_gap),
    "capacity": generate_two_head_table(df_capacity)
}


@ app.callback(
    Output("summary-tab-content", "children"),
    Input("summary-tab", "value")
)
def render_summary_tab_content(tab):
    return summary_tab_data[tab]


_projection_graphs = html.Div(children=[
    html.Div(children=[
        html.H4("KPI Projections Across Teams | Utilization"),
        dcc.Dropdown(id='projection-graph-dropdown',
                     options=[
                         {'label': 'Metric 1', 'value': '1'},
                         {'label': 'Metric 2', 'value': '2'},
                         {'label': 'Metric 3', 'value': '3'},
                     ],
                     value='1'),
    ], className="projection-graphs__header"),
    dcc.Graph(id='projection-graph', config={'displayModeBar': False}),
], className="projection-graphs")


@ app.callback(Output(component_id='projection-graph', component_property='figure'),
               [Input(component_id='projection-graph-dropdown', component_property='value')])
def graph_update(dropdown_value):
    df = generate_random_df(5, 2, 0, 100, col_names=["x", "y"], row_names=[
        "01A", "01B", "01C", "02A", "03A"])
    fig = px.bar(df, height=250)
    fig.update_layout(showlegend=False, margin={'t': 0, 'b': 0, 'l': 0, 'r': 0}, paper_bgcolor='rgba(0,0,0,0)',
                      plot_bgcolor='rgba(0,0,0,0)')
    return fig


_projections_section = html.Details(children=[
    html.Summary("Hide Projections Across Teams",
                 id="projections-section-title"),
    html.Div(children=[_summary, _projection_graphs],
             className="projections-section")
], open=True)

df = px.data.election()
geojson = px.data.election_geojson()

map_fig = px.choropleth_mapbox(df, geojson=geojson, color="Bergeron",
                               locations="district", featureidkey="properties.district",
                               center={"lat": 45.5517, "lon": -73.7073},
                               mapbox_style="carto-positron", zoom=10)
map_fig.update_layout(margin={'t': 0, 'b': 0, 'l': 0, 'r': 0},
                      paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
map_fig.update_coloraxes(showscale=False)

_geoboundary_section = html.Div(children=[
    html.Div(children=[
        html.H4("Geoboundary and Team Assignments"),
        html.Button("Create Custom Geoboundary Assignment",
                    id="create-custom-geoboundary-button", className="button"),
    ], className="geoboundary-section__header"),
    html.Div(children=[
        html.Div(children=[
            html.Form(children=[
                html.Fieldset(children=[
                    html.Label("Show Geoboundary As:",
                               htmlFor="geoboundary-type-selector"),
                    dcc.RadioItems(id="geoboundary-type-selector", options=[
                        {"label": "Teams", "value": "teams"},
                        {"label": "Geocodes", "value": "geocodes"}
                    ], value="teams")
                ], className="radio-list radio-list--column"),
                html.Fieldset(children=[
                    html.Label("View Geoboundary Outlines for:",
                               htmlFor="geoboundary-view-selector"),
                    dcc.RadioItems(id="geoboundary-view-selector", options=[
                        {"label": "Existing Geoboundary and Existing Team",
                            "value": "existing-geoboundary-existing-team"},
                        {"label": "Optimal Geoboundaries and Existing Team",
                            "value": "optimal-geoboundaries-existing-team"},
                        {"label": "Optimal Geoboundaries based on defined # of Teams",
                            "value": "optimal-geoboundaries-defined-teams"},
                        {"label": dcc.Dropdown(
                            [
                                {"label": "Option 1", "value": "option-1"},
                                {"label": "Option 2", "value": "option-2"},
                                {"label": "Option 3", "value": "option-3"},
                                {"label": "Option 4", "value": "option-4"},
                            ], value=""), "value": "custom-geoboundary"}
                    ], value="existing-geoboundary-existing-team")
                ], className="radio-list radio-list--column"),
                html.Fieldset(children=[
                    html.Label("Color Map by:", htmlFor="color-map-selector"),
                    dcc.RadioItems(id="color-map-selector", options=[
                        {"label": "Team Assignments", "value": "team-assignments"},
                        {"label": dcc.Dropdown([
                            {"label": "Nurse Count", "value": "nurse-count"},
                            {"label": "Nurse Gap", "value": "nurse-gap"},
                            {"label": "Capacity %", "value": "capacity"}
                        ]), "value": "custom-color-map"}
                    ], value=""),
                    dcc.RadioItems(id="additional-map-layers", options=[
                        {"label": dcc.Dropdown(
                            [
                                {"label": "Option 1", "value": "option-1"},
                                {"label": "Option 2", "value": "option-2"},
                                {"label": "Option 3", "value": "option-3"},
                                {"label": "Option 4", "value": "option-4"},
                            ], value=""), "value": "additional-map-layers-value"},
                    ], value="")
                ], className="radio-list radio-list--column"),
            ]),
            html.Div(children=[
                html.Div(children=[
                    html.P("Total"),
                    html.P("00 Geocodes")
                ], className="geoboundary-section__total-count"),
                html.Div(children=[
                    html.P("Geocodes Impacted From Existing Geoboundary Assignments"),
                    html.Div(children=[
                        generate_table(generate_random_df(
                            15, 3, 0, 100, col_names=["Geocode Changes", "From", "To"]))
                    ])
                ], className="geoboundary-section__geocode-changes"),
            ], className="geoboundary-section__info"),
        ], className="geoboundary-section__options"),
        html.Div(children=[
            dcc.Graph(id="geoboundary-map", figure=map_fig,
                      config={'displayModeBar': False}),
        ], className="geoboundary-section__map"),
    ], className="geoboundary-section__content")
], className="section geoboundary-section")

_notes_section = html.Div(children=[
    html.H4("Notes"),
    html.P(children=[
        "Select ",
        html.Span("\"Create Custom Geoboundary Assignment\" ",
                  style={"fontWeight": "bold"}),
        "to go into edit mode with additional buttons."
    ])
], className="notes-section")

app.layout = html.Div(children=[
    html.Div(children=[_navbar, _model_options_section], className="section"),
    html.Div(children=[html.Div(children=[_outlook_section, _projections_section],
             className="section"), _geoboundary_section, _notes_section])
])

if __name__ == '__main__':
    server = app.server
