{
    'name': 'Custom Report Template',
    'version': '17.0',
    'category': 'Product',
    'summary': 'Custom Report Template',
    'description': "Custom Invoice Template",
    'website': 'https://biztras.com/',
    'author' : 'Biztras',
    'depends': ['base','account'],
    'data': [
        'report/invoice_template_custom.xml',
        'report/report.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'OEEL-1',
}
