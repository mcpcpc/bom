#!/usr/bin/env python
# -*- coding: utf-8 -*-

from dataclasses import dataclass
from dataclasses import field
from enum import Enum
from enum import auto
from typing import Optional
from typing import List
from typing import Union

class Classification(Enum):
    ASSEMBLY = auto()
    COMPONENT = auto()

class Unit(Enum):
    EACH = auto()
    KILOMETERS = auto()
    METERS = auto()
    DECIMETERS = auto()
    CENTIMETERS = auto()
    MILLIMETERS = auto()
    INCHES = auto()
    FEET = auto()
    YARDS = auto()
    MILES = auto()

@dataclass
class LineItem:
    """Line item representation"""
    
    classification: Classification
    unit: Unit
    quantity: Union[int, float]
    parent: Optional[int] = None
    child: Optional[int] = None
    mpn: Optional[str] = None
    description: Optional[str] = None

    def to_record(self) -> dict:
        record = {
            "classification": self.classification.name,
            "unit": self.unit.name,
            "parent": self.parent,
            "child": self.child,
            "quantity": self.quantity,
            "mpn": self.mpn,
            "description": self.description     
        }
        return record