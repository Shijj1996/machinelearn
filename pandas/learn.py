import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

fp = pd.read_csv('./pandas/tongji.csv')
#print(fp.describe(include='all'))
print(fp.head(1)['Time'][0])
print(fp.columns)


