"""Planner response contract"""

from dataclasses import dataclass

@dataclass
class PlannerResponse:
    steps: list
