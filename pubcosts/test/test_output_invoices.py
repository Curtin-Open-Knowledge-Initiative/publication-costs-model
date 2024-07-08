"""
Test cases for output_invoices
"""

import unittest
from pubcosts.categories.apcs.output_invoices import *

def create_invoices():
    test_invoice1 = Invoice("10.1032/XXXXX", "TESTID", 42.5)
    test_invoice2 = Invoice("10.1032/XXXXX", 5096, 56)
    test_invoice3 = Invoice("", "TESTID", 1024)
    test_invoice4 = Invoice("10.1032/XXXXX", "TESTID", None)

    return [test_invoice1, test_invoice2, test_invoice3, test_invoice4]


class TestInvoice(unittest.TestCase):
    def test_invoice_creation(self):
        create_invoices()


class TestInvoicedOutput(unittest.TestCase):
    def test_output_creation(self):
        invoice_list = create_invoices()
        invoice = invoice_list[0]
        test_output1 = InvoicedOutput(identifier=invoice.identifier,
                                      invoice_id=invoice.invoice_id,
                                      cost=invoice.cost)
        assert test_output1.identifier == "10.1032/XXXXX"
        assert test_output1.cost == 42.5
        assert test_output1.invoice_id == "TESTID"

        invoice = invoice_list[3]
        test_output4 = InvoicedOutput(identifier=invoice.identifier,
                                      invoice_id=invoice.invoice_id,
                                      cost=invoice.cost)
        assert test_output4.identifier == "10.1032/XXXXX"
        assert test_output4.cost is None

    def test_invoiced_output_list(self):
        invoice_list = create_invoices()
        testlist = InvoicedOutputsList(invoice_list)
        assert testlist.num_outputs() == 4
        assert testlist.num_costed() == 3
        assert len(testlist.get_outputs()) == testlist.num_outputs()
        assert testlist.get_total_cost() == 1122.5


if __name__ == '__main__':
    unittest.main()