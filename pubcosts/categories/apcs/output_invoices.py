"""
Calculate costs based on direct invoice data provided by institution

This module requires a dataset containing APCs and invoiced prices paid, with exactly one
price defined per DOI.
"""

from dataclasses import dataclass
from typing import List, Union

from pubcosts.categories.apcs.abstract import AbstractOutputList, AbstractOutput


@dataclass
class Invoice:
    identifier: str
    invoice_id: Union[str, int]
    cost: Union[float, None]


@dataclass
class InvoicedOutput(AbstractOutput):
    invoice_id: Union[str, int, None] = None


class InvoicedOutputsList(AbstractOutputList):
    """
    Class for managing outputs with output-level invoices
    """

    def __init__(self,
                 invoices: List[Invoice],
                 **kwargs):
        outputs = [InvoicedOutput(identifier=invoice.identifier,
                                  invoice_id=invoice.invoice_id,
                                  cost=invoice.cost)
                   for invoice in invoices]
        super().__init__(outputs=outputs,
                         **kwargs)
