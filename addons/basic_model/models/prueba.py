from odoo import models, fields


class Prueba(models.Model):
    _name = "prueba"

    name = fields.Char(string="Nombre", required=True)
    email = fields.Char(string="E-Mail")
    age = fields.Integer(string="Edad")