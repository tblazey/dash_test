#!/usr/bin/python

#Load libraries
from datetime import datetime, timedelta
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px

#Load in data with pandas
plot_data = pd.read_csv('./temp_data.csv',
                        parse_dates=['Datetime'],
                        dtype={'Temperature': 'float64', 'Status': object})
                       
#Create scanner plot
fig = px.scatter(plot_data,
                 x='Datetime',
                 y='Temperature',
                 color='Status',
                 color_discrete_sequence=['#348cc1', '#e34e21'])
                 
#Update layout
fig.update_traces(marker={'size':12, 'line':{'color':'black', 'width':2}})
fig.update_xaxes(showgrid=True,
                 gridwidth = 1,
                 gridcolor = 'Black',
                 showline = True,
                 linewidth = 3,
                 linecolor = 'black',
                 tickfont = {'color' : 'black', 'size' : 14},
                 ticklen = 10,
                 tickcolor = 'black',
                 ticks = 'outside',
                 range = [plot_data['Datetime'].iloc[-1] - timedelta(hours = 12),
                          plot_data['Datetime'].iloc[-1] + timedelta(hours = 1)])
fig.update_yaxes(showgrid = True,
                 gridwidth = 1,
                 gridcolor = 'Black',
                 showline = True,
                 linewidth = 3,
                 linecolor = 'black',
                 tickfont = {'color':'black', 'size':14},
                 ticklen = 10,
                 tickcolor='black',
                 ticks = 'outside',
                 tick0 = 0.5,
                 nticks = 6,
                 range = [0.0, 2.5],
                 fixedrange = True)
fig.update_layout(dragmode = 'pan',
                  margin={'t':40, 'b':40},
                  autosize=True,
                  plot_bgcolor = 'white',
                  xaxis_title = '<b>Date</b>',
                  xaxis_title_font_color = 'black',
                  xaxis_title_font_size = 20,
                  yaxis_title= '<b>Temperature (K)</b>',
                  yaxis_title_font_color = 'black',
                  yaxis_title_font_size = 20,
                  legend={'y' : 0.1,
                         'title' : '<b>Status</b>',
                         'xanchor' : 'center',
                         'bgcolor' : 'rgba(255, 255, 255, 1)',
                         'bordercolor' : 'black',
                         'borderwidth' : 1.5,
                         'title_font_size' : 16,
                         'title_font_color' : 'black',
                         'font':{'color' :'black', 'size' : 14}})

#Create dash app for showing plot
config = dict({'scrollZoom': True})
app = dash.Dash(__name__, title='Spinlab Temperature')
server = app.server
app.layout = html.Div(
    children=[
        html.Div(className='rows', style={'columnCount':2},
            children=[
                html.Div(className='one columns', style={'width':'100%'},
                    children=[
                        html.H1(style={'text-align': 'center', 'font-size':'1.75vw'},
                            children=[
                                'Spinlab Temperature Log',
                                dcc.Graph(figure=fig, config=config, style={'height': '40vw'})
                            ]
                        )
                    ]
                ),
                html.Div(className='one columns', style={'display': 'inline-block', 'width':'95%'},
                    children=[
                        html.H1(style={'text-align': 'center', 'font-size':'1.75vw'},
                            children=[
                                'Latest CryoStatus Page',
                                html.Img(src=app.get_asset_url('2020-08-28-18-56-27.png'),
                                         style={'max-width': '100%',
                                                'max-height':'100%',
                                                'padding-top':'2vw',
                                                'padding-left':'2vw'})
                            ]
                        )                     
                    ]
                )
            ]
        )
    ]
)

#Run app
if __name__ == '__main__':
    app.run_server()
