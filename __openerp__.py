# coding: utf-8
{
    'name': "SP Limit Creation of Item",
    'summary': "Supercoop Limit Creation of Item",
    'description': """
        Empêche la création rapide de nouvelles fiches depuis diverses vues :
            - création d'article depuis le formulaire d'impression d'étiquettes
            - création de catégorie interne, catégorie d'étiquette, unité de mesure/achat, et fournisseur depuis le formulaire d'une fiche article
            - création de modèle d'étiquette depuis le formulaire d'une fiche d'étiquette
            - création de fournisseur depuis le formulaire de bon de commande
        (Complère le module 'Coop Limit Creation of Product' de La Louve)
    """,
    'author': "Supercoop",
    'website': "http://www.supercoop.fr",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Supercoop',
    'version': '9.0.1.0.0',
    # any module necessary for this one to work correctly
    'depends': [
        'product',
        'product_to_print',
        'purchase',
    ],
    # always loaded
    'data': [
        'views/product_pricetag_wizard.xml',
        'views/product_category_print.xml',
        'views/product_template.xml',
        'views/product_supplierinfo.xml',
        'views/purchase_order.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}