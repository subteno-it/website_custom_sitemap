# -*- coding: utf-8 -*-
##############################################################################
#
#    website_custom_sitemap module for OpenERP, Allow to customize the sitemap.xml file per static file upload
#    Copyright (C) 2016 SYLEAM Info Services (<http://www.Syleam.fr/>)
#              Sylvain Garancher <sylvain.garancher@syleam.fr>
#
#    This file is a part of website_custom_sitemap
#
#    website_custom_sitemap is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    website_custom_sitemap is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Website Custom Sitemap',
    'version': '1.0',
    'category': 'Custom',
    'description': """Allow to customize the sitemap.xml file per static file upload""",
    'author': 'SYLEAM',
    'website': 'http://www.syleam.fr/',
    'depends': ['website'],
    'data': [
        'views/website.xml',
    ],
    'installable': True,
    'active': False,
    'license': 'AGPL-3',
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
