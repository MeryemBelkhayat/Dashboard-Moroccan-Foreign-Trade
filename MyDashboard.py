

"""importing necessary libraries"""

import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from plotly.graph_objs.layout import Annotation


"""Data processing"""

df=pd.read_excel('Data.xlsx')
df=df.rename(columns={"Libellé du groupement d'utilisation": "groupement_utilisation",
                   "Libellé de la section CTCI": "section_CTCI",
                   "Libellé de la division CTCI": "division_CTCI",
                   "Libellé du groupe CTCI": "groupe_CTCI",
                   "Libellé du pays": "pays",
                   "Libellé du flux": "flux"})

#create importation dataFrame
df1=df
importation = df1.loc[(df1['flux'] == 'Importations CAF')]


#Create exportation dataFrame
df1=df
exportation= df1.loc[(df1['flux'] == 'Exportations FAB')]

#Create monthly evolution of importation dataFrame
data = {'Mois': ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Aout', 'Septembre', 'Octobre', 'Novembre','Décembre']}
total_importation = pd.DataFrame(data)
total_importation_2018 = []
total_importation_2019 = []
total_importation_2020 = []
Mois = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Aout', 'Septembre', 'Octobre', 'Novembre',
        'Décembre']
for i in Mois:
    total_importation_2018.append(importation['Valeur DHS ' + str(i) + ' 2018'].sum())
for i in Mois:
    total_importation_2019.append(importation['Valeur DHS ' + str(i) + ' 2019'].sum())
for i in Mois:
    total_importation_2020.append(importation['Valeur DHS ' + str(i) + ' 2020'].sum())

total_importation['total_importation_2018'] = total_importation_2018
total_importation['total_importation_2019'] = total_importation_2019
total_importation['total_importation_2020'] = total_importation_2020

#Create monthly evolution of exportation dataFrame
total_exportation = pd.DataFrame(data)

total_exportation_2018 = []
total_exportation_2019 = []
total_exportation_2020 = []
for i in Mois:
    total_exportation_2018.append(exportation['Valeur DHS ' + str(i) + ' 2018'].sum())
for i in Mois:
    total_exportation_2019.append(exportation['Valeur DHS ' + str(i) + ' 2019'].sum())
for i in Mois:
    total_exportation_2020.append(exportation['Valeur DHS ' + str(i) + ' 2020'].sum())

total_exportation['total_exportation_2018'] = total_exportation_2018
total_exportation['total_exportation_2019'] = total_exportation_2019
total_exportation['total_exportation_2020'] = total_exportation_2020

Annee=['2018','2019','2020']
data = {'Annee':Annee}

#Create annual evolution of importation&exportation dataFrame
M = ["groupement_utilisation"]
for i in Mois:
    M.append("Valeur DHS " + i + " 2018")

ImportationParGU2018 = importation.loc[:, M]
ImportationParGU2018 = ImportationParGU2018.groupby(['groupement_utilisation']).sum().reset_index()
ImportationParGU2018["total_2018"] = ImportationParGU2018.sum(axis=1)

M = ["groupement_utilisation"]
for i in Mois:
    M.append("Valeur DHS " + i + " 2019")

ImportationParGU2019 = importation.loc[:, M]
ImportationParGU2019 = ImportationParGU2019.groupby(['groupement_utilisation']).sum().reset_index()
ImportationParGU2019["total_2019"] = ImportationParGU2019.sum(axis=1)

M = ["groupement_utilisation"]
for i in Mois:
    M.append("Valeur DHS " + i + " 2020")

ImportationParGU2020 = importation.loc[:, M]
ImportationParGU2020 = ImportationParGU2020.groupby(['groupement_utilisation']).sum().reset_index()
ImportationParGU2020["total_2020"] = ImportationParGU2020.sum(axis=1)

M = ["groupement_utilisation"]
for i in Mois:
    M.append("Valeur DHS " + i + " 2018")

ExportationParGU2018 = exportation.loc[:, M]
ExportationParGU2018 = ExportationParGU2018.groupby(['groupement_utilisation']).sum().reset_index()
ExportationParGU2018["total_2018"] = ExportationParGU2018.sum(axis=1)

M = ["groupement_utilisation"]
for i in Mois:
    M.append("Valeur DHS " + i + " 2019")

ExportationParGU2019 = exportation.loc[:, M]
ExportationParGU2019 = ExportationParGU2019.groupby(['groupement_utilisation']).sum().reset_index()
ExportationParGU2019["total_2019"] = ExportationParGU2019.sum(axis=1)

M = ["groupement_utilisation"]
for i in Mois:
    M.append("Valeur DHS " + i + " 2020")

