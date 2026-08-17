from odoo import fields, models


class Developer(models.Model):
    _name = 'demo.developers'
    _description = 'Devs'

    name = fields.Char(string='Nom')
    website = fields.Char(string='Site web')