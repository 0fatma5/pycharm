{
    'name': "first_app",
    'author': "Fatma Ahmed",
    'category': '',
    'version': '17.0.0.1.0',
    'depends': [
        'base','sale_management','account','mail'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/base_menu.xml',
        'views/Property_view.xml',
        'views/owner_view.xml',
        'views/tag_view.xml',
        'views/sale_order_view.xml',
        'views/building_view.xml',
        'reports/property_report.xml'


    ],
    'assets':
        {
            'web.assets_backend':['first_app\static\src\css\property.css']
        },
    'application': True
}