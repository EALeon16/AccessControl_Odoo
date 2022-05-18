from urllib.request import Request
from odoo import http
from odoo.http import request
from odoo.addons.accesscontrol.models.models import Carrera
import json

id = None

class paginaCarrera(http.Controller):
    @http.route([
      '/docentes',  
    ], type='http', auth='public', website=True)
    def main (self, **kwards):
      carrera = request.env['accesscontrol.carrera'].sudo().search([('estado_carrera','=',True)])
      docente = request.env['accesscontrol.docente'].sudo().search([('estado_docente','=',True)])
      
      context = {
        'c':carrera,
        'd':docente,

      }
      return request.render('accesscontrol.websitedocente',context)
    
    @http.route([
      '/guardardocente',  
    ], type='http', auth='public', website=True,cors='*',csrf=False)
    def guardarDocente (self, **post):
      cedula = request.params['cedula_docente']
      nombre= request.params['nombre_docente']
      apellido= request.params['apellido_docente']
      email = request.params['correo_docente']
      tarjeta = request.params['id_tarjeta']
      carrera = request.params['carrera']
      buscarCarrera =request.env['accesscontrol.carrera'].sudo().search([('nombre_carrera','=',carrera)])

      if request.env['accesscontrol.docente'].sudo().search([('cedula_docente','=',cedula)]) or request.env['accesscontrol.docente'].sudo().search([('id_tarjeta','=',tarjeta)]):
        print('Ya existe el docente')
        return request.redirect('/docentes')
      else:
        request.env['accesscontrol.docente'].sudo().create({
          'cedula_docente':cedula,
          'nombre_docente':nombre,
          'apellido_docente':apellido,
          'correo_docente':email,
          'id_tarjeta':tarjeta,
          'carrera_id':buscarCarrera.id,

        })
        print('Docente creado')
        
        return request.redirect('/docentes')

    @http.route([
      '/eliminardocente',  
    ], type='http', auth='public' , website=True, csrf=False, METHODS= ['POST', 'GET'])
    def eliminarDocente (self, **kw):
      global id
      try:
        doc = request.params['id']
        id = doc
        buscar = request.env['accesscontrol.docente'].sudo().search([('id','=',doc)])
        context = {
        'b':buscar,

        }
        return request.render('accesscontrol.webeliminardocente',context)

      except:
        eliminard = request.env['accesscontrol.docente'].sudo().search([('id','=',id)]).sudo().unlink()
        print('Se elimino', id)
        id = None
        return request.redirect('/docentes')

    @http.route([
      '/editardocente',  
    ], type='http', auth='public' , website=True, csrf=False, METHODS= ['POST', 'GET'])
    def editarDocente (self, **kw):
       
      pasa = False
      global id
      try:
        idD = request.params['id']
        carrera = request.env['accesscontrol.carrera'].sudo().search([('estado_carrera','=',True)])
        docente = request.env['accesscontrol.docente'].sudo().search([('id','=',idD)])
        context = {
          'c':carrera,
          'd':docente,

        }
        id = idD
        pasa = True
        return request.render('accesscontrol.webeditardocente',context)
      except:
        cedula = request.params['cedula_docente']
        nombre= request.params['nombre_docente']
        apellido= request.params['apellido_docente']
        email = request.params['correo_docente']
        tarjeta = request.params['id_tarjeta']
        carrera = request.params['carrera']
        buscarCarrera =request.env['accesscontrol.carrera'].sudo().search([('nombre_carrera','=',carrera)])
        request.env['accesscontrol.docente'].sudo().search([('id','=',id)]).sudo().update({
          'cedula_docente':cedula,
          'nombre_docente':nombre,
          'apellido_docente':apellido,
          'correo_docente':email,
          'id_tarjeta':tarjeta,
          'carrera_id':buscarCarrera.id,

        })
        id = None
        print('Se edito', nombre, apellido) 
        return request.redirect('/docentes')