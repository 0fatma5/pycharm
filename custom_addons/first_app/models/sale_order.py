from odoo import models, fields


class SaleOrder(models.Model):
    _inherit = 'sale.order'
# model inheritNCE BYSM3 FEL DB
    property_id =fields.Many2one('property')
    # esmha gybo mn odoo dos 3ala confirm 7ytl3 esmo
    def action_confirm(self):
        res=super(SaleOrder,self).action_confirm()
        print("inside action_confirm")
        return res



