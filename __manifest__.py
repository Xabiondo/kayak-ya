# -*- coding: utf-8 -*-
{
    'name': "kayak-ya",
    'summary': "Gestión de alquiler de Kayaks",
    'description': """
        Módulo para gestionar las reservas de los Kayaks.
        Gestión de servicios, precios, reservas y facturación.
    """,
    'author': "Equipo KayakYa",
    'category': 'Services',
    'version': '0.1',
    'depends': ['base', 'mail', 'account'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/kayak_service_views.xml',
        'views/kayak_booking_views.xml',
        'views/res_partner_views.xml',
        'views/menu.xml',
    ],
    'application': True,
    'installable': True,
    'license': 'LGPL-3',
}