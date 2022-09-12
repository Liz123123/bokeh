from ast import Index
from turtle import update
import pandas as pd
from bokeh.sampledata.gapminder import fertility, life_expectancy
from bokeh.layouts import row, column
from bokeh.models import  Select, TextInput,  ColumnDataSource
from bokeh.plotting import figure, show

df = pd.DataFrame(fertility)
años = Select(title="Año", options=sorted(fertility))
cast = TextInput(title="Valor")

b = "1964"
año = años.value
colums_name = df.index.values
source = ColumnDataSource(data=dict(fertility=[]))


TOOLTIPS = [
    ("Pais", "$index"),
    ("Pais", "@source"),
    ("Indice de fertilidad", "@x"),
    ("Expectativa de vida", "@y")
]

plot = figure(width=800, height=800, tooltips=TOOLTIPS)

x1 = fertility[b]
y1 = life_expectancy[b]

plot.circle_dot(x1, y1, size=20, color="purple", alpha=0.3)



plot.hover.point_policy = "follow_mouse"

mostra = row(plot, column(años, cast))

show(mostrar)
