#!/usr/bin/python

#Load libraries
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
from git import Repo

#Load in data file
plot_data = pd.read_csv('./temp_data.csv',
                        parse_dates=['Datetime'],
                        dtype={'Temperature': 'float64', 'Status': object})
                        
#Add data point
add_frame = pd.DataFrame(dict(Datetime=plot_data['Datetime'].iloc[-1] + timedelta(hours=2),
                              Temperature=0.8,
                              Status='Ready'), index=[0])

#Append data
plot_data = plot_data.append(add_frame, ignore_index=True)

#Write it out
plot_data.to_csv('./temp_data.csv', index=False)

#Commit it
repo = Repo('/Users/blazeyt/Desktop/dash_test/')
repo.index.add('./temp_data.csv')
repo.index.commit('test commit')
origin = repo.remote(name='origin')
origin.push()

                            