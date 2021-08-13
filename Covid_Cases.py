import sys
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("USA Covid Data.csv")

data.isna().sum() #check for missing values

dataT = data.dropna() #drops any missing values from the table

cases_by_state = dataT.groupby('State')['Total Cases'].sum() #creates a series of 

S_unique = list(data.State.unique()) #gets the unique states

cases_by_state = cases_by_state.reindex(S_unique, axis = 0) #keeps the state in its original order

cases_by_state = cases_by_state.to_frame() #converts the series to a dataframe

cases_by_state.reset_index(level = 0, inplace = True) # corrects the dataframe so the States are not in the index location

print(cases_by_state.dropna()) #Displays the new dataframe with null values removed from the table

plt.figure(figsize = (50,50))

plt.bar (
    data['State'],
    data['Total Cases'],
    color = (0.7,0.6,0.5,0.9)
)

plt.suptitle('Covid Data By State', fontsize = 20)
plt.title('Covid Cases By State', fontsize = 20)
plt.xlabel('State', fontsize = 20)
plt.ylabel('Total Cases (in millions)', fontsize = 20)

for x, case in enumerate(cases_by_state['Total Cases']):

    plt.text(x,
             case + 10000,
             case,
             ha = 'center',
             fontsize = 9)

plt.setp(plt.gca().get_xticklabels(),
         rotation = 80,
         horizontalalignment = 'right',
         fontsize = 20)

plt.setp(plt.gca().get_yticklabels('Total Cases'), fontsize=20) #This code sets the y and x axis tick label alignments, specifically the rotation

plt.show() #generates the bar chart, some of the numbers do not appear above the bar because the values were listed as NaN and were dropped earlier