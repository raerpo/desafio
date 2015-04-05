#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import re

import webapp2
from webapp2_extras import json
import jinja2
import time

from datetime import datetime

from google.appengine.ext import db
from google.appengine.api import users

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),
                               autoescape=True)


def render_str(template, **params):
    t = jinja_env.get_template(template)
    return t.render(params)

def get_user():
        user = users.get_current_user()
        return user

class MainHandler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        return render_str(template, **params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

class MainPage(MainHandler):
    def get(self):
        self.render('index.html')
    def post(self):
        self.response.content_type = 'application/json'
        codigo = self.request.get('codigo')
        if codigo == '7x7mFPcBY4qtI7h':
            validacion = {'equipo': 'liderazgo', 'error_':'false'}
            self.response.write(json.encode(validacion))
        elif codigo == '7J63m3rK7E25MSy':
            validacion = {'equipo': 'trabajo_en_equipo', 'error_':'false'}
            self.response.write(json.encode(validacion))
        elif codigo == '3Fubt76cBRwjTYa':
            validacion = {'equipo': 'orientacion_al_logro', 'error_':'false'}
            self.response.write(json.encode(validacion))
        else:
            validacion = {'equipo': 'ninguno', 'error_':'true'}
            self.response.write(json.encode(validacion))

class MapaLiderazgo(MainHandler):
    def get(self):
        self.render('mapa_liderazgo.html')
    def post(self):
        self.response.content_type = 'application/json'
        punto = self.request.get('punto')
        codigo = self.request.get('codigo')
        if punto == '1' and codigo == '48yB8dH4V58xbRx':
            coordenadas = {'latitud':'4.680569', 'longitud': '-74.047702', 'clave':'true', 'punto':'2'}
            self.response.write(json.encode(coordenadas))
        elif punto == '2' and codigo == 'Ug1195M928451LU':
            coordenadas = {'latitud':'4.676829', 'longitud': '-74.048194', 'clave':'true', 'punto':'3'}
            self.response.write(json.encode(coordenadas))
        else:
            coordenadas = {'latitud':'0', 'longitud': '0', 'clave':'false'}
            self.response.write(json.encode(coordenadas))

class MapaOrientacion(MainHandler):
    def get(self):
        self.render('mapa_orientacion.html')
    def post(self):
        self.response.content_type = 'application/json'
        punto = self.request.get('punto')
        codigo = self.request.get('codigo')
        if punto == '1' and codigo == '8p8B85pkG5q621F':
            coordenadas = {'latitud':'4.679904', 'longitud': '-74.044532', 'clave':'true', 'punto':'2'}
            self.response.write(json.encode(coordenadas))
        elif punto == '2' and codigo == '84321H39689Ih8W':
            coordenadas = {'latitud':'4.676829', 'longitud': '-74.048194', 'clave':'true', 'punto':'3'}
            self.response.write(json.encode(coordenadas))
        else:
            coordenadas = {'latitud':'0', 'longitud': '0', 'clave':'false'}
            self.response.write(json.encode(coordenadas))

class MapaTrabajo(MainHandler):
    def get(self):
        self.render('mapa_trabajo.html')
    def post(self):
        self.response.content_type = 'application/json'
        punto = self.request.get('punto')
        codigo = self.request.get('codigo')
        if punto == '1' and codigo == 'x6jYIE9iH4M59uk':
            coordenadas = {'latitud':'4.682616', 'longitud': '-74.044110', 'clave':'true', 'punto':'2'}
            self.response.write(json.encode(coordenadas))
        elif punto == '2' and codigo == '5D9MS15a4tRd29A':
            coordenadas = {'latitud':'4.676829', 'longitud': '-74.048194', 'clave':'true', 'punto':'3'}
            self.response.write(json.encode(coordenadas))
        else:
            coordenadas = {'latitud':'0', 'longitud': '0', 'clave':'false'}
            self.response.write(json.encode(coordenadas))

app = webapp2.WSGIApplication([('/', MainPage),
                               ('/liderazgo', MapaLiderazgo),
                               ('/orientacion_al_logro', MapaOrientacion),
                               ('/trabajo_en_equipo', MapaTrabajo)],
                              debug=True)