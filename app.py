from flask import flask
app = Flas(__name__)

@app.route('/')
def index():
  return 'hell from app'
  
  
