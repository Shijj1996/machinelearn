import seaborn as sns
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt 

#创造x轴 1，2，3，4，5，6，7，8
x=np.arange(8)
#创造y轴 数据
y=np.array([1,3,4,2,11,3,9,8])

z=np.array([1,2,3,4,5,6,7,8])

#将xy数据格式化到pandas格式的对象 字典
df = pd.DataFrame({"x-axis": x,"y-axis": y,"z-axis":z})

#设置柱状图的data中的xy元素 palette指定色彩模式 
#sns.barplot(x="x-axis",y="z-axis",palette="RdBu_r",data=df)
sns.barplot(x="x-axis",y="y-axis",palette="RdBu_r",data=df)
plt.xticks(rotation=90)
plt.show()