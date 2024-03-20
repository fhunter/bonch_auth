#!/usr/bin/python3
# coding=utf-8

""" Main web app module """

import datetime
import bottle
from bottle import view, request, response, static_file, abort, redirect
import settings

app = application = bottle.Bottle()

@app.route(settings.PREFIX + '/')
@view('mainpage')
def main():
    return dict()

@app.route(settings.PREFIX + r'/<filename:re:.*\.css>')
def send_css(filename):
    #DONE
    return static_file(filename, root='./files/', mimetype='text/css')

@app.route(settings.PREFIX + r'/<filename:re:.*\.js>')
def send_js(filename):
    #DONE
    return static_file(filename, root='./files/', mimetype='text/javascript')


if __name__ == '__main__':
    bottle.run(app=app,
        debug=True, reloader=True,
        host='127.0.0.1',
        port=8888)

