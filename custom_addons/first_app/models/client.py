from odoo import models, fields


# msh 7y3aml table gded 7yzwd 3ala el table el 2adem
class Client(models.Model):
    _name = 'client'
    _inherit = 'owner'
    client_code = fields.Char('Client Code')
    owner_id=fields.Many2one('owner', string='Owner')
    active=fields.Boolean('Active',default=True)