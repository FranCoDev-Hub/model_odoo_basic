import string
from odoo import models, fields

class HrEmployee(models.AbstractModel):

    _inherit = 'hr.employee'

    ine = fields.Char(string="Número de Credencial")