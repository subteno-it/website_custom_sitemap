# -*- coding: utf-8 -*-
# Copyright 2016 SYLEAM Info Services
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import odoo
from odoo import http
from odoo.http import request


class Website(odoo.addons.website.controllers.main.Website):
    @http.route()
    def sitemap_xml_index(self):
        if request.website.sitemap:
            mimetype = 'application/xml;charset=utf-8'
            content = request.website.sitemap.decode('base64')

            return request.make_response(content, [('Content-Type', mimetype)])

        return super(Website, self).sitemap_xml_index()

