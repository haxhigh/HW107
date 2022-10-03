import pandas as pd
import plotly.graph_objects as pg

df = pd.read_csv("C:/Users/iliea/OneDrive/Desktop/Code/Python/Hw/Hw107/cups of coffee vs hours of sleep.csv")

print(df.groupby("Coffee in ml")["sleep in hours"].mean())

fig = pg.Figure(pg.bar(x = df.groupby("Coffee in ml")["sleep in hours"].mean(),y = ["1","2","3","4","5","6"],orientation = "h"))
fig.show()