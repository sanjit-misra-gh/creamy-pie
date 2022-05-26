from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)

Bootstrap(app)

@app.route('/')
def index():
    return(render_template('index.html'))

@app.route('/trends')
def trends():
    return(render_template('trends.html'))


@app.route('/medicines')
def medicines():
    return(render_template('medicines.html'))


@app.route('/reports')
def reports():
    return(render_template('reports.html'))


@app.route('/settings')
def settings():
    return(render_template('settings.html'))


@app.route('/booktest')
def booktest():
    return(render_template('booktest.html'))
    

@app.route('/contact-us')
def contact():
    return(render_template('contact.html'))


if __name__ == '__main__':
    app.run(host='0.0.0.0')