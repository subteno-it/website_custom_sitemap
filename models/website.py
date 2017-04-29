# -*- coding: utf-8 -*-
# Copyright 2016 SYLEAM Info Services
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields


class Website(models.Model):
    _inherit = 'website'

    sitemap = fields.Binary(string='Sitemap.xml', help='Sitemap.xml file to replace the standard default one automatically created by Odoo.')

