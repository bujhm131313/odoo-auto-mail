# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup

from odoo import models, fields, api

FROM = 'Igor Kurilko <bujhm1313@gmail.com>'


class ResPartner(models.Model):
    _inherit = 'res.partner'

    subjects = fields.Char(string='Предметы')
    school = fields.Char(string='Школа')

    @api.model
    def message_new(self, msg_dict, custom_values=None):
        if msg_dict.get('email_from') == FROM:
            partner_values = self.msg_parse(msg_dict.get('body'))

            # Find partners with current email
            existing_partner = self.search([
                ('email', '=', partner_values.get('email')
                 )])

            if existing_partner:
                existing_partner.write(partner_values)
                res_id = existing_partner.ids[0]
            else:
                res_id = self.create(partner_values).id

        else:
            res_id = super(ResPartner, self).message_new(
                msg_dict, custom_values)

        # Send email
        template = self.env.ref('auto_mail.response_template')
        template.send_mail(res_id)

        return res_id

    @staticmethod
    def msg_parse(msg_body):
        soup = BeautifulSoup(msg_body)
        text_list = map(lambda x: x.text, soup.findAll("b"))

        event_name = text_list[0]
        partner_name = text_list[1]
        partner_email = text_list[2]
        partner_subject = text_list[3]
        partner_phone = text_list[4]
        partner_school = text_list[5]

        return {
            'name': partner_name,
            'email': partner_email,
            'subjects': partner_subject,
            'phone': partner_phone,
            'school': partner_school,
        }
