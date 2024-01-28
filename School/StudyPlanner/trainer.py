import pandas as pd
import numpy as np

df = pd.read_csv("/home/sarthak/Documents/Automation/School/StudyPlanner/train.csv")
print(np.array(df[0:10]))
