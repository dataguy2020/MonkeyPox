# !/usr/bin/env python
author = "Michael Brown"
license = "Based off of sript by Sreenivas Bhattiprolu of Python for Microscopists"

import pandas as pd
import datetime as dt
from matplotlib import pyplot as plt
from datetime import timedelta
import seaborn as sns


from warnings import simplefilter
simplefilter(action="ignore", category=pd.errors.PerformanceWarning)

monkeypox = pd.read_csv('https://raw.githubusercontent.com/dataguy2020/MonkeyPox/main/dataset/UnitedStates/States/Maryland/CountyCases.csv')

monkeypox['DATE'] = [dt.datetime.strptime(x, '%m/%d/%Y')
        for x in monkeypox['DATE']]

monkeypox['AlleganyWeeklyCases'] = monkeypox['Allegany'].diff()
monkeypox['AnneArundelWeeklyCases'] = monkeypox['Anne_Arundel'].diff()
monkeypox['BaltimoreWeeklyCases'] = monkeypox['Baltimore'].diff()
monkeypox['BaltimoreCityWeeklyCases'] =  monkeypox['Baltimore_City'].diff()
monkeypox['CalvertWeeklyCases'] = monkeypox['Calvert'].diff()
monkeypox['CarolineWeeklyCases'] = monkeypox['Caroline'].diff()
monkeypox['CarrollWeeklyCases'] = monkeypox['Carroll'].diff()
monkeypox['CecilWeeklyCases'] = monkeypox['Cecil'].diff()
monkeypox['CharlesWeeklyCases'] = monkeypox['Charles'].diff()
monkeypox['DorchesterWeeklyCases'] = monkeypox['Dorchester'].diff()
monkeypox['FrederickWeklyCases'] = monkeypox['Frederick'].diff()


#Debug
print(monkeypox.dtypes)

