# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.exceptions import UserError


class StockPickingBatch(models.Model):
    _inherit = ['stock.picking.batch']

    delivery_id = fields.Many2one('delivery.carrier', string='Método de entrega')