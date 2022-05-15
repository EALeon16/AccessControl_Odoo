from urllib.request import Request
from odoo import http
from odoo.http import request
from odoo.addons.accesscontrol.models.models import Carrera
id = None


class principalMateria(http.Controller):
    @http.route([
      '/materia',  
    ], type='http', auth='public', website=True)
    def main (self, **kwards):
      carrera = request.env['accesscontrol.carrera'].sudo().search([('estado_carrera','=',True)])
      materia = request.env['accesscontrol.materia'].sudo().search([('estado_materia','=',True)])
      context = {
        'c':carrera,
        'materia':materia,

      }
      return request.render('accesscontrol.websitmateria',context)

    @http.route([
      '/guardar_materia',  
    ], type='http', auth='public', website=True,cors='*',csrf=False)
    def guardarCarrera (self, **post):
        nombre = request.params['nombre_materia']
        carrera = request.params['carrera']
        buscarcarrera = request.env['accesscontrol.carrera'].sudo().search([('nombre_carrera','=',carrera)])
        buscarmateria =request.env['accesscontrol.materia'].sudo().search([('nombre_materia','=',nombre)])
        buscarmateriaCarrera =request.env['accesscontrol.materia'].sudo().search([('carrera_id','=',buscarcarrera.id)])
        materia = None
        for i in range(len(buscarmateria)):
            if str(buscarcarrera.id) in str(buscarmateria[i].carrera_id):
              materia = buscarmateria[i]
              break
        if materia is None:
          request.env['accesscontrol.materia'].sudo().create({
          'nombre_materia':nombre,
          'carrera_id':buscarcarrera.id,
          })
          print('se creoooooooooooooooooo', nombre, carrera, buscarcarrera.id)
          return request.redirect('/materia')
        else:
          if materia.estado_materia:
            print('Ya existe esta materia', nombre, carrera, materia.id)
            return request.redirect('/curso')
          else:
            request.env['accesscontrol.materia'].sudo().search([('id','=',materia.id)]).sudo().update({'estado_materia':True})
            print('Ya existe esta materia', nombre, carrera, materia.id)
            return request.redirect('/materia')

    @http.route([
      '/eliminarmateria',  
    ], type='http', auth='public' , website=True, csrf=False, METHODS= ['POST', 'GET'])
    def eliminarMateria (self, **kw):
      global id
      try:
        materia = request.params['id']
        id = materia
        buscar = request.env['accesscontrol.materia'].sudo().search([('id','=',materia)])
        context = {
        'b':buscar,

        }
        return request.render('accesscontrol.webeliminarmateria',context)

      except:
        eliminarmateria = request.env['accesscontrol.materia'].sudo().search([('id','=',id)]).sudo().unlink()
        print('Se elimino', id)
        id = None
        return request.redirect('/materia')

    @http.route([
      '/editarmateria',  
    ], type='http', auth='public' , website=True, csrf=False, METHODS= ['POST', 'GET'])
    def editarCarrera (self, **kw):
       
      pasa = False
      global id
      try:
        idmateria = request.params['id']
        carrera = request.env['accesscontrol.carrera'].sudo().search([('estado_carrera','=',True)])
        materia = request.env['accesscontrol.materia'].sudo().search([('id','=',idmateria)])
        context = {
          'c':carrera,
          'm':materia,

        }
        print('carrera',carrera)
        id = idmateria
        pasa = True
        print('carrera',carrera) 
        return request.render('accesscontrol.webeditarmateria',context)
      except:
        nombre = request.params['nombre_materia']
        carrera = request.params['carrera']
        buscarcarrera = request.env['accesscontrol.carrera'].sudo().search([('nombre_carrera','=',carrera)])
        editarmateria = request.env['accesscontrol.materia'].sudo().search([('id','=',id)]).sudo().update({
          'nombre_materia':nombre,
          'carrera_id':buscarcarrera.id,
        })
        id = None
        print('Se edito') 
        return request.redirect('/materia')