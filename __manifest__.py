# -*- coding: utf-8 -*-
{
    'name': "kayak-ya",

    'summary': "Gestión de alquiler de Kayaks",

    'description': "Módulo """"
        Módulo para gestionar las reservas de los Kayaks , 
        el módulo tiene : 
            Gestión de servicios y precios 
            Reservas de clientes con fechas 
            Facturación automática

    """,

    'author': "Xabi , Dani , Iván , Andoni / KayakYa",
    'website': "a rellenar",

    'category': 'Services',
    'version': '0.1',
    'depends': ['base' , 'mail' , 'account'] ,


    'data': [
        'security/security.xml' , 
        'security/ir.model.access.csv' , 



        'views/kayak_service_views.xml',
        'views/kayak_booking_views.xml' , 
        'views/res_partner_views.xml' , 
        'views/templates.xml',
    ],

    'demo': [
        'demo/demo.xml',
    ],

    'installable' : True , 
    'application' : True , 
    'license' : 'LGPL-3'
}

