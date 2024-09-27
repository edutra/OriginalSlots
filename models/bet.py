import pydantic

class Bet(pydantic.BaseModel):
    numbers: list[int]
    username: str
    bet: int
