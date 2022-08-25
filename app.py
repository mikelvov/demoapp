from dash import Dash, html, dcc, dash_table, Input, Output
# import dash_auth
import pandas as pd
from datetime import datetime, timedelta, date

VALID_USERNAME_PASSWORD_PAIRS = {
    'hello': '0000'
}

white_button_style = {'Align': 'center',
                      'textAlign': 'center',
                      'background-color': 'white',
                      'color': 'black',
                      'height': '75px',
                      'width': '150px',
                      'border-radius' : '10px',
                      }

app = Dash(__name__)
# auth = dash_auth.BasicAuth(
#     app,
#     VALID_USERNAME_PASSWORD_PAIRS
# )

app.layout = html.Div(children=[
    html.H1('Tasks queue', style={'textAlign': 'center'}),
    html.Button('Click to refresh table', id='button', style=white_button_style),
    html.Div(id='body-div'),
    html.H2(id='calendar_table')
    # dash_table.DataTable(id='datatable'),
    # dcc.Markdown('''Dash and Markdown''')
])

@app.callback(
    Output(component_id='calendar_table', component_property='children'),
    Output(component_id='body-div', component_property='children'),
    Input(component_id='button', component_property='n_clicks')
)
def update_output(n_clicks):
    if n_clicks is None:
        return None, None
    else:
        now = datetime.now()
        time = [now + timedelta(minutes=-3),
                now + timedelta(minutes=-2),
                now + timedelta(minutes=-1)]
        df = pd.DataFrame({
            "Number": [1, 2, 3],
            "Chat": ["chat_name", "chat_name", "chat_name"],
            "link": ['url', 'url', 'url'],
            "Time": [time[0].strftime("%Y-%m-%d %H:%M:%S"),
                     time[1].strftime("%Y-%m-%d %H:%M:%S"),
                     time[2].strftime("%Y-%m-%d %H:%M:%S")]
        })
        str = "Now time : " + now.strftime("%H:%M:%S")
        return dash_table.DataTable(data=df.to_dict('records')), str


if __name__ == '__main__':
    app.run_server(debug=True)