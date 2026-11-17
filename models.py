from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from enum import Enum


class ModulStatus(Enum):
    OFFEN = "offen"
    IN_BEARBEITUNG = "in_bearbeitung"


class Pruefungsart(Enum):
    KLAUSUR = "Klausur"
    HAUSARBEIT = "Hausarbeit"
    PORTFOLIO = "Portfolio"


@dataclass
class Pruefungsleistung:
    titel: str
    pruefungsart: Pruefungsart
    note: float | None = None
    datum: date | None = None

    def __post_init__(self) -> None:
        # TODO 1: Wenn note nicht None ist und nicht zwischen
        # 1.0 und 5.0 liegt, löse einen ValueError aus.
        pass

    def ist_bestanden(self) -> bool:
        return self.note is not None and self.note <= 4.0