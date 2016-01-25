from flask import Flask, render_template, request
from flask.ext.sqlalchemy import SQLAlchemy
import pygal
from pygal.style import DarkSolarizedStyle

app = Flask( __name__ )

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


def get_temps () :
    return [ 22,21,21,22,23,24,23,22,21,22,22 ]

def get_times ( scale ) :
    return [ [ float( i*scale ) for i in range( len( get_temps() ) ) ]]

def get_chart ( title, times, temps ) :
    bar_chart = pygal.Bar( width=1200, height=600, explizite_size=True, title=title, style = DarkSolarizedStyle, disable_xml_declaration=True )
    bar_chart.x_label = times
    bar_chart.add( 'Temperatur in Grad Celsius', temps )
    return bar_chart

@app.route("/")
def home_view () :
    return render_template( "base.html" )

@app.route( "/temperature" )
def temp_view () :
    scale = 24
    title ='Raumtemperatur der letzten %sh' % scale
    chart = get_chart( title, get_times( scale ), get_temps() )
    return render_template( "project.html", title=title, chart=chart )

@app.route( "/bootstrap" )
def bootstrap () :
    return render_template( "bootstrap.html" ) 
