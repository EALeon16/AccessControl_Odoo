from email.policy import default
from logging import warning
from odoo import fields, models, api


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

class Docente(models.Model):
    _name = 'accesscontrol.docente'
    cedula_docente = fields.Char('cedula_docente', required=True)
    nombre_docente = fields.Char('nombre_docente', required=True)
    apellido_docente = fields.Char('apellido_docente', required=True)
    correo_docente = fields.Char('correo_docente', required=True)
    estado_docente = fields.Char('estado_docente', default=True)
    id_tarjeta = fields.Char('id_tarjeta', required=True)
    carrera_id = fields.Many2one('accesscontrol.carrera')


class Estudiante(models.Model):
    _name = 'accesscontrol.estudiante'
    cedula_estudiante = fields.Char('cedula_estudiante', required=True)
    nombre_estudiante = fields.Char('nombre_estudiante', required=True)
    apellido_estudiante = fields.Char('apellido_estudiante', required=True)
    estado_estudiante = fields.Char('estado_estudiante', default=True)
    id_tarjeta = fields.Char('id_tarjeta', required=True)
    curso_id = fields.Many2one('accesscontrol.curso')

warning = fields.Boolean('warning',default=False)


class Horario(models.Model):
    _name = 'accesscontrol.horario'
    hora_inicio = fields.Char('hora_inicio', required=True)
    hora_fin = fields.Char('hora_fin', required=True)
    dia = fields.Char('dia', required=True )
    estado_horario = fields.Char('estado_horario', default=True)
    lab_id = fields.Many2one('accesscontrol.lab')
    carrera_id = fields.Many2one('accesscontrol.carrera')
    materia_id = fields.Many2one('accesscontrol.materia')
    curso_id = fields.Many2one('accesscontrol.curso')
    docente_id = fields.Many2one('accesscontrol.docente')

class DialogBoxWizard(models.TransientModel):
    """ Wizard for dialog box
    """
    _name = 'dialog.box.wizard'

    message = fields.Text('Message')
    mode = fields.Selection([
        ('ok', 'OK only'),
        ('yes_no', 'Yes / No'),
        ('cancel_confirm', 'Cancel / Confirm'),
        ], 'Mode', default='cancel_confirm')
    action = fields.Text('Action', help='Use self as reference for call')

    @api.model
    def open_dialog(self, message, action, title, mode='cancel_confirm'):
        """ Open dialog box procedure
        """
        # Create record
        current = self.create({
            'message': message,
            'mode': mode,
            'action': action,
            })

        return {
            'type': 'ir.actions.act_window',
            'name': title,
            'view_type': 'form',
            'view_mode': 'form',
            'res_id': current.id,
            'res_model': 'dialog.box.wizard',
            # 'view_id': view_id, # False
            'views': [(False, 'form')],
            'domain': [],
            'context': self.env.context,
            'target': 'new',
            'nodestroy': False,
            'flags': {
                'form': {'action_buttons': False},
                }
            }

    # --------------------
    # Wizard button event:
    # --------------------
    def action_go(self):
        """ Event for button done
        """
        return eval(self.action)