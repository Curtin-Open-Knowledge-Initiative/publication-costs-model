"""
Calculate a per-output estimated APC based on list price
"""

from typing import Iterable, Union
from dataclasses import dataclass
from abstract import AbstractOutputList, AbstractOutput


@dataclass
class APCsPerOutput(AbstractOutput):
    total_estimated_apc: Union[float, None] = None
    local_apportionment: Union[float, None] = None


class APCsPerOutputList(AbstractOutputList):

    def __init__(self,
                 identifiers: Iterable[str],
                 **kwargs):
        super().__init__(outputs=[APCsPerOutput(identifier=identifier) for identifier in identifiers],
                         **kwargs)

    def calculate_apcs(self):
        pass
        # Lookup tables per identifier
        # Apply heuristic for cost apportionment
        # Add costs to outputs
