# This file is part stock_inventory_reference module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta
from trytond.pyson import Eval, Not, Equal

__all__ = ['Inventory']


class Inventory:
    __metaclass__ = PoolMeta
    __name__ = 'stock.inventory'
    reference = fields.Char("Reference",
        states={
            'readonly': Not(Equal(Eval('state'), 'draft')),
            }, depends=['state'])
