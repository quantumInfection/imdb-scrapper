"""All the functions for section 2 are written here"""

import pandas as pd
import plotly.graph_objects as go


def analyze(csv_filename: str):
    """Generate graphs required"""
    df = pd.read_csv(csv_filename)

    graph_1 = go.Figure(go.Scatter(y=df['Total Ratings'], x=df['Rating Score']))
    graph_1.show()

    graph_2 = go.Figure(go.Scatter(y=df['Budget'], x=df['Rating Score']))
    graph_2.show()

    new_df = df[['Genre', 'Gross USA']].copy()
    new_df.explode('Genre')
    print(new_df.groupby(['Genre']).mean().to_string())



