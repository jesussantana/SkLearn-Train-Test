# Categorical Data

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
%matplotlib inline

df_raw = pd.read_csv('../data/raw/DelayedFlights.csv')
X = df.iloc[:, :-1].values