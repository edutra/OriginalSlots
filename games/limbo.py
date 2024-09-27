from fastapi import APIRouter
import random
from models.bet import LimboBet
import db

class Limbo:

    router = APIRouter()
    house_edge = 0.01

    @staticmethod
    def generate_multiplier():
        # To ensure the game has a predictable house edge, we can use this formula.
        ran = random.uniform(0, 1000000)
        return round(abs(1000000 / (1 - ran * (1 - Limbo.house_edge))), 2)

    @router.get("/limbo/bet")
    async def bet(bet: LimboBet):
        user = db.get_user(bet.username)
        if user.credit < bet.bet:
            return {"message": "Not enough credit"}

        multiplier = Limbo.generate_multiplier()

        db.update_user_credit(user.username, user.credit - bet.bet)

        if bet.multiplier is None:
            return {"message": "bet multiplier is required"}

        if multiplier >= bet.multiplier:
            new_credit = user.credit + (bet.bet * bet.multiplier)
            db.update_user_credit(user.username, new_credit)
            return {"multiplier": multiplier, "message": "You won!"}
        else:
            db.update_user_credit(user.username, user.credit)
            return {"multiplier": multiplier, "message": "You lost!"}
