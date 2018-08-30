import pandas as pd 
import numpy as np
from  sklearn.linear_model import LinearRegression as LR 

y_df=pd.read_csv("bias_score_reg.csv")

y_data=y_df["x-values"].values.tolist()

x_data=[]

for i in range(len(y_data)):
	x_data.append(i)

x_data=np.array(x_data).reshape(-1,1)
y_data=np.array(y_data).reshape(-1,1)

bias_model=LR()

bias_model.fit(x_data, y_data)

print(bias_model.coef_)
