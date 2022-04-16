from urllib.request import Request
from odoo import http
from odoo.http import request
from odoo.addons.accesscontrol.models.models import Carrera
import json

id = None

class paginaCarrera(http.Controller):
    @http.route([
      '/carrera',  
    ], type='http', auth='public', website=True)
    def main (self, **kwards):
      carrera = request.env['accesscontrol.carrera'].sudo().search([('estado_carrera','=',True)])
      
      context = {
        'c':carrera

      }
      return request.render('accesscontrol.websitecarrera',context)

    @http.route([
      '/guardar_carrera',  
    ], type='http', auth='public', website=True,cors='*',csrf=False)
    def guardarCarrera (self, **post):
        carrera = request.params['nombre_carrera']
        if request.env['accesscontrol.carrera'].sudo().search([('nombre_carrera','=',carrera)]):
          c = request.env['accesscontrol.carrera'].sudo().search([('nombre_carrera','=',carrera)])
          if request.env['accesscontrol.carrera'].sudo().search([('estado_carrera','=',False)]):
            request.env['accesscontrol.carrera'].sudo().search([('id','=',c.id)]).sudo().update({'estado_carrera':True})
            print('ya existe la carrera y se actualizo')
            return request.redirect('/carrera')
          else:
            print('ya existe la carrera')
            return request.redirect('/carrera')
        else:
          request.env['accesscontrol.carrera'].sudo().create(post)
          print('se creo', post)
          return request.redirect('/carrera')
    
    @http.route([
      '/eliminarcarrera',  
    ], type='http', auth='public' , website=True, csrf=False, METHODS= ['POST', 'GET'])
    def eliminarCurso (self, **kw):
      global id
      try:
        carreraid = request.params['id']
        id = carreraid
        buscar = request.env['accesscontrol.carrera'].sudo().search([('id','=',carreraid)])
        context = {
        'b':buscar,

        }
        return request.render('accesscontrol.webeliminarcarrera',context)
      except:
        eliminarcarrera = request.env['accesscontrol.carrera'].sudo().search([('id','=',id)]).sudo().update({'estado_carrera':False})
        print('Se elimino la carrera', id)
        id = None
        return request.redirect('/carrera')



    @http.route([
      '/editarcarrera',  
    ], type='http', auth='public' , website=True, csrf=False, METHODS= ['POST', 'GET'])
    def editarCarrera (self, **kw):
      pasa = False
      global id 
      try:
        fir2 = request.params['id']
        buscarC = request.env['accesscontrol.carrera'].sudo().search([('id','=',fir2)])
        context = {
          'c':buscarC,

        }
        id = fir2
        pasa = True
        return request.render('accesscontrol.webeditarcarrera',context)
      except:
        nombre = request.params['nombre_carrera']
        carreraeliminar2 = request.env['accesscontrol.carrera'].sudo().search([('id','=',id)]).sudo().update({'nombre_carrera':nombre})
        id = None
        print('Error')
      

      #datos = request.field['nombre_carrera']
      
      print('----------self--------', kw,'---------kw--------', '---------request--------',request.httprequest.data)
      if pasa:
        return request.render('accesscontrol.webeditarcarrera',{})
      else:  
        return request.redirect('/carrera')
