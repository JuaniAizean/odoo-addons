# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (c) 2012 Acysos S.L. (http://acysos.com) All Rights Reserved.
#                       Ignacio Ibeas <ignacio@acysos.com>
#    $Id$
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    "name" : "Product change price update draft invoice",
    "version" : "1.0",
    "author" : "Acysos S.L.",
    "category" : "Generic Modules/Inventory Control",
    "website" : "www.acysos.com",
    "description": """Change the price and description of a product and update all invoice with state draft
        Add a new product line to the invoice.
        Remove a product line for the invoice.
    """,
    "license" : "AGPL-3",
    "depends" : [
        "base",
        "account",
        "decimal_precision",
        ],
    "init_xml" : [],
    "demo_xml" : [],
    "update_xml" :['product_view.xml','wizard/product_change_price.xml'],
    "active": False,
    "installable": True
}