from urllib.request import Request
from odoo import http
from odoo.http import request
from odoo.addons.accesscontrol.models.models import Carrera
id = None


class principalLab(http.Controller):
    @http.route([
      '/horarios',  
    ], type='http', auth='public', website=True)
    def main (self, **kwards):
      lab = request.env['accesscontrol.materia'].sudo().search([('estado_materia','=',True)])
      lab2 = request.env['accesscontrol.carrera'].sudo().search([('estado_carrera','=',True)])
      context = {
        'm':lab,
        'c':lab2

      }
      return request.render('accesscontrol.websitehorario',context)