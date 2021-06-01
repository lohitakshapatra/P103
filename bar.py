import plotly.express as px
import pandas as pd

df=pd.read_csv("Copy+of+data+-+data.csv")
fig=px.bar(df,x="date",y="cases",title="cases in a country")
fig.show()