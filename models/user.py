import pydantic
class User(pydantic.BaseModel):
    username: str
    credit: float
