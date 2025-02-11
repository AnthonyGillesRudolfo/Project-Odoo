from odoo import api, fields, models, _

class PosConfig(models.Model):
    _inherit = 'pos.config'
    no_zero_qty = fields.Boolean(string='No Zero Quantity')

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'
    no_zero_qty = fields.Boolean(string='No Zero Quantity', related='pos_config_id.no_zero_qty', readonly=False)

class PosSession(models.Model):
    _inherit = 'pos.session'

    def _loader_param_product_product(self):
        res = super()._loader_param_product_product()
        res['search_params']['fields'].extend(['qty_available','type'])
        return res

class ProductProductInherit(models.Model):
    _inherit = 'product.product'

    @api.model
    def _load_pos_data_fields(self, config_id):
        params = super()._load_pos_data_fields(config_id)
        params += ['qty_available', 'type']
        return params