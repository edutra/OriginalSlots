from fastapi import APIRouter

class Keno:

    router = APIRouter()

    @router.get("/keno", tags=["keno"])
    async def keno():
        return {"msg": "Keno"}
