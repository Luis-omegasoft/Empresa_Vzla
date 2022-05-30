# -*- coding: utf-8 -*-
##############################################################################
#
#    MoviTrack
#    Copyright (C) 2020-TODAY MoviTrack.
#    You can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    It is forbidden to publish, distribute, sublicense, or sell copies
#    of the Software or modified copies of the Software.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    GENERAL PUBLIC LICENSE (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
import logging
from odoo import models, fields, api

_logger = logging.getLogger('__name__')


class ResCompany(models.Model):
    _inherit = 'res.company'

    def _get_country(self):
        country = self.env['res.country'].search([('id', '=', '238')], limit=1)
        if country.id:
            return country.id

    country_id = fields.Many2one('res.country', string="Country", default=_get_country)
    municipality_id = fields.Many2one('res.country.state.municipality', 'Municipality')
    parish_id = fields.Many2one('res.country.state.municipality.parish', 'Parish')

    @api.model
    def _address_fields(self):
        address_fields = set(super(ResCompany, self)._address_fields())
        address_fields.add('municipality_id')
        address_fields.add('parish_id')
        return list(address_fields)
