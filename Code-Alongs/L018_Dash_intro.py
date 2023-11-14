from dash import Dash, html, dcc, callback, Output, Input

app = Dash(__name__)

# <div>
#     <h1>My dash application</h1>
#     <h2>More info ...</h2>
# </div>

my_H1 = html.H1(children="Fredriks dash application") 
my_H2 = html.H2(children="More info ...")
my_dropdown = dcc.Dropdown(options=["Äpple", "Päron", "Apelsin"], value="Päron")
app.layout = html.Div(children=[my_H1, my_H2, my_dropdown])

@callback(
    Output(my_H2, component_property="children"),
    Input(my_dropdown, component_property="value")
)
def update_heading2(fruit):
    return fruit.upper()

app.run(host="0.0.0.0", debug=True)