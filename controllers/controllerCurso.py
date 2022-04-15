from urllib.request import Request
from odoo import http
from odoo.http import request
from odoo.addons.accesscontrol.models.models import Carrera
id = None


class principalCurso(http.Controller):
    @http.route([
      '/curso',  
    ], type='http', auth='public', website=True)
    def main (self, **kwards):
      carrera = request.env['accesscontrol.carrera'].sudo().search([('estado_carrera','=',True)])
      curso = request.env['accesscontrol.curso'].sudo().search([('estado_curso','=',True)])
      context = {
        'c':carrera,
        'curso':curso,

      }
      return request.render('accesscontrol.websitecurso',context)

    @http.route([
      '/guardar_curso',  
    ], type='http', auth='public', website=True,cors='*',csrf=False)
    def guardarCarrera (self, **post):
        nombre = request.params['nombre_curso']
        carrera = request.params['carrera']
        request.env['accesscontrol.curso'].sudo().create({
          'nombre_curso':nombre,
          'carerra_id':carrera,
        })

        print('se creoooooooooooooooooo', nombre, carrera)
        return request.redirect('/curso')

    @http.route([
      '/eliminarcurso',  
    ], type='http', auth='public' , website=True, csrf=False, METHODS= ['POST', 'GET'])
    def eliminarCarrera (self, **kw):
      global id
      try:
        carrera = request.params['id']
        id = carrera
        buscar = request.env['accesscontrol.curso'].sudo().search([('id','=',carrera)])
        context = {
        'b':buscar,

        }
        return request.render('accesscontrol.webeliminarcurso',context)

      except:
        eliminarcurso = request.env['accesscontrol.curso'].sudo().search([('id','=',id)]).sudo().update({'estado_curso':False})
        print('dasdasdadasdasdadasdasdadasdadasdasd', id)
        id = None
        return request.redirect('/curso')


    @http.route([
      '/editarcurso',  
    ], type='http', auth='public' , website=True, csrf=False, METHODS= ['POST', 'GET'])
    def editarCarrera (self, **kw):
       
      pasa = False
      global id
      try:
        idcurso = request.params['id']
        carrera = request.env['accesscontrol.carrera'].sudo().search([('estado_carrera','=',True)])
        curso = request.env['accesscontrol.curso'].sudo().search([('id','=',idcurso)])
        context = {
          'c':carrera,
          'curso':curso,

        }
        print('carrera',carrera)
        id = idcurso
        pasa = True
        print('carrera',carrera) 
        return request.render('accesscontrol.webeditarcurso',context)
      except:
        nombre = request.params['nombre_curso']
        carrera = request.params['carrera']
        editarcurso = request.env['accesscontrol.curso'].sudo().search([('id','=',id)]).sudo().update({
          'nombre_curso':nombre,
          'carerra_id':carrera,
        })
        id = None
        print('Se edito') 
        return request.redirect('/curso')

          
      
              

      
      
      