from email.policy import default
from odoo import fields, models


class Administrador(models.Model):
    _name = 'accesscontrol.administrador'
    nombre_admin = fields.Char('nombre_admin', required=True) 
    apellido_admin = fields.Char('apellido_admin', required=True)
    id_tarjeta = fields.Char('id_tarjeta', required=True)
    estado = fields.Char('estado', required=True)
    contrasenia = fields.Char('contrasenia', required=True)
    usuario = fields.Char('usuario', required=True)
    correo = fields.Char('correo', required=True)
    foto= fields.Char('foto', required=False)

class Carrera(models.Model):
    _name = 'accesscontrol.carrera'
    nombre_carrera = fields.Char('nombre_carrera', required=True)
    estado_carrera = fields.Char('estado_carrera', default=True)

class Curso(models.Model):
    _name = 'accesscontrol.curso'
    nombre_curso = fields.Char('nombre_curso', required=True)
    estado_curso = fields.Char('estado_curso', default=True)
    carerra_id = fields.Many2one('accesscontrol.carrera')

class Materia(models.Model):
    _name = 'accesscontrol.materia'
    nombre_materia = fields.Char('nombre_materia', required=True)
    estado_materia = fields.Char('estado_materia', default=True)
    carrera_id = fields.Many2one('accesscontrol.carrera')

class Laboratorio(models.Model):
    _name = 'accesscontrol.lab'
    codigo_lab = fields.Char('codigo_lab', required=True)
    nombre_lab = fields.Char('nombre_lab', required=True)
    estado_lab = fields.Char('estado_lab', default=True)
    estado_puerta = fields.Char('estado_puerta', default='Cerrado')
    clave_llave = fields.Char('clave_llave', default='#')