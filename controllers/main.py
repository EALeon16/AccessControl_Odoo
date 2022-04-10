from odoo import http
from odoo.http import request

class prueba(http.Controller):
    @http.route([
      '/accesscontrol',  
    ], type='http', auth='public', website=True,cors='*')
    def main (self):
        return request.render('accesscontrol.website',{})

class vistaPrincipal(http.Controller):
    @http.route([
      '/principal',  
    ], type='http', auth='public', website=True,cors='*')
    def main (self):
        return request.render('accesscontrol.websiteprincipal',{})