#!/usr/bin/env python

import plotly.express as px


if __name__ == "__main__":
    df = px.data.tips()
    fig = px.violin(df, y="total_bill")
    fig.show()
