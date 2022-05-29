from flask import Flask, render_template
from flask import Blueprint

controller = Blueprint('controller', __name__)


@controller.route('/controller')
def index():
    return(render_template('index.html'))

@controller.route('/trends')
def trends():
    return(render_template('trends.html'))


@controller.route('/medicines')
def medicines():
    return(render_template('medicines.html'))


@controller.route('/reports')
def reports():
    return(render_template('reports.html'))


@controller.route('/settings')
def settings():
    return(render_template('settings.html'))


@controller.route('/booktest')
def booktest():
    return(render_template('booktest.html'))
    

@controller.route('/contact-us')
def contact():
    return(render_template('contact.html'))