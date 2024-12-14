from odoo import models, fields


class Owner(models.Model):
    _name = 'owner'
    name=fields.Char('Owner Name',required=True)
    phone=fields.Char('Phone')
    address=fields.Char('Address')

    property_ids=fields.One2many('property','owner_id',string='Property')

