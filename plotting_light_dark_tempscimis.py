#!/usr/bin/python
#above tells where python is
import sys #import module sys to capture arguments from terminal that we want to use in python program
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
def plotting_light_dark_tempscimis(ID):
    ''' Return plots of temp over time.
    First loads in data, error_bad_lines = False ignores bad lines, parse_dates combines date and hour columns into single column
    Second selects only data referring to stationID
    Creates two subsets from above using sol radiance > 0 or =0
    finally plots first using a empty figure
    figure 1 is plot of air temp over time during light hours
    figure 2 is plot of air temp over temp in night hours
    fig 3 is difference of air soil temp at night hours over time

    @param filename = n-dimensional array of values
    @param stationID = stationID of location of interest

    Examples
    ----------
    >>>>>>>>>
    '''
    data = pd.read_csv('hourly(2).csv', error_bad_lines=False, parse_dates = [['Date', 'Hour (PST)']])
    specificcity = data.loc[data['Stn Id'] == ID]
    specificcitylighttemps = specificcity.loc[specificcity['Sol Rad (Ly/day)'] > 0]
    specificcitydarktemps = specificcity.loc[specificcity['Sol Rad (Ly/day)'] == 0]
    specificcitydarktemps['difference'] = specificcitydarktemps['Air Temp (F)'] - specificcitydarktemps['Soil Temp (F)']
    #warnings.simplefilter(action = 'ignore', category = FutureWarning) #ignorning future warning not sure what it is
    print('hellorob')
    fig = plt.figure(figsize = (10.0, 3.0))
    axes1 = fig.add_subplot(1,3,1)
    axes2 = fig.add_subplot(1,3,2)
    axes3 = fig.add_subplot(1,3,3)
    axes1.plot(specificcitylighttemps['Date_Hour (PST)'], specificcitylighttemps['Air Temp (F)'])
    axes2.plot(specificcitydarktemps['Date_Hour (PST)'], specificcitydarktemps['Air Temp (F)'])
    axes3.plot(specificcitydarktemps['Date_Hour (PST)'], specificcitydarktemps['difference'])
    return plt.show()
if __name__ == "__main__":
    ID = int(sys.argv[1])
    plotting_light_dark_tempscimis(ID)
 #tells when ran by itself take inputs from command line
