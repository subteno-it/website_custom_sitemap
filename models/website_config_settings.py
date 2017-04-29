# -*- coding: utf-8 -*-
# Copyright 2016 SYLEAM Info Services
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields


class WebsiteConfigSettings(models.TransientModel):
    _inherit = 'website.config.settings'

    sitemap = fields.Binary(string='Sitemap.xml', related='website_id.sitemap', help='Sitemap.xml file to replace the standard default one automatically created by Odoo.')

