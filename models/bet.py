import pydantic
from typing import Optional

class Bet(pydantic.BaseModel):
    username: str
    bet: float

class WheelBet(Bet):
    difficulty: int
    sectors: int

class KenoBet(Bet):
    numbers: list[int]

class LimboBet(Bet):
    multiplier: float
