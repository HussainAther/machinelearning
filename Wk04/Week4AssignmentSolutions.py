import numpy as np
import pandas as pd
import datetime

def missing_link(x):
    """Define a function that will be passed to calculate() as an argument"""
    return x**2

def filter_DNA(c):
    """
    Accepts one character as an argument
    Returns True if it belongs to the DNA alphabet "ACGT" and False otherwise
    """
    if c in "ACGTacgt":
        return True
    else:
        return False

x = np.linspace(-4*np.pi, 4*np.pi, num=33)
y = []
for number in x:
    if np.isclose(np.sin(number), np.cos(number)):
        y.append(number)

y = np.array(y)

url = "https://github.com/BuzzFeedNews/nics-firearm-background-checks/blob/master/data/nics-firearm-background-checks.csv?raw=true"
guns = pd.read_csv(url)
guns.head()
guns.info()
guns.describe()

guns["year"] = pd.to_datetime(guns["month"], yearfirst=True, format="%Y-%M").dt.year

assert guns['year'].min(), guns['year'].max() == (1998, 2018)

totals_2000 = guns.loc[guns["year"]==2000]["totals"].sum()
totals_2017 = guns.loc[guns["year"]==2017]["totals"].sum()

assert totals_2000 == 8427096
assert totals_2017 == 24955919

states_with_more_long_guns = ((guns.groupby("state")["long_gun"].mean()) > (guns.groupby("state")["handgun"].mean())).sum()
states_with_more_handguns = ((guns.groupby("state")["long_gun"].mean()) < (guns.groupby("state")["handgun"].mean())).sum()

assert states_with_more_long_guns == 37
assert states_with_more_handguns == 18