ExportationParGU2020 = exportation.loc[:, M]
ExportationParGU2020 = ExportationParGU2020.groupby(['groupement_utilisation']).sum().reset_index()
ExportationParGU2020["total_2020"] = ExportationParGU2020.sum(axis=1)

GU = df['groupement_utilisation'].unique()
mylist=["Total"]
for s in list(GU):
    mylist.append(s)
evolution_exportation_annuelle_GU = pd.DataFrame(data)
evolution_importation_annuelle_GU = pd.DataFrame(data)

for j in GU:
    X = []
    Y = []
    tem = ExportationParGU2018.loc[ExportationParGU2018['groupement_utilisation'] == j]
    X.append(float(tem.loc[:, 'total_2018']))
    tem = ExportationParGU2019.loc[ExportationParGU2019['groupement_utilisation'] == j]
    X.append(float(tem.loc[:, 'total_2019']))
    tem = ExportationParGU2020.loc[ExportationParGU2020['groupement_utilisation'] == j]
    X.append(float(tem.loc[:, 'total_2020']))
    evolution_exportation_annuelle_GU[j] = X

    tem = ImportationParGU2018.loc[ImportationParGU2018['groupement_utilisation'] == j]
    Y.append(float(tem.loc[:, 'total_2018']))
    tem = ImportationParGU2019.loc[ImportationParGU2019['groupement_utilisation'] == j]
    Y.append(float(tem.loc[:, 'total_2019']))
    tem = ImportationParGU2020.loc[ImportationParGU2020['groupement_utilisation'] == j]
    Y.append(float(tem.loc[:, 'total_2020']))
    evolution_importation_annuelle_GU[j] = Y


exportation_annuelle=[]
importation_annuelle=[]

for i in Annee:
    exportation_annuelle.append(total_exportation['total_exportation_'+i].sum())
for i in Annee:
    importation_annuelle.append(total_importation['total_importation_'+i].sum())


evolution_importation_annuelle_GU['Total']=importation_annuelle
evolution_exportation_annuelle_GU['Total']=exportation_annuelle

grouped_dfim = importation.groupby(["groupement_utilisation"]).sum().reset_index()
grouped_dfex = exportation.groupby(["groupement_utilisation"]).sum().reset_index()

totalimp_2018 = grouped_dfim["Valeur DHS Janvier 2018"]
totalimp_2019 = grouped_dfim["Valeur DHS Janvier 2019"]
totalimp_2020 = grouped_dfim["Valeur DHS Janvier 2020"]
totalexp_2018 = grouped_dfex["Valeur DHS Janvier 2018"]
totalexp_2019 = grouped_dfex["Valeur DHS Janvier 2019"]
totalexp_2020 = grouped_dfex["Valeur DHS Janvier 2020"]
for i in Mois[1:]:
    totalimp_2018 += grouped_dfim["Valeur DHS " + i + " 2018"]
    totalimp_2019 += grouped_dfim["Valeur DHS " + i + " 2019"]
    totalimp_2020 += grouped_dfim["Valeur DHS " + i + " 2020"]
    totalexp_2018 += grouped_dfex["Valeur DHS " + i + " 2018"]
    totalexp_2019 += grouped_dfex["Valeur DHS " + i + " 2019"]
    totalexp_2020 += grouped_dfex["Valeur DHS " + i + " 2020"]

grouped_dfim["2018"] = totalimp_2018
grouped_dfim["2019"] = totalimp_2019
grouped_dfim["2020"] = totalimp_2020

grouped_dfex["2018"] = totalexp_2018
grouped_dfex["2019"] = totalexp_2019
grouped_dfex["2020"] = totalexp_2020
grouped_dfim = grouped_dfim[["groupement_utilisation", "2018", "2019", "2020"]]
grouped_dfex = grouped_dfex[["groupement_utilisation", "2018", "2019", "2020"]]



"""Making the dashboard"""

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
colors = {
 'background': '#0D213A',
 'text': '#9090FE'
}

