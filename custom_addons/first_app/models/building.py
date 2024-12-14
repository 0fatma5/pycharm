from odoo import models, fields


class Building(models.Model):
    _name = 'building'
    _description = 'Building'
    _inherit = ['mail.thread','mail.activity.mixin']
    # display name lw feh filed esmo name msh lazm tsd5m dh 3al4an 7y3amlha automatic
    _rec_name = 'code'
    no =fields.Integer()
    code = fields.Char()
    description = fields.Text()
    name = fields.Char()
    active=fields.Boolean('Active',default=True)



