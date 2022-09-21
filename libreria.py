from ast import Index
from bokeh.io import curdoc
import pandas as pd
from bokeh.sampledata.gapminder import fertility, life_expectancy
from bokeh.layouts import row, column
from bokeh.models import  Select, TextInput,  ColumnDataSource
from bokeh.plotting import figure, show

columns = list(fertility.columns)


years = [int(year) for year in columns]
years_etiqueta = [str(x) for x in years]
Co = list(fertility.index)
Coun = [str(y) for y in Co]
rename_dict = dict(zip(columns, years))
fertility = fertility.rename(columns=rename_dict)
life_expectancy = life_expectancy.rename(columns=rename_dict)

df = pd.Series(Coun)
años = Select(title="Año", options=years_etiqueta)

a = years[45]
b = years[49]
#source = ColumnDataSource(data=dict(
#    desc=['Afghanistan', 'Albania', 'Algeria', 'American Samoa', 'Andorra', 'Angola', 'Anguilla', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'British Virgin Islands', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Cayman Islands', 'Central African Rep.', 'Chad', 'Channel Islands', 'Chile', 'China', 'Christmas Island', 'Cocos Island', 'Colombia', 'Comoros', 'Congo, Dem. Rep.', 'Congo, Rep.', 'Cook Islands', 'Costa Rica', "Cote d'Ivoire", 'Croatia', 'Cuba', 'Cyprus', 'Czech Rep.', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Rep.', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Faeroe Islands', 'Falkland Islands (Malvinas)', 'Fiji', 'Finland', 'France', 'French Guiana', 'French Polynesia', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guadeloupe', 'Guam', 'Guatemala', 'Guernsey', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Holy See', 'Honduras', 'Hong Kong, China', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Isle of Man', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jersey', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Korea, Dem. Rep.', 'Korea, Rep.', 'Kosovo', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macao, China', 'Macedonia, FYR', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Martinique', 'Mauritania', 'Mauritius', 'Mayotte', 'Mexico', 'Micronesia, Fed. Sts.', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Montserrat', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'Netherlands Antilles', 'New Caledonia', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Niue', 'Norfolk Island', 'Northern Cyprus', 'Northern Mariana Islands', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Pitcairn', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Reunion', 'Romania', 'Russia', 'Rwanda', 'Saint Barth�lemy', 'Saint Helena', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Martin', 'Saint Vincent and the Grenadines', 'Saint-Pierre-et-Miquelon', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Serbia excluding Kosovo', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovak Republic', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Sudan', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Svalbard', 'Swaziland', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Timor-Leste', 'Togo', 'Tokelau', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Turks and Caicos Islands', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 'Wallis et Futuna', 'Vanuatu', 'Venezuela', 'West Bank and Gaza', 'Western Sahara', 'Vietnam', 'Virgin Islands (U.S.)', 'Yemen, Rep.', 'Zambia', 'Zimbabwe', '�land'],
#))

source = ColumnDataSource(dict(Coun = Coun))

TOOLTIPS = [
    ("Pais", "$index"),
    ("Pais", "Coun"),
    ("Indice de fertilidad", "@x"),
    ("Expectativa de vida", "@y")
]

plot = figure(title="Relación del indice de fertilidad con la expectativa de vida de los paises", x_axis_label="Indice de Fertilidad", y_axis_label="Expectativa de Vida",width=800, height=800, tooltips=TOOLTIPS)
plot.toolbar_location = "below"
plot.background_fill_color = "lightgrey"
plot.border_fill_color = "lightgrey"

x1 = fertility[b]
y1 = life_expectancy[b]
x2 = fertility[a]
y2 = life_expectancy[a]

plot.circle_dot(x1, y1, legend=years_etiqueta[49] ,size=20, color="purple", alpha=0.3)
plot.triangle_dot(x2, y2, legend=years_etiqueta[44], size=20, color="green", alpha=0.3)



plot.hover.point_policy = "follow_mouse"

mostrar = row(plot, años)
plot.legend.title = "Años"

#show(mostrar)
show(plot)
