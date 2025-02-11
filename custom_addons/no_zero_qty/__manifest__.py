{
    'name': 'No Zero Quantity in POS',
    'version': '1.0.0',
    'category': 'Point of Sale',
    'summary': 'This module restricts the sale of products with zero or negative stock levels in the Point of Sale',
    'author': 'Anthony',
    'depends': ['base','point_of_sale'],
    'data': [
        'views/pos_config_view.xml',
    ],
    'assets':{
        'point_of_sale._assets_pos': [
            '/no_zero_qty/static/src/js/models.js',
         ],
    },
    'license':'OPL-1',
    'installable': True,
    'auto_install': False,
    'application': False
}
