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
                  plot_bgcolor = 'white',
                  xaxis_title = '<b>Date</b>',
                  xaxis_title_font_color = 'black',
                  xaxis_title_font_size = 20,
                  yaxis_title= '<b>Temperature (K)</b>',
                  yaxis_title_font_color = 'black',
                  yaxis_title_font_size = 20,
                  title = '<b>Spinlab Temperature</b>',
                  title_font_color = 'black',
                  title_font_size = 24,
                  title_x = 0.5,
                  legend={'y' : 0.5,
                         'title' : '<b>Status</b>',
                         'xanchor' : 'center',
                         'bgcolor' : 'rgba(255, 255, 255, 1)',
                         'bordercolor' : 'black',
                         'borderwidth' : 1.5,
                         'title_font_size' : 16,
                         'font':{'color' :'black', 'size' : 14}})

#Create dash app for showing plot
config = dict({'scrollZoom': True})
app = dash.Dash(title='Spinlab Temperature')
server = app.server
app.layout = html.Div([
    dcc.Graph(figure=fig, config=config)
])

#Run app
if __name__ == '__main__':
    app.run_server()
