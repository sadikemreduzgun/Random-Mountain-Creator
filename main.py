import random as rd
from create_mountain import mountain_rising
import numpy as np
import pandas as pd
from create_flat import flat
import plotly.graph_objects as go
from create_area import create_area
from create_hills import hill_type_1


size = 50
area = np.zeros((size, size))
area = flat(area, size)
#print(area)
area = mountain_rising(area, size)

for i in range(0,200):
    x, y = rd.randint(0, 40), rd.randint(0, 40)
    area = hill_type_1(area, x, y)


df = pd.DataFrame(area)
print(df)

my_z_dict = {}

z = area
elements = 1

# filling up my_z_dict dictionary to use as our data-z-values (heights)
for lines in z:
    my_z_dict.update({elements: z[elements - 1]})
    elements += 1

# if you want to see defined dictionary:
# print(my_z_dict)

# loading data into a DataFrame object
loaded_z_DataFrame = pd.DataFrame(my_z_dict)

# to use modules
fig = go.Figure()

"""you can change its color by just write a color scale on of following:
             'aggrnyl', 'agsunset', 'algae', 'amp', 'armyrose', 'balance',
             'blackbody', 'bluered', 'blues', 'blugrn', 'bluyl', 'brbg',
             'brwnyl', 'bugn', 'bupu', 'burg', 'burgyl', 'cividis', 'curl',
             'darkmint', 'deep', 'delta', 'dense', 'earth', 'edge', 'electric',
             'emrld', 'fall', 'geyser', 'gnbu', 'gray', 'greens', 'greys',
             'haline', 'hot', 'hsv', 'ice', 'icefire', 'inferno', 'jet',
             'magenta', 'magma', 'matter', 'mint', 'mrybm', 'mygbm', 'oranges',
             'orrd', 'oryel', 'oxy', 'peach', 'phase', 'picnic', 'pinkyl',
             'piyg', 'plasma', 'plotly3', 'portland', 'prgn', 'pubu', 'pubugn',
             'puor', 'purd', 'purp', 'purples', 'purpor', 'rainbow', 'rdbu',
             'rdgy', 'rdpu', 'rdylbu', 'rdylgn', 'redor', 'reds', 'solar',
             'spectral', 'speed', 'sunset', 'sunsetdark', 'teal', 'tealgrn',
             'tealrose', 'tempo', 'temps', 'thermal', 'tropic', 'turbid',
             'turbo', 'twilight', 'viridis', 'ylgn', 'ylgnbu', 'ylorbr',
             'ylorrd'
             like colorscale='speed' below:"""

# using some modules
fig.add_trace(go.Surface(z=loaded_z_DataFrame.values,
                         colorscale='delta'))
# updating plot sizing
fig.update_layout(
    width=1250,
    height=900,
)

# updating 3D scene options
fig.update_scenes(
    aspectratio=dict(x=1, y=1, z=0.7),
    aspectmode="manual"
)

# adding button
fig.update_layout(
    updatemenus=[
        dict(
            type="buttons",
            direction="left",
            buttons=list([
                dict(
                    args=["type", "surface"],
                    label=f"3D Surface is:",
                    method="restyle"
                ),
                dict(
                    args=["type", "contour"],
                    label=f"Contour line is:",
                    method="restyle"
                )
            ]),
            pad={"r": 10, "t": 10},
            showactive=True,
            x=0.11,
            xanchor="left",
            y=1.1,
            yanchor="top"
        ),
    ]
)

fig.show()
