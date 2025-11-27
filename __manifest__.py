{
    'name': 'Gestion des Certifications',
    'version': '18.0.1.0.0',
    'category': 'Services',
    'summary': 'Module de gestion des certifications',
    'description': """
        Module de gestion des certifications
        =====================================
        * Suivi des demandes de certification
        * Gestion des audits
        * Suivi des statuts
    """,
    'author': 'Bafode Jaiteh',
    'website': 'https://github.com/bvfode',
    'license': 'LGPL-3',
    'depends': ['base', 'mail'],
    'data': [
        'data/sequence.xml',
        'security/ir.model.access.csv',
        'views/certification_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
