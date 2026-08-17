from odoo import fields, models

class Tag(models.Model):
    _name = 'demo.tags' # demo_tags
    _description = 'Tags'

    name = fields.Char(string='Nom')