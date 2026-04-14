{
    'name': 'FAMTECH Website Enhancements',
    'version': '1.0',
    'summary': 'Custom dynamic pages and backend fetchers for FAMTECH.',
    'category': 'Website',
    'author': 'Jomari G. Castillo',
    'depends': ['website', 'event'], # Tells Odoo this module needs the Website and Event apps to work
    'data': [
        'views/news_template.xml',
        'views/partners.xml', # Tells Odoo to load your front-end code
    ],
    'installable': True,
    'application': False,
}