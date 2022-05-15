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
      lab = request.env['accesscontrol.lab'].sudo().search([('estado_lab','=',True)])
      lab2 = request.env['accesscontrol.carrera'].sudo().search([('estado_carrera','=',True)])
      carrera = request.env['accesscontrol.carrera'].sudo().search([('estado_carrera','=',True)])
      materia = request.env['accesscontrol.materia'].sudo().search([('estado_materia','=',True)])
      curso = request.env['accesscontrol.curso'].sudo().search([('estado_curso','=',True)])
      docente = request.env['accesscontrol.docente'].sudo().search([('estado_docente','=',True)])
      horario = request.env['accesscontrol.horario'].sudo().search([('estado_horario','=',True)])
      context = {
        'lab':lab,
        'c':lab2,
        'carrera':carrera,
        'materia':materia,
        'curso':curso,
        'docente':docente,
        'h':horario,
        

      }
      print('diaaaaaaaaaaaaaaaaaaa',horario)
      return request.render('accesscontrol.websitehorario',context)
    @http.route([
      '/guardarhorario',  
    ], type='http', auth='public', website=True,cors='*',csrf=False)
    def guardarHorario (self, **post):
      hora_inicio = request.params['hora_inicio']
      hora_fin= request.params['hora_fin']
      dia= request.params['dia']
      lab = request.params['lab']
      carrera = request.params['carrera']
      materia= request.params['materia']
      curso = request.params['curso']
      docente = request.params['docente']
      buscarCarrera =request.env['accesscontrol.carrera'].sudo().search([('nombre_carrera','=',carrera)])
      buscarLab =request.env['accesscontrol.lab'].sudo().search([('nombre_lab','=',lab)])
      buscarMateria =request.env['accesscontrol.materia'].sudo().search([('nombre_materia','=',materia)])
      buscarCurso =request.env['accesscontrol.curso'].sudo().search([('nombre_curso','=',curso)])
      buscarDocente =request.env['accesscontrol.docente'].sudo().search([('nombre_docente','=',docente)])
      aux = None
      listaHorario = request.env['accesscontrol.horario'].sudo().search([('estado_horario','=',True)])
      print('Print fuera del for',listaHorario)
      for i in range(len(listaHorario)):
        print('Print fuera del if',listaHorario[i])
        if dia in listaHorario[i].dia and str(buscarLab.id) in str(listaHorario[i].lab_id):
          print('Print dentro del if compara hora inicio',listaHorario[i])
          if (hora_inicio >= listaHorario[i].hora_inicio and hora_inicio <= listaHorario[i].hora_fin) and (hora_fin >= listaHorario[i].hora_inicio and hora_fin <= listaHorario[i].hora_fin):
            print('La hora inicial esta entre hora inicial y final existente',listaHorario[i],aux)
            aux = listaHorario[i]
            break
          elif (hora_fin >= listaHorario[i].hora_inicio and hora_fin <= listaHorario[i].hora_fin):
            print('La hora final esta entre hora inicial y final existente',listaHorario[i],aux)
            aux = listaHorario[i]
            break
        else:
          aux = None
      if aux is None:
            request.env['accesscontrol.horario'].sudo().create({
            'hora_inicio':hora_inicio,
            'hora_fin':hora_fin,
            'dia':dia,
            'lab_id':buscarLab.id,
            'carrera_id':buscarCarrera.id,
            'materia_id':buscarMateria.id,
            'curso_id':buscarCurso.id,
            'docente_id':buscarDocente.id,

            })
            print('Se creo el horarioo')
            return request.redirect('/horarios')
            
      else:
          print('Horario ocupado')
          return request.redirect('/carrera')

    @http.route([
      '/editarhorario',  
    ], type='http', auth='public' , website=True, csrf=False, METHODS= ['POST', 'GET'])
    def editarHorario (self, **kw):
      pasa = False
      global id
      try:
        idH = request.params['id']
        lab = request.env['accesscontrol.lab'].sudo().search([('estado_lab','=',True)])
        lab2 = request.env['accesscontrol.carrera'].sudo().search([('estado_carrera','=',True)])
        carrera = request.env['accesscontrol.carrera'].sudo().search([('estado_carrera','=',True)])
        materia = request.env['accesscontrol.materia'].sudo().search([('estado_materia','=',True)])
        curso = request.env['accesscontrol.curso'].sudo().search([('estado_curso','=',True)])
        docente = request.env['accesscontrol.docente'].sudo().search([('estado_docente','=',True)])
        horario = request.env['accesscontrol.horario'].sudo().search([('estado_horario','=',True)])
        fh = request.env['accesscontrol.horario'].sudo().search([('id','=',idH)])
        context = {
          'lab':lab,
          'c':lab2,
          'carrera':carrera,
          'materia':materia,
          'curso':curso,
          'docente':docente,
          'h':horario,
          'fh':fh,
          

        }
        id = idH
        pasa = True
        return request.render('accesscontrol.webeditarhorario',context)
      except:
        hora_inicio = request.params['hora_inicio']
        hora_fin= request.params['hora_fin']
        dia= request.params['dia']
        lab = request.params['lab']
        carrera = request.params['carrera']
        materia= request.params['materia']
        curso = request.params['curso']
        docente = request.params['docente']
        buscarCarrera =request.env['accesscontrol.carrera'].sudo().search([('nombre_carrera','=',carrera)])
        buscarLab =request.env['accesscontrol.lab'].sudo().search([('nombre_lab','=',lab)])
        buscarMateria =request.env['accesscontrol.materia'].sudo().search([('nombre_materia','=',materia)])
        buscarCurso =request.env['accesscontrol.curso'].sudo().search([('nombre_curso','=',curso)])
        buscarDocente =request.env['accesscontrol.docente'].sudo().search([('nombre_docente','=',docente)])
        aux = None
        listaHorario = request.env['accesscontrol.horario'].sudo().search([('estado_horario','=',True)])
        print('Print fuera del for',listaHorario)
        request.env['accesscontrol.horario'].sudo().search([('id','=',id)]).sudo().update({
          'hora_inicio':hora_inicio,
          'hora_fin':hora_fin,
          'dia':dia,
          'lab_id':buscarLab.id,
          'carrera_id':buscarCarrera.id,
          'materia_id':buscarMateria.id,
          'curso_id':buscarCurso.id,
          'docente_id':buscarDocente.id,

        })
        id = None
        print('Se edito el horarioo')
        return request.redirect('/horarios')
          
       






     