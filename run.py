from flask import Flask
from app import app
import pygal

app = Flask( __name__ )

if __name__ == "__main__" :
  app.run( debug=True )
