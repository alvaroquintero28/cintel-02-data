import plotly.express as px
from shiny.express import input, ui
from shinywidgets import render_plotly
import palmerpenguins  # this package provides the Palmer Penguins dataset

# use the built in function to load the Palmer Penguins dataset
penguins_df = palmerpenguins.load_penguins()

ui.page_opts(title="Alvaro's King Penguin data", fillable=True)
with ui.layout_columns():

    @render_plotly
    def plot1():
        return px.histogram(px.data.tips(), y="tip")

    @render_plotly
    def plot2():
        return px.histogram(px.data.tips(), y="total_bill")

