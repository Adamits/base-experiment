import src.modeling as modeling

from dataclasses import dataclass, field
from typing import AnyStr, List
import inspect

import yaml

@dataclass
class Config:
    output_path: AnyStr
    model_classname: AnyStr

    def get_model_class(self):
        """Get the actual modeling class from the provided `model_classname`"""
        models_factory = {name: cls for name, cls in self.get_model_list()}
        cls = models_factory.get(self.model_classname)

        if not cls:
            msg = f"{self.model_classname} is not implemented or was not imported from the modeling module!"
            raise NotImplementedError(msg)

        return cls

    @staticmethod
    def get_model_list():
        return inspect.getmembers(modeling, inspect.isclass)

    @classmethod
    def read(cls, fn: AnyStr):
        with open(fn) as file:
            args_dict = yaml.load(file, Loader=yaml.FullLoader)

        return Config(**args_dict)