app.layout =html.Div(style={'backgroundColor': colors['background']},children=[
             html.H1(
             children='Commerce Extérieur',
             style={
             'color': colors['text']
             }
             ),
    html.Div([
        html.Div([
            html.H6(children='Evolution Mensuelle Des Flux Importation-Exportation',
                    style={'textAlign': 'center', 'color': colors['text']}),
            dcc.Slider(min=2018, max=2020, step=1, value=2020, id='slider',dots=True, marks={
                2018: '2018',
                2019: '2019',
                2020: '2020'},
            ),
            html.Br(),
            dcc.Graph(id="time-series",
                      style={'height': 200},
                      )], className='four columns'),
                html.Div([
                    html.H6(children="Evolution de la répartition des échanges selon les groupements d'utilisation",
                            style={'textAlign': 'center', 'color': colors['text']}),
                    dcc.RadioItems(
                        id="radio1",
                        options=[{'label': 'Importaion', 'value': 'Importation'},
                                 {'label': 'Exportation', 'value': 'Exportation'},],
                        value='Importation',
                        labelStyle ={'display': 'inline-flex','fontWeight': 'bold','color':'#B8DBEE'},
                        ),
                    dcc.Graph(id="DONUTPIE",
                              style={'height':200}),
                          ], className='eight columns')],className='one row'),
            html.Div([
                html.Div([
                    html.H6(children="Répartition des flux Importation-Exportation selon les pays",
                            style={'textAlign': 'center', 'color': colors['text']}),

                    dcc.RadioItems(
                        id="Checklist2",
                        options=[{'label': 'Importaion', 'value': 'Importation'},
                                 {'label': 'Exportation', 'value': 'Exportation'}, ],
                        value='Importation',
                        labelStyle ={'display': 'inline-flex','fontWeight': 'bold','color':'#B8DBEE'},
                        ),
                    dcc.Graph(id="MAP",
                              style={'height': 250}),
                    ], className='six columns'),
                html.Div([
                    html.Br(),
                    html.H6(children='Balance Commerciale',
                            style={'textAlign': 'center', 'color': colors['text']}),
                    dcc.Tabs(id="tabs", value=2,style={'textAlign': 'center','height':50}, children=[
                        dcc.Tab(label='2020', value=2),
                        dcc.Tab(label='2019', value=1),
                        dcc.Tab(label='2018', value=0),
                    ],colors={ 'border': '#B8DBEE', 'primary': '#2cc7c2','background': '#B8DBEE'},content_style={'textAlign': 'center', 'color': colors['text']}),
                    dcc.Graph(id='indicator',
                      style={'height':240}),
                      ], className='three columns'),
                html.Div([
                    html.H6(children='Evolution Annuelle Des Flux Importation-Exportation',
                            style={'textAlign': 'center', 'color': colors['text']}),
                    dcc.Dropdown(
                        id="dropdown",
                        style={'height':30,'weight':60,'backgroundColor':'#B8DBEE','color':'#0D213A'},
                        options=[{"label": x, "value": x} for x in mylist],
                        value=mylist[0],
                        clearable=False,),
                    html.Br(),
                    dcc.Graph(id='bar-chart',
                      style={'height':215}),
                      ], className='three columns')], className='one row'),
])



@app.callback(
    Output("bar-chart", "figure"),
    [Input("dropdown", "value")])
def update_bar_chart(x):
    ex=list(evolution_exportation_annuelle_GU[x])
    im = list(evolution_importation_annuelle_GU[x])
    trace1 = go.Bar(
        x=Annee,
        y=ex,
        marker_color='#9090FE',
        textposition="outside",  # text position
        name="Exportation",  # legend name
    )
    trace2 = go.Bar(
        x=Annee,
        y=im,
        marker_color='#42DEED',
        textposition="outside",
        name="Importation",
    )
    data = [trace1, trace2]  # combine two charts/columns
    layout = go.Layout(barmode="group")  # define how to display the columns
    fig3 = go.Figure(data=data, layout=layout)
    fig3.update_layout(
        title=dict(x=0.5),  # center the title
        xaxis_title="Années",  # setup the x-axis title
        yaxis_title="Valeur en DH",  # setup the x-axis title
        margin=dict(l=20, r=20, t=60, b=20),  # setup the margin
        paper_bgcolor="#0D213A",  # setup the background color
        plot_bgcolor='rgba(0,0,0,0)'
    )

    fig3.update_layout(font_color="#B8DBEE")

    return fig3
@app.callback(
    Output("time-series", "figure"),
    [Input("slider", "value")])
def update_time_series(x):
    trace1 = go.Scatter(
        x=Mois,
        y=total_exportation["total_exportation_"+str(x)],
        marker_color='#9090FE',
        name="Exportation",
    )
    trace2 = go.Scatter(
        x=Mois,
        y=total_importation["total_importation_"+str(x)],
        marker_color='#42DEED',
        name="Importation",
    )
    data = [trace1, trace2]  # combine two charts/columns

    fig = go.Figure(data=data)
    fig.update_layout(
        title=dict(x=0.5),  # center the title
        xaxis_title="Années",  # setup the x-axis title
        yaxis_title="Valeur en DH",  # setup the x-axis title
        margin=dict(l=20, r=20, t=60, b=20),  # setup the margin
        paper_bgcolor="#0D213A",  # setup the background color
        plot_bgcolor='rgba(0,0,0,0)'
    )
    fig.update_layout(font_color="#B8DBEE")

    return fig
