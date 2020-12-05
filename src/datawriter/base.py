import os

from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from typing import List


@dataclass_json
@dataclass
class Prediction:
    """Dataclass for a prediction"""
    id: str = None


class BaseWriter:
    def __init__(self, pred_dir: str):
        """Base class for writing data from predictions"""
        self.pred_dir = pred_dir

        os.makedirs(self.pred_dir, exist_ok=True)

    def make_prediction(self, samples: List):
        """Make a prediciton from samples"""
        raise NotImplementedError

    def write_prediction(self, prediction: Prediction):
        """Write the actual prediciton to an output"""
        raise NotImplementedError
