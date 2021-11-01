#Resposta do Exercicio 1 e 1.1

import pandas as pd
import plotly.express as px
import numpy as ny

df = px.data.gapminder().query("country=='Brazil'")

fig = px.line(df,x='year', y= 'lifeExp', labels={'year': 'Anos','lifeExp': 'Espectativa da idade'
},color_discrete_sequence=px.colors.qualitative.Pastel1,template='plotly_white',line_shape="spline")
fig.update_layout(title={'text' : 'Evolução da Expectativa de Vida no Brasil','y': 0.9,'x': 0.5})
fig.update_xaxes(showgrid=False)
fig.update_yaxes(showgrid=False)

fig.show()

df = px.data.gapminder().query("continent=='Americas'")
fig = px.bar(df.query("year==2007"),x=("country"), y="lifeExp", color="country",
labels={'country': 'País','lifeExp': 'Espectativa da idade'
},color_discrete_sequence=px.colors.qualitative.Pastel1,template='plotly_white')
fig.update_layout(title={'text' : 'Expectativa de Vida dos Países do Continente Americano (2007)','y': 0.9,'x': 0.5})


fig.update_xaxes(showgrid=False)
fig.update_yaxes(showgrid=False)
fig.show()

#Resposta do Exercicio 1 e 1.1

df = px.data.gapminder().query("country in ['Brazil', 'Canada','Chile']")

fig = px.line(df, x="lifeExp", y="year", color="country", text="year",
labels={'lifeExp': 'Idade','year': 'Anos'},color_discrete_sequence=px.colors.qualitative.Antique,template='plotly_white')
fig.update_traces(textposition="bottom right")
fig.update_layout(title={'text' :'Expectativa de Vida - Brazil, Cananda e Chile - (1950 - 2010)','y': 1.0,'x': 0.5})
fig.update_xaxes(showgrid=False)
fig.update_yaxes(showgrid=False)
fig.show()


import plotly.express as px


df = px.data.gapminder()

fig = px.scatter(df.query("year==2007"),x=("gdpPercap"), y="lifeExp", color="country",
labels={'lifeExp': 'Expectativa de Idade','gdpPercap': 'Gross Domestic Product','country' : 'País'
},color_discrete_sequence=px.colors.qualitative.D3,template='plotly_white')
fig.update_xaxes(showgrid=False)
fig.update_yaxes(showgrid=False)
fig.show()