@app.callback(
    Output("MAP", "figure"),
    [Input("Checklist2", "value")])
def update_map(x):
    if x == 'Importation':
        df_map = pd.read_excel('df_mapim.xlsx')
    else:
        df_map = pd.read_excel('df_mapex.xlsx')
    colors = ['#948c00', '#fff200', '#f0eca8']
    Annee = ['2018', '2019', '2020']
    fig1 = go.Figure()
    j = 0
    for i in Annee:
        df_map = df_map.loc[(df_map[str(i)] >= 10)]
        df_map['temp'] = np.log(df_map[str(i)]) * 0.95 + 0.05 * df_map[str(i)]
        df_map['text'] = df_map['pays'] + ':<br> ' + df_map[str(i)].astype(str) + ' DH'
        fig1.add_trace(go.Scattergeo(
            lon=df_map['log'],
            lat=df_map['lat'],
            text=df_map['text'],
            name=i,
            marker=dict(
                size=df_map['temp'] / 100005000,
                color=colors[j],
                line_width=0
            )))
        j += 1

    fig1.update_layout(
        geo=go.layout.Geo(
            scope='world',
            showframe=False,
            showcoastlines=True,
            landcolor="#B8DBEE",
            countrycolor="#0D213A",
            coastlinecolor="#0D213A",
            oceancolor="#0D213A",
            bgcolor="#0D213A",
        ),
        legend_traceorder='reversed',
        margin=dict(l=2, r=5, t=2, b=2),
    )
    fig1.update_layout(legend=dict(
        yanchor="top",
        y=0.99,
        xanchor="right",
        x=0.01
    ))

    fig1.update_layout(font_color="#B8DBEE",
                      paper_bgcolor="#0D213A",  # setup the background color
                      plot_bgcolor="#0D213A")
    return fig1

@app.callback(
    Output("DONUTPIE", "figure"),
    [Input("radio1", "value")])

def update_DONUTPIE(x):
    if x == 'Importation':
        grouped_df = grouped_dfim
    else:
        grouped_df = grouped_dfex

    trace1 = {
        "hole": 0.8,
        "type": "pie",
        "labels": grouped_df['groupement_utilisation'],
        "values": grouped_df['2018'],
        "name": "2018",
        "showlegend": False,
        "domain": {'x': [0, 1], 'y': [0.2, 0.8]}
    }
    trace2 = {
        "hole": 0.8,
        "type": "pie",
        "labels": grouped_df['groupement_utilisation'],
        "values": grouped_df['2019'],
        "name": "2019",
        "showlegend": False,
        "domain": {'x': [0.2, 0.8], 'y': [0.1, 0.9]}
    }
    trace3 = {
        "hole": 0.85,
        "type": "pie",
        "labels": grouped_df['groupement_utilisation'],
        "values": grouped_df['2020'],
        "name": "2020",
        "showlegend": True,
        "domain": {'x': [0.1, 0.9], 'y': [0, 1]}

    }
    colors = ['#7900FF', '#548CFF', '#93FFD8', '#35b6bd', '#FFF9F9', '#D77FA1', '#99FEFF', '#94B3FD', '#B983FF']
    data = [trace1, trace2, trace3]
    fig2 = go.Figure(data=data)
    fig2.update_layout(
        margin=dict(l=2, r=2, t=2, b=2),
        paper_bgcolor="#0D213A",  # setup the background color
        plot_bgcolor='rgba(0,0,0,0)'
    )
    fig2.update_traces(marker=dict(colors=colors, line=dict(color='#000000', width=2)))
    fig2.update_layout(font_color="#B8DBEE")
    return fig2

@app.callback(
    Output("indicator", "figure"),
    [Input("tabs", "value")])
def update_indicator(x):
    ex=list(evolution_exportation_annuelle_GU['Total'])[x]
    im=list(evolution_importation_annuelle_GU['Total'])[x]
    balance=float(ex)-float(im)
    fig5 = go.Figure(go.Indicator(
        mode="gauge+number",
        value=balance,
        domain={'x': [0, 1], 'y': [0, 1]},
        gauge={'axis': {'range': [-300000000000, 300000000000], 'tickwidth': 1},
               'bar': {'color': "#B8DBEE"},
               'bordercolor': "#B8DBEE",
               'steps': [
                   {'range': [-300000000000, 0], 'color': '#db1812'},
                   {'range': [0,300000000000], 'color': '#42ed59'}],
               }
    ))
    fig5.update_layout(font_color="#B8DBEE",paper_bgcolor="#0D213A",plot_bgcolor='rgba(0,0,0,0)')
    return fig5


if __name__ == '__main__':
 app.run_server(debug=False)
