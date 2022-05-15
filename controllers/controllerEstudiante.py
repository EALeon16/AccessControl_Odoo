from urllib.request import Request
from odoo import http
from odoo.http import request
from odoo.addons.accesscontrol.models.models import Carrera
import json

id = None

class paginaEstudiante(http.Controller):
    @http.route([
      '/estudiantes',  
    ], type='http', auth='public', website=True)
    def main (self, **kwards):
      estudiante = request.env['accesscontrol.estudiante'].sudo().search([('estado_estudiante','=',True)])
      curso = request.env['accesscontrol.curso'].sudo().search([('estado_curso','=',True)])
      
      context = {
        'e':estudiante,
        'curso':curso

      }
      return request.render('accesscontrol.websiteestudiante',context)


    
    @http.route([
      '/guardarestudiante',  
    ], type='http', auth='public', website=True,cors='*',csrf=False)
    def guardarEstudiante (self, **post):
      cedula = request.params['cedula_estudiante']
      nombre= request.params['nombre_estudiante']
      apellido= request.params['apellido_estudiante']
      tarjeta = request.params['id_tarjeta']
      curso = request.params['curso']
      buscarCurso =request.env['accesscontrol.curso'].sudo().search([('nombre_curso','=',curso)])
      request.env['accesscontrol.estudiante'].sudo().create({
        'cedula_estudiante':cedula,
        'nombre_estudiante':nombre,
        'apellido_estudiante':apellido,
        'id_tarjeta':tarjeta,
        'curso_id':buscarCurso.id,

      })
      
      
      return request.redirect('/estudiantes')


    @http.route([
      '/eliminarestudiante',  
    ], type='http', auth='public' , website=True, csrf=False, METHODS= ['POST', 'GET'])
    def eliminarestudiante (self, **kw):
      global id
      try:
        est = request.params['id']
        id = est
        buscar = request.env['accesscontrol.estudiante'].sudo().search([('id','=',est)])
        context = {
        'b':buscar,

        }
        return request.render('accesscontrol.webeliminarestudiante',context)

      except:
        eliminarest = request.env['accesscontrol.estudiante'].sudo().search([('id','=',id)]).sudo().unlink()
        print('Se elimino', id)
        id = None
        return request.redirect('/estudiantes')
    
    @http.route([
      '/editarestudiante',  
    ], type='http', auth='public' , website=True, csrf=False, METHODS= ['POST', 'GET'])
    def editarEstudiante (self, **kw):
       
      pasa = False
      global id
      try:
        idest = request.params['id']
        curso = request.env['accesscontrol.curso'].sudo().search([('estado_curso','=',True)])
        estudiante = request.env['accesscontrol.estudiante'].sudo().search([('id','=',idest)])
        context = {
          'c':curso,
          'e':estudiante,

        }
        print('estudiante',estudiante)
        id = idest
        pasa = True
        print('estudiante',estudiante) 
        return request.render('accesscontrol.webeditarestudiante',context)
      except:
        cedula = request.params['cedula_estudiante']
        nombre= request.params['nombre_estudiante']
        apellido= request.params['apellido_estudiante']
        tarjeta = request.params['id_tarjeta']
        curso = request.params['curso']
        buscarCurso =request.env['accesscontrol.curso'].sudo().search([('nombre_curso','=',curso)])
        request.env['accesscontrol.estudiante'].sudo().search([('id','=',id)]).sudo().update({
          'cedula_estudiante':cedula,
          'nombre_estudiante':nombre,
          'apellido_estudiante':apellido,
          'id_tarjeta':tarjeta,
          'curso_id':buscarCurso.id,

        })
        id = None
        print('Se edito', nombre, apellido) 
        return request.redirect('/estudiantes')