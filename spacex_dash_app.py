# Импорт необходимых библиотек
import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Чтение данных о запусках SpaceX в pandas dataframe
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# Создание Dash приложения
app = dash.Dash(__name__)

# Создание макета приложения
app.layout = html.Div(children=[
    html.H1('SpaceX Launch Records Dashboard',
            style={'textAlign': 'center', 'color': '#503D36', 'font-size': 40}),
    # TASK 1: Добавление выпадающего списка для выбора места запуска
    # Значение по умолчанию - ALL для всех мест
    dcc.Dropdown(
        id='site-dropdown',
        options=[
            {'label': 'All Sites', 'value': 'ALL'},
            {'label': 'CCAFS LC-40', 'value': 'CCAFS LC-40'},
            {'label': 'CCAFS SLC-40', 'value': 'CCAFS SLC-40'},
            {'label': 'KSC LC-39A', 'value': 'KSC LC-39A'},
            {'label': 'VAFB SLC-4E', 'value': 'VAFB SLC-4E'}
        ],
        value='ALL',
        placeholder="Select a Launch Site here",
        searchable=True
    ),
    html.Br(),
    
    # TASK 2: Добавление круговой диаграммы для отображения общего количества успешных запусков для всех мест
    # Если выбрано конкретное место запуска, показать количества успешных и неуспешных запусков для этого места
    html.Div(dcc.Graph(id='success-pie-chart')),
    html.Br(),

    # TASK 3: Добавление ползунка для выбора диапазона нагрузки
    dcc.RangeSlider(
        id='payload-slider',
        min=min_payload,
        max=max_payload,
        step=1000,
        marks={min_payload: str(min_payload), max_payload: str(max_payload)},
        value=[min_payload, max_payload]
    ),
    html.P("Payload range (Kg):"),
    html.Br(),

    # TASK 4: Добавление точечной диаграммы для отображения корреляции между нагрузкой и успешностью запуска
    html.Div(dcc.Graph(id='success-payload-scatter-chart')),
])

# TASK 2 & 4: Добавление функций обратного вызова
@app.callback(
    [Output(component_id='success-pie-chart', component_property='figure'),
     Output(component_id='success-payload-scatter-chart', component_property='figure')],
    [Input(component_id='site-dropdown', component_property='value'),
     Input(component_id='payload-slider', component_property='value')]
)
def update_charts(entered_site, payload_range):
    # Фильтрация dataframe на основе выбранного места запуска
    if entered_site == 'ALL':
        filtered_df = spacex_df
    else:
        filtered_df = spacex_df[spacex_df['Launch Site'] == entered_site]

    # Фильтрация dataframe на основе диапазона нагрузки
    filtered_df = filtered_df[(filtered_df['Payload Mass (kg)'] >= payload_range[0]) & 
                              (filtered_df['Payload Mass (kg)'] <= payload_range[1])]

    # Круговая диаграмма для количества успешных запусков
    pie_fig = px.pie(filtered_df, names='class', title='Success Launches')
    
    # Точечная диаграмма для нагрузки и успешности запуска
    scatter_fig = px.scatter(filtered_df, x='Payload Mass (kg)', y='class', color='Booster Version Category',
                             title='Payload vs. Launch Success')
    
    return pie_fig, scatter_fig

# Запуск приложения
if __name__ == '__main__':
    app.run_server()
