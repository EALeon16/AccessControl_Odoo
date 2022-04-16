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
      
      context = {
        'c':carrera

      }
      return request.render('accesscontrol.websitedocente',context)