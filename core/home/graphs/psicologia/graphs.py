import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio
import base64

import pandas as pd
from django.forms.models import model_to_dict

class homeViewGraphs:
    def __init__(self, context, name_context) -> None:
        self.context = context
        self.name_context = name_context

        self.make_data()
    def to_records(self):
        records = [model_to_dict(record) for record in self.context[self.name_context]]

        return records
    def make_data(self):
        records = self.to_records()
        df = pd.DataFrame.from_records(records)

        self.df = df
    
    def values_graph(self,col_name,x_name, y_name ,graph_name, kind='bar'):
        talk = {
            '1': 'Si (Me gustaría hablar al respecto)',
            '2': 'Si (No me gustaría hablar al respecto)',
            '3': 'No'
        }

        if kind == 'pie' and graph_name != 'Humor matutino':
            self.df[col_name] = self.df[col_name].map(talk)

        counts = self.df[col_name].value_counts().reset_index(name='count')
        counts['percent'] = round((counts['count'] / counts['count'].sum()) * 100, 2)


        if kind == 'bar':
            fig = go.Figure(data=go.Bar(x=counts[col_name], y=counts['count'], text=counts['percent']))
            fig.update_layout(
                xaxis_title=x_name,
                yaxis_title=y_name
            )
        elif kind == 'pie':
            fig = go.Figure(data=go.Pie(labels=counts[col_name], values=counts['count'], textinfo='percent+label' ))

        fig.update_layout(
                title=graph_name
            )
        
        
        return fig.to_html(transparent=True)


class JugadorDetailViewGraphs:
    def __init__(self, context, name_context, img=False) -> None:
        self.context = context
        self.name_context = name_context
        self.img = img
        
        self.make_data()

    def to_records(self):
        if self.context[self.name_context] != None:
            records = [model_to_dict(record) for record in self.context[self.name_context]]
        else:
            records = []

        if len(records) != 0:

            for idx, record in enumerate(self.context[self.name_context]):
                records[idx]['created_at'] = record.created_at

        else:
            records = []

        return records
    def make_data(self):
        records = self.to_records()
        if len(records) != 0:
            df = pd.DataFrame.from_records(records)
            self.df = df
        else:
            self.df = []

    
    def lines(self, col_name_x, col_name_y, x_name, y_name, titulo,colors=False):
        if colors:
            color='white'

        else:
            color = 'dimgrey'
        if len(self.df) != 0:
            talk = {
                '1': 'Si (Me gustaría hablar al respecto)',
                '2': 'Si (No me gustaría hablar al respecto)',
                '3': 'No'
            }

            self.df['created_at'] = pd.to_datetime(self.df['created_at']).dt.date

            # Ordena el DataFrame por 'created_at'
            self.df = self.df.sort_values(by='created_at')

            # Crea el gráfico de líneas con Plotly
            fig = px.line(self.df, x=col_name_x, y=col_name_y, markers=True, title=titulo)
            fig.update_xaxes(title_text=x_name)
            fig.update_yaxes(title_text=y_name)
            fig.update_traces(line=dict(color='mediumslateblue'))

            fig.update_xaxes(
                gridcolor=color,  # Color de las reglas
                title_font=dict(color='lightslategray'),  # Color del título del eje X
                tickfont=dict(color='lightslategray'),    # Color de las etiquetas de las marcas del eje X
                tickformat='%Y-%m-%d'  # Formato de fecha deseado (año-mes-día)

            )

            fig.update_yaxes(
                gridcolor=color,  # Color de las reglas
                title_font=dict(color='lightslategray'),  # Color del título del eje Y
                tickfont=dict(color='lightslategray')    # Color de las etiquetas de las marcas del eje Y
            )

            fig.update_layout(
                title=titulo,
                title_font=dict(color='darkseagreen'),  # Color del título de la gráfica
                paper_bgcolor='rgba(0,0,0,0)',  # Establecer el fondo transparente
                plot_bgcolor='rgba(0,0,0,0)'   # Establecer el fondo del gráfico transparente
            )

            if not self.img:
                return fig.to_html(full_html=True)
            

            return  base64.b64encode(pio.to_image(fig, format='png')).decode()


        else:
            return ''

