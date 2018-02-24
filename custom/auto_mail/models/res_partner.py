# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    subjects = fields.Selection(
        [('math', 'Математика'),
         ('literature', 'Литература'),
         ], string='Предметы')

    @api.model
    def process_message(self, *args, **kwargs):
        pass
