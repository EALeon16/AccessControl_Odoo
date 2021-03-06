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
        buscarcarrera = request.env['accesscontrol.carrera'].sudo().search([('nombre_carrera','=',carrera)])
        listacurso = request.env['accesscontrol.curso'].sudo().search([('nombre_curso','=',nombre)])
        curso = None
        for i in range(len(listacurso)):
          if str(buscarcarrera.id) in str(listacurso[i].carerra_id):
            curso = listacurso[i]
            print(curso)
            break

        if curso is None:    
          request.env['accesscontrol.curso'].sudo().create({
            'nombre_curso':nombre,
            'carerra_id':buscarcarrera.id,
          })

          print('se creo el curso', nombre, carrera)
          return request.redirect('/curso')
        else:
          print('Ya existe ese curso',)
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
        eliminarcurso = request.env['accesscontrol.curso'].sudo().search([('id','=',id)]).sudo().unlink()
        print('Se elimino', id)
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
        buscarcarrera = request.env['accesscontrol.carrera'].sudo().search([('nombre_carrera','=',carrera)])
        editarcurso = request.env['accesscontrol.curso'].sudo().search([('id','=',id)]).sudo().update({
          'nombre_curso':nombre,
          'carerra_id':buscarcarrera.id,
        })
        id = None
        print('Se edito') 
        return request.redirect('/curso')

          
      
              

      
      
      