import pydantic
from typing import Optional

class Bet(pydantic.BaseModel):
    numbers: Optional[list[int]] = None
    multiplier: Optional[float] = None
    username: str
    bet: float
