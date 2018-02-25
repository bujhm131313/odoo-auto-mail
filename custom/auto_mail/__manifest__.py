{
    'name': "Auto mail",

    'summary': """
        Module to automatically parse and answer incoming emails
    """,

    'description': """
        Module to automatically parse and answer incoming emails
    """,

    'author': 'Igor Kurilko',
    'category': 'Uncategorized',
    'version': '0.1',

    'depends': [
        'base',
        'crm',
        'mass_mailing',
    ],

    'data': [
        # 'security/ir.model.access.csv',
        'views/res_partner.xml',

        'data/ir_actions_server.xml',
        'data/mail_template.xml',
    ],
}
