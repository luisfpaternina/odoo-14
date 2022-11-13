{
    'name': 'Credit limit',

    'version': '14.0.0.0',

    'author': "Luis Felipe Paternina",

    'contributors': ['Luis Felipe Paternina'],

    'website': "https://www.youtube.com/results?search_query=introdoo",

    'category': 'account',

    'depends': [

       
        'base',
        'sale_management',
        'account_accountant',
        'contacts',

    ],

    'data': [
        
        'data/sequences.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/credit_limit.xml',
        'views/res_partner.xml',
        'views/sale_order.xml',
        'reports/credit_limit_report.xml',
                   
    ],
    'installable': True
}
