# This file is part stock_inventory_reference module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
try:
    from trytond.modules.stock_inventory_reference.tests.test_stock_inventory_reference import suite
except ImportError:
    from .test_stock_inventory_reference import suite

__all__ = ['suite']
