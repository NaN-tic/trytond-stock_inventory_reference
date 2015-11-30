# This file is part of the stock_inventory_reference module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class StockInventoryReferenceTestCase(ModuleTestCase):
    'Test Stock Inventory Reference module'
    module = 'stock_inventory_reference'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        StockInventoryReferenceTestCase))
    return suite
