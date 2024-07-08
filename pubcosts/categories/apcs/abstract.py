"""
Base classes for managing DOIs and associated prices within the apc category


"""

from typing import Optional, List, Iterable, Literal, Union
from dataclasses import dataclass

import pandas as pd
import pandas_gbq

identifier_classes = ['doi', 'isbn', 'url', None]


@dataclass
class AbstractOutput:
    """
    Class for defining a single output
    """

    identifier: str = None,
    cost: List[Union[float, None]] = None


class AbstractOutputList:
    """
    Abstract class for holding sets of outputs
    """

    def __init__(self,
                 outputs: Iterable[Union[AbstractOutput, str, None]]):

        self._outputs = []
        self._df = None
        if outputs:
            for output in outputs:
                if issubclass(output.__class__, AbstractOutput):
                    self._outputs.append(output)
                elif type(output) == str:
                    self._outputs.append(AbstractOutput(identifier=output))

    def num_outputs(self) -> int:
        return len(self._outputs)

    def get_outputs(self) -> List[AbstractOutput]:
        return self._outputs

    def get_costs(self) -> Iterable[float]:
        return (output.cost for output in self.get_outputs() if output.cost is not None)

    def num_costed(self) -> int:
        return len([cost for cost in self.get_costs() if cost is not None])

    def get_total_cost(self) -> float:
        return sum(self.get_costs())

    def as_dataframe(self) -> pd.DataFrame:
        if self._df:
            return self._df
        else:
            self._df = pd.DataFrame([output.asdict() for output in self.get_outputs()])

    def make_bq_outputs_table(self,
                              bq_table_name,
                              bq_project):
        pandas_gbq.to_gbq(self.as_dataframe(),
                          destination_table=bq_table_name,
                          project_id=bq_project)
