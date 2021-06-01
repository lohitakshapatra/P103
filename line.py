import plotly.express as px
import pandas as pd

df=pd.read_csv("Copy+of+data+-+data.csv")
fig=px.line(df,x="country",y="cases",color="country",title="cases")
fig.show()