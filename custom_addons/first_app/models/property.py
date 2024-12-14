from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class Property(models.Model):
    _name = 'property'
    # odoo bysuuport inheritance mn katr mn model
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = _("Property Management")

    name = fields.Char(required=True, default='New')
    # el tarcking byegy fel log file yzhrly
    description = fields.Text(tracking=1)
    postcode = fields.Char(required=True)
    data_availability = fields.Date(tracking=1)
    expected_price = fields.Float()
    selling_price = fields.Float()
    diff = fields.Float(compute='_compute_diff' ,store=1,readonly=0)
    bedrooms = fields.Integer(required=True)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection([
        ('north', 'North'),
        ('south', 'South'),
        ('east', 'East'),
        ('west', 'West')
    ], default='north')
    owner_id=fields.Many2one('owner', string='Owner')
    tag_ids = fields.Many2many('tag', string='Tags')
    # kda 7a5ly en el data el f owner tro7 l owner addres el feh prop msh lazm t3aml store hya kda kda 7t save fel db
    owner_address = fields.Char(related='owner_id.address',readonly=0,store=1)
    owner_phone = fields.Char(related='owner_id.phone',readonly=0,store=1)


    state=fields.Selection([
        ('draft', 'Draft'),
        ('pending', 'Pending'),
        ('sold', 'Sold'),
        ('closed', 'Closed'),

    ],default='draft')
# lw 3ndk record bt5alf el constraints bt3atk yb3a kda msh 7tb2a y3any msln lw enta 3ndk 2 record using the same name w ro7t 3aml el constraints dh f msh 7ytb2
    _sql_constraints = [
        ('unique_name', 'unique("name")', 'This name is exist')
    ]
    line_ids = fields.One2many('property.line','property_id')
    active=fields.Boolean('Active',default=True)
    expected_selling_date= fields.Date(tracking=1)
    is_late=fields.Boolean()


    @api.depends('expected_price', 'selling_price','owner_id.phone')


    def _compute_diff(self):
        for rec in self:
            print(rec)
            print("inside _compute_diff")
            rec.diff=rec.expected_price-rec.selling_price
    @api.onchange('expected_price')
    def _onchange_expected_price(self):
        for rec in self:
            print(rec)
            print("inside _onchange")
            return {
                'warning': {'title' : 'warning','message': "negative value.",'type': "notification"}
            }

    @api.constrains('bedrooms')
    def _check_bedrooms_greater_zero(self):
        for rec in self:
            if rec.bedrooms <= 0:  # Ensure bedrooms > 0
                raise ValidationError(_("Bedrooms must be greater than 0."))

    def action_draft(self):
        for rec in self:
            print("inside action_draft")
            rec.state = 'draft'
            # or  rec.write({'state': 'draft'})
    def action_pending(self):
        for rec in self:
            print("inside action_pending")
            rec.state = 'pending'
    def action_sold(self):
        for rec in self:
            print("inside action_sold")
            rec.state = 'sold'

    def action_closed(self):
        for rec in self:
            rec.state = 'closed'
    def check_expected_selling_date(self):
        print(self)
        property_ids=self.search([])
        for rec in property_ids:
            if rec.expected_selling_date and rec.expected_selling_date < fields.Date.today():
                rec.is_late = True



    #
    # @api.model_create_multi
    # def create(self, vals):
    #     res = super(Property, self).create(vals)
    #     print("inside create method")
    #     return res
    # @api.model
    # def _search(self, domain, offset=0, limit=None, order=None, access_rights_uid=None):
    #     res =super(Property, self)._search(domain, offset, limit, order, access_rights_uid)
    #     print("inside _search")
    #     return res
    #
    # def write(self, vals):
    #     res = super(Property, self).write(vals)
    #     print("inside write")
    #     return res
    #
    # def unlink(self):
    #     res = super(Property, self).unlink()
    #     print("inside unlink")
    #     return res
    #
    #
    #
    # line msh lines

class PropertyLine(models.Model):
    _name = 'property.line'
    property_id=fields.Many2one('property')
    area=fields.Float()
    description=fields.Char()