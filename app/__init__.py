import pygal
from flask import Flask, render_template, request
from pygal.style import DarkSolarizedStyle

def get_temps () :
    return [ 22,22,22,22,22,22,22,22,22,22,22 ]

def get_times ( scale ) :
    return [ i*scale for i in len( get_temps() ) ]

def get_chart ( title, times, temps ) :
    bar_chart = pygal.Bar( width=1200, height=600, explizite_size=true, title=title, style = DarkSolarizedStyle )
    bar_chart.x_label = times
    bar_chart.add( 'Temperatur in Grad Celsius', temps )
    return bar_chart
  

@app.route("/")
def home_view () :
    scale = 24
    title ='Raumtemperatur der letzten %sh' % scale
    chart = get_chart( title, get_times( scale ), get_temps() )
    return render_template( "project.html", title, chart.render() )

