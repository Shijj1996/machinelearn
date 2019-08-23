import numpy as np
import pandas as pd
from pandas import plotting


import matplotlib.pyplot as plt
plt.style.use('seaborn')

import seaborn as sns
sns.set_style('darkgrid')

from sklearn.linear_model import LogisticRegression 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn import svm
from sklearn import metrics 
from sklearn.tree import DecisionTreeClassifier

iris=pd.read_csv('./Iris_data/iris.csv')#,usecols=[1,2,3,4,5])
#print(iris.info)
#print(iris.describe())

# 设置颜色主题
antV = ['#1890FF', '#2FC25B', '#FACC14', '#223273', '#8543E0', '#13C2C2', '#3436c7', '#F04864'] 

# 绘制  Violinplot
    #subplots构造了图表画布的基本对象，以及一些其他属性
f, axes = plt.subplots(2, 2, figsize=(8, 8), sharex=True)
    #？？？不懂
sns.despine(left=True)

    #ax 参数确定了sns会在axe的[x,y]plots的基础上构造图画
sns.violinplot(x='Species', y='Sepal.Length', data=iris, palette=antV, ax=axes[0, 0])
sns.violinplot(x='Species', y='Sepal.Width', data=iris, palette=antV, ax=axes[0, 1])
sns.violinplot(x='Species', y='Petal.Length', data=iris, palette=antV, ax=axes[1, 0])
sns.violinplot(x='Species', y='Petal.Width', data=iris, palette=antV, ax=axes[1, 1])


# 绘制  pointplot
f, axes1 = plt.subplots(2, 2, figsize=(8, 8), sharex=True)
sns.despine(left=True)

sns.pointplot(x='Species', y='Sepal.Length', data=iris, color=antV[0], ax=axes1[0, 0])
sns.pointplot(x='Species', y='Sepal.Width', data=iris, color=antV[1], ax=axes1[0, 1])
sns.pointplot(x='Species', y='Petal.Length', data=iris, color=antV[2], ax=axes1[1, 0])
sns.pointplot(x='Species', y='Petal.Width', data=iris, color=antV[3], ax=axes1[1, 1])


plt.show()