#%% Bibliotecas 
from bcb import sgs
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.filters.hp_filter import hpfilter
import datetime as dt
import numpy as np
#importar bases de Selic, IPCA e Núcleo do IPCA
#%% Selic
selic  = sgs.get(432, "2020-01-01",dt.datetime.today())
#%% IPCA
ipca = sgs.get(433, "2020-01-01", dt.datetime.today())
ipca12m = sgs.get(13522, "2020-01-01", dt.datetime.today())
#%% Nucleos do IPCA
cores = [11427, 16121, 27838, 27839, 11426, 4466, 16122, 28751, 28750]
core = sgs.get(cores, "2019-02-01", dt.datetime.today())
core["mean"] = core.mean(axis=1)
core = core[["mean"]].astype(float).round(2)
core12m = core.rolling(window=12).apply(lambda x:(np.prod(1 + x/100) - 1) * 100,
                                        raw=True).dropna().round(2)
#%%
    
