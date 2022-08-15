from odoo import fields, models

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    is_part = fields.Boolean(
        string='Is Part',
        required=False)
    is_installable = fields.Boolean(
        string='Is Installable',
        required=False)
    component_ids = fields.One2many(
        comodel_name='esd.product.component',
        inverse_name='product_id',
        string='Component_ids',
        required=False)


class ESDProductComponent(models.Model):
    _name = 'esd.product.component'
    _description = 'Product Component'

    product_id = fields.Many2one(
        comodel_name='product.template',
        string='Product',
        required=False)
    part_id = fields.Many2one(
        comodel_name='product.template',
        string='Part',
        required=False, domain="[('is_part', '=', True)]")

