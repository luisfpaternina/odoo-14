{
    'name': 'Generate Reports ',

    'version': '14.0.0.0',

    'author': "Introdoo",

    'contributors': ['Luis Felipe Paternina'],

    'website': "https://www.youtube.com/results?search_query=introdoo",

    'category': 'reports',

    'depends': [

       
        'base',
        'contacts',
        'report_xlsx',
        'hr_expense',

    ],

    'data': [
        
        #'views/res_partner.xml',
        'reports/report_xlsx.xml',
                   
    ],
    'installable': True
}
