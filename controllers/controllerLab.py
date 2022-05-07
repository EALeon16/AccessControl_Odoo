from urllib.request import Request
from odoo import http
from odoo.http import request
from odoo.addons.accesscontrol.models.models import Carrera
id = None


class principalLab(http.Controller):
    @http.route([
      '/lab',  
    ], type='http', auth='public', website=True)
    def main (self, **kwards):
      lab = request.env['accesscontrol.lab'].sudo().search([('estado_lab','=',True)])
      self.warning = False
      print('waaaaaaaaaaaaaaaaaaaarrrrrnnnnnnniiiiiing', self.warning)
      context = {
        'lab':lab,
        'warning':self.warning

      }
      return request.render('accesscontrol.websitelab',context)

    @http.route([
      '/guardarlab',  
    ], type='http', auth='public', website=True,cors='*',csrf=False)
    def guardarLab (self, **post):
        codigo = request.params['codigo_lab']
        nombre = request.params['nombre_lab']
        clave = request.params['clave_llave']
        if request.env['accesscontrol.lab'].sudo().search([('codigo_lab','=',codigo)]):
          c = request.env['accesscontrol.lab'].sudo().search([('codigo_lab','=',codigo)])
          if request.env['accesscontrol.lab'].sudo().search([('estado_lab','=',False)]):
            request.env['accesscontrol.lab'].sudo().search([('id','=',c.id)]).sudo().update({'estado_lab':True})
            print('ya existe el lab y se actualizo')
            return request.redirect('/lab')
          else:
            print('ya existe el lab')
            return request.redirect('/lab')
        else:
          request.env['accesscontrol.lab'].sudo().create(post)
          print('se creo', post)
          return request.redirect('/lab')

    @http.route([
      '/eliminarlab',  
    ], type='http', auth='public' , website=True, csrf=False, METHODS= ['POST', 'GET'])
    def eliminarLab (self, **kw):
      global id
      try:
        lab = request.params['id']
        id = lab
        buscar = request.env['accesscontrol.lab'].sudo().search([('id','=',lab)])
        context = {
        'b':buscar,

        }
        return request.render('accesscontrol.webeliminarlab',context)

      except:
        eliminarlab = request.env['accesscontrol.lab'].sudo().search([('id','=',id)]).sudo().update({'estado_lab':False})
        print('Se elimino', id)
        id = None
        return request.redirect('/lab')

    @http.route([
      '/editarlab',  
    ], type='http', auth='public' , website=True, csrf=False, METHODS= ['POST', 'GET'])
    def editarLab (self, **kw):
       
      pasa = False
      global id
      try:
        idlab = request.params['id']
        buscarlab = request.env['accesscontrol.lab'].sudo().search([('id','=',idlab)])
        context = {
          'lab':buscarlab,

        }
        id = idlab
        pasa = True
        print('lab', buscarlab) 
        return request.render('accesscontrol.webeditarlab',context)
      except:
        codigo = request.params['codigo_lab']
        nombre = request.params['nombre_lab']
        estado = request.params['clave_puerta']
        clave = request.params['clave_llave']
        editarlab = request.env['accesscontrol.lab'].sudo().search([('id','=',id)]).sudo().update({
          'codigo_lab':codigo,
          'nombre_lab':nombre,
          'estado_puerta':estado,
          'clave_llave':clave,
        })
        id = None
        print('Se edito', codigo, nombre, estado,clave) 
        return request.redirect('/lab')